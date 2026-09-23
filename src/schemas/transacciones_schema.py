"""Esquema y reglas de validación para las transacciones financieras.

Este módulo define:
- El esquema estructural de las transacciones (tipos de datos, campos requeridos).
- Reglas de calidad para validar la integridad de los registros.
- Métodos para aplicar las reglas y identificar registros inválidos.
"""

from pyspark.sql.types import (
    StructType, StructField, StringType, DoubleType,
    TimestampType, IntegerType, BooleanType
)
from pyspark.sql import DataFrame
from pyspark.sql.functions import col, when, lit, current_timestamp
import pandas as pd
from pydantic import BaseModel, validator, Field
from typing import List, Optional, Dict
from datetime import datetime
import re

# -----------------------------------------------------
# Esquema estructural de las transacciones
# -----------------------------------------------------
TRANSACCIONES_SCHEMA = StructType([
    StructField("id_transaccion", StringType(), False),
    StructField("fuente", StringType(), False),
    StructField("tipo", StringType(), False),
    StructField("monto", DoubleType(), False),
    StructField("moneda", StringType(), False),
    StructField("fecha_procesamiento", TimestampType(), False),
    StructField("fecha_transaccion", TimestampType(), False),
    StructField("cuenta_origen", StringType(), True),
    StructField("cuenta_destino", StringType(), True),
    StructField("estado", StringType(), True),
    StructField("metadata", StringType(), True),
    StructField("hash_idempotencia", StringType(), True)
])

# -----------------------------------------------------
# Reglas de calidad de datos
# -----------------------------------------------------
class ReglaCalidad:
    """Representa una regla de calidad con umbral y acción."""

    def __init__(self, nombre: str, expresion_condicional, accion: str, umbral: float = 0.0):
        self.nombre = nombre
        self.expresion = expresion_condicional
        self.accion = accion  # "cuarentena" o "correccion"
        self.umbral = umbral

    def aplicar(self, df: DataFrame) -> DataFrame:
        """Aplica la regla al DataFrame y marca los registros inválidos."""
        return df.withColumn(
            "_regla_fallida",
            when(self.expresion, lit(self.nombre)).otherwise(lit(None))
        )

# Reglas de calidad para transacciones
REGLAS_CALIDAD = [
    ReglaCalidad(
        nombre="monto_no_positivo",
        expresion_condicional=(col("monto") <= 0),
        accion="cuarentena"
    ),
    ReglaCalidad(
        nombre="moneda_invalida",
        expresion_condicional=~col("moneda").isin(["USD", "EUR", "COP", "MXN", "CLP", "PEN", "ARS"]),
        accion="cuarentena"
    ),
    ReglaCalidad(
        nombre="fecha_transaccion_futura",
        expresion_condicional=(col("fecha_transaccion") > current_timestamp()),
        accion="cuarentena"
    ),
    ReglaCalidad(
        nombre="id_transaccion_vacio",
        expresion_condicional=(col("id_transaccion").isNull() | (col("id_transaccion") == "")),
        accion="cuarentena"
    ),
    ReglaCalidad(
        nombre="tipo_transaccion_invalido",
        expresion_condicional=~col("tipo").isin(["PAGO", "TRANSFERENCIA", "RETIRO", "DEPOSITO", "AJUSTE"]),
        accion="cuarentena"
    ),
    ReglaCalidad(
        nombre="cuenta_origen_vacia_para_transferencia",
        expresion_condicional=(
            (col("tipo") == "TRANSFERENCIA") &
            (col("cuenta_origen").isNull() | (col("cuenta_origen") == ""))
        ),
        accion="cuarentena"
    )
]

# -----------------------------------------------------
# Modelo Pydantic para validación adicional
# -----------------------------------------------------
class TransaccionPydantic(BaseModel):
    """Modelo Pydantic para validación de transacciones individuales."""

    id_transaccion: str = Field(..., min_length=1)
    fuente: str
    tipo: str
    monto: float = Field(..., gt=0)
    moneda: str
    fecha_procesamiento: datetime
    fecha_transaccion: datetime
    cuenta_origen: Optional[str] = None
    cuenta_destino: Optional[str] = None
    estado: Optional[str] = None
    metadata: Optional[str] = None
    hash_idempotencia: Optional[str] = None

    @validator('moneda')
    def validar_moneda(cls, v):
        if v not in {"USD", "EUR", "COP", "MXN", "CLP", "PEN", "ARS"}:
            raise ValueError('Moneda no válida')
        return v

    @validator('tipo')
    def validar_tipo(cls, v):
        if v not in {"PAGO", "TRANSFERENCIA", "RETIRO", "DEPOSITO", "AJUSTE"}:
            raise ValueError('Tipo de transacción no válido')
        return v

    @validator('fecha_transaccion')
    def validar_fecha(cls, v):
        if v > datetime.now():
            raise ValueError('Fecha de transacción no puede ser futura')
        return v

# -----------------------------------------------------
# Funciones utilitarias para manejo de esquemas
# -----------------------------------------------------
def validar_esquema(df: DataFrame) -> DataFrame:
    """Valida que el DataFrame cumpla con el esquema esperado."""
    try:
        df.sparkSession.createDataFrame(df.rdd, TRANSACCIONES_SCHEMA)
        return df
    except Exception as e:
        raise ValueError(f"Esquema inválido: {str(e)}")

def aplicar_reglas_calidad(df: DataFrame) -> Dict[str, DataFrame]:
    """Aplica todas las reglas de calidad y retorna DataFrames válidos e inválidos."""
    df_valid = df
    df_invalidos = None

    for regla in REGLAS_CALIDAD:
        df_regla = regla.aplicar(df_valid)
        # Separar registros válidos e inválidos para esta regla
        invalidos = df_regla.filter(col("_regla_fallida") == regla.nombre)

        if df_invalidos is None:
            df_invalidos = invalidos
        else:
            df_invalidos = df_invalidos.union(invalidos)

        df_valid = df_regla.filter(col("_regla_fallida").isNull()).drop("_regla_fallida")

    # Añadir metadatos de validación
    df_valid = df_valid.withColumn("_validacion_pasada", lit(True))
    if df_invalidos is not None:
        df_invalidos = df_invalidos.withColumn("_validacion_pasada", lit(False))

    return {"validos": df_valid, "invalidos": df_invalidos}

def generar_hash_idempotencia(row: Dict) -> str:
    """Genera un hash único para idempotencia basado en los campos clave."""
    import hashlib
    clave = f"{row['id_transaccion']}_{row['fuente']}_{row['monto']}_{row['fecha_transaccion']}"
    return hashlib.md5(clave.encode('utf-8')).hexdigest()

def convertir_a_pandas(df: DataFrame) -> pd.DataFrame:
    """Convierte un DataFrame de Spark a pandas con validación Pydantic."""
    pdf = df.toPandas()
    for _, row in pdf.iterrows():
        try:
            TransaccionPydantic(**row.to_dict())
        except Exception as e:
            raise ValueError(f"Validación Pydantic fallida: {str(e)}")
    return pdf