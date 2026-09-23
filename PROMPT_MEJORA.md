# Prompt para Mejorar el Codigo Base

Copia y pega el contenido del bloque de abajo en un asistente de IA (Claude, ChatGPT)
para obtener un ZIP con el proyecto completo y arrancable.

Si preferis trabajar en tu editor con un agente local (Claude Code, Cursor, Copilot), usa `AGENTS.md` en vez de este archivo: dice lo mismo pero para que escriba los archivos en disco.

## Las dos reglas que no se negocian

1. **Completa el boilerplate.** Todo lo que el proyecto necesita para compilar y arrancar: manifiesto de dependencias, punto de entrada, configuracion, capa de interfaz, y las capas del patron arquitectonico declarado. Eso es andamiaje y es tu trabajo.
2. **NO resuelvas el reto.** Los entregables de las fases son el trabajo de la persona. El hueco pedagogico se deja como esta: el proyecto arranca, pero lo que el reto pide implementar NO esta implementado.

Dicho de otra forma: si algo impide compilar, arreglalo. Si algo es logica de negocio incompleta, validaciones ausentes, un secreto hardcodeado o un patron mejorable, dejalo exactamente como esta — es lo que la persona tiene que encontrar.

## Lo que le falta a este proyecto

Esto NO lo tenes que adivinar: salio de comparar el proyecto contra la arquitectura declarada del reto y de un analisis estatico del codigo. Completalo TODO.

### Referencias colgando en el codigo que si esta

Cada una rompe la compilacion:

- `requirements.txt` — `pyspark-sql@3.5.0`: pyspark-sql declara la version 3.5.0, pero PyPI respondio que esa version no existe. Es una version inventada: reemplazala por una version publicada real, o si no se conoce con certeza, usa el mecanismo centralizado del ecosistema (BOM/parent/platform/version catalog) y no declares una version individual.

## Como saber que terminaste

```bash
pip install -r requirements.txt && pytest -q
```

Ese comando corriendo sin errores es la definicion de "listo".

---

```
## Briefing del reto (autoridad)
Este bloque manda sobre los archivos adjuntos. El stack y el rol salen de AQUÍ, no de un topic genérico ni de markdown placeholder.

### Perfil
Chapter Ciencia de Datos, Especialidad Ingeniero de Datos, Tecnología PySpark, Advanced

### Brecha de conocimiento
Construye procesos de transformacion y carga idempotentes con reglas de calidad y cuarentena de registros invalidos

### Misión / candidato
Consolidar las transacciones diarias en el modelo analitico

### Datos adicionales
Candidato con 3 años en datos

### Reto
- Tema: pipelines de transformacion y carga
- Seniority: advanced-l2
- Tipo: practical
- Título: Consolidación de transacciones diarias en el modelo analítico
- Tiempo estimado: 8 horas

### Fases (trabajo del HUMANO — PROHIBIDO completarlas)
No implementes estos entregables. Dejalos como hueco pedagógico. El asistente solo materializa el proyecto arrancable para que el participante pueda trabajar.
- Fase 1: Exploración y modelado de datos — objetivo: Comprender la estructura y las reglas de las transacciones provenientes de las diferentes fuentes. — entregable (NO resolver): Esquema de transacciones modeladas y reglas de calidad documentadas.
- Fase 2: Transformación de datos — objetivo: Transformar las transacciones de acuerdo a las reglas de calidad y asegurar la idempotencia del proceso. — entregable (NO resolver): Proceso de transformación idempotente con reglas de calidad aplicadas y mecanismo de cuarentena para registros inválidos.
- Fase 3: Carga de datos en el modelo analítico — objetivo: Cargar las transacciones transformadas en el modelo analítico de manera idempotente. — entregable (NO resolver): Transacciones cargadas en el modelo analítico con idempotencia asegurada y registros inválidos en cuarentena.

Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 0 — ¿Esto es un proyecto o una carcasa?
Antes de extraer archivos, leé el Briefing (si está) y diagnosticá el adjunto.

Es CARCASA si ocurre CUALQUIERA de estas:
- No hay manifiesto de dependencias del stack del briefing (manifest.json de VTEX IO / package.json / pom.xml / build.gradle / requirements.txt / go.mod / *.tf / *.csproj, según corresponda)
- Hay un "binario" que en realidad es un comentario ("no puede ser mostrado como texto plano", placeholder .fig/.docx vacío)
- Los markdowns ya completan entregables de fases posteriores ("se implementó fade-in", lista de áreas ya resuelta)

Si es CARCASA:
- MATERIALIZÁ un proyecto que arranca en el stack del briefing (VTEX IO Store Framework, Angular, Terraform, pytest, Nest, etc.). Incluí manifiesto, punto de entrada y capa de interfaz reales.
- NO copies los markdowns de "solución" como si fueran el producto. Son ruido de generación.
- NO resuelvas las fases del briefing (están marcadas PROHIBIDO). Dejá el hueco pedagógico: el flujo existe, las microinteracciones/calidad/infra que el reto pide NO están hechas.
- Después seguí al PASO 5 (ZIP).

Si es un proyecto REAL (manifiesto + código que compila o arranca):
- Seguí PASO 1 en adelante. 🔴 compilación sí. 🟡 pedagógico no.

PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Exportación en ZIP
Empaqueta todos los archivos en un único archivo ZIP descargable respetando exactamente
la estructura de rutas indicada por los marcadores.
El ZIP debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: El ZIP debe estar listo para descargar al finalizar. No preguntes si el usuario
quiere generarlo. Simplemente genera el archivo y proporciona el enlace de descarga; No debes desplegar en el chat el resumen de lo que arreglaste al Zip, solo entregalo.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación, placeholders o binarios fake, NO la reproduzcas:
aplicá PASO 0 (materializar el proyecto del briefing). Reproducir la carcasa es un fallo.
No agregues texto después del enlace de descarga del ZIP
No preguntes si el usuario quiere el ZIP: simplemente generalo siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:

// === ARCHIVO: requirements.txt ===
pyspark==3.5.0
apache-airflow==2.9.2
pandas==2.2.2
pytest==8.1.1
pydantic==2.7.1
pyspark-sql==3.5.0
python-dateutil==2.9.0.post0
six==1.16.0
numpy==1.26.4
pyarrow==15.0.2

# === ARCHIVO: src/schemas/transacciones_schema.py ===
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

// === ARCHIVO: dags/transacciones_etl_dag.py ===
from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from src.extract.extract_transacciones import extract_transacciones
from src.transform.transform_transacciones import transform_transacciones
from src.load.load_transacciones import load_transacciones

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'transacciones_etl_dag',
    default_args=default_args,
    description='ETL para consolidar transacciones diarias',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(1),
    catchup=False,
)

extract_task = PythonOperator(
    task_id='extract_transacciones',
    python_callable=extract_transacciones,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_transacciones',
    python_callable=transform_transacciones,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_transacciones',
    python_callable=load_transacciones,
    dag=dag,
)

extract_task >> transform_task >> load_task

// === ARCHIVO: src/extract/extract_transacciones.py ===
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when
from src.schemas.transacciones_schema import TransaccionPydantic

class ExtractTransacciones:
    def __init__(self, spark: SparkSession):
        self.spark = spark

    def extract_from_sources(self):
        try:
            # Simulación de lectura de datos de diferentes fuentes
            df_pagos = self.spark.read.format('csv').option('header', 'true').load('data/pagos.csv')
            df_cuentas = self.spark.read.format('csv').option('header', 'true').load('data/cuentas.csv')
            df_tarjetas = self.spark.read.format('csv').option('header', 'true').load('data/tarjetas.csv')

            # Unificación de los DataFrames
            df_transacciones = df_pagos.union(df_cuentas).union(df_tarjetas)

            # Filtrado de transacciones válidas
            df_transacciones = df_transacciones.filter((col('fecha')!= '') & (col('monto') > 0))

            return df_transacciones
        except Exception as e:
            print(f'Error al extraer transacciones: {e}')
            return None

def extract_transacciones():
    spark = SparkSession.builder.appName('ExtractTransacciones').getOrCreate()
    extractor = ExtractTransacciones(spark)
    return extractor.extract_from_sources()

// === ARCHIVO: src/transform/transform_transacciones.py ===
from pyspark.sql import functions as F
from pyspark.sql.types import StringType
from src.schemas.transacciones_schema import ReglaCalidad, validar_esquema, aplicar_reglas_calidad

class TransformTransacciones:
    def __init__(self):
        pass

    def apply_rules(self, df):
        try:
            # Aplicación de reglas de calidad
            reglas = [
                ReglaCalidad('fecha_no_nula', lambda row: row['fecha']!= '', 'drop', 1.0),
                ReglaCalidad('monto_positivo', lambda row: row['monto'] > 0, 'drop', 1.0),
            ]
            df_validado = aplicar_reglas_calidad(df, reglas)

            # Transformación de datos
            df_transformado = df_validado.withColumn('fecha', F.to_date(col('fecha'), 'yyyy-MM-dd'))
            df_transformado = df_transformado.withColumn('monto', col('monto').cast('double'))
            df_transformado = df_transformado.withColumn('tipo', when(col('tipo') == 'pago', 'PAGO').otherwise('OTRO'))

            return df_transformado
        except Exception as e:
            print(f'Error al transformar transacciones: {e}')
            return None

def transform_transacciones():
    spark = SparkSession.builder.appName('TransformTransacciones').getOrCreate()
    transformer = TransformTransacciones()
    df_extracted = extract_transacciones()
    if df_extracted is not None:
        return transformer.apply_rules(df_extracted)
    return None


// === ARCHIVO: src/load/load_transacciones.py ===
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from src.utils.idempotency_utils import generar_hash_idempotencia
from src.utils.quality_rules import ReglaCalidad, validar_esquema
from src.schemas.transacciones_schema import TransaccionPydantic

class LoadTransacciones:
    def __init__(self, spark: SparkSession):
        self.spark = spark
        self.transacciones_df = None

    def cargar_transacciones(self, transacciones_df: pd.DataFrame):
        self.transacciones_df = transacciones_df
        self._aplicar_reglas_calidad()
        self._cargar_en_modelo_analitico()

    def _aplicar_reglas_calidad(self):
        reglas = [
            ReglaCalidad('regla_moneda', TransaccionPydantic.validar_moneda, 'quarentine', 0.0),
            ReglaCalidad('regla_tipo', TransaccionPydantic.validar_tipo, 'quarentine', 0.0),
            ReglaCalidad('regla_fecha', TransaccionPydantic.validar_fecha, 'quarentine', 0.0)
        ]
        validar_esquema(self.transacciones_df)
        self.transacciones_df = aplicar_reglas_calidad(self.transacciones_df, reglas)

    def _cargar_en_modelo_analitico(self):
        transacciones_spark_df = self.spark.createDataFrame(self.transacciones_df)
        transacciones_spark_df = transacciones_spark_df.withColumn('idempotency_key', generar_hash_idempotencia(transacciones_spark_df))
        transacciones_spark_df.write.parquet('/path/to/modelo_analitico', mode='append')

    def _mover_a_cuarentena(self, df: pd.DataFrame):
        df.to_csv('/path/to/quarentine', mode='a', header=False)

// === ARCHIVO: src/utils/quality_rules.py ===
from pyspark.sql import DataFrame
from pydantic import BaseModel, validator
from typing import Dict

class ReglaCalidad:
    def __init__(self, nombre: str, expresion_condicional, accion: str, umbral: float = 0.0):
        self.nombre = nombre
        self.expresion_condicional = expresion_condicional
        self.accion = accion
        self.umbral = umbral

    def aplicar(self, df: DataFrame) -> DataFrame:
        filtered_df = df.filter(self.expresion_condicional)
        if self.accion == 'quarentine':
            df = df.subtract(filtered_df)
        return df

class TransaccionPydantic(BaseModel):
    moneda: str
    tipo: str
    fecha: str
    @validator('moneda')
    def validar_moneda(cls, v):
        if v not in ['USD', 'EUR', 'GBP']:
            raise ValueError('Moneda no soportada')
        return v
    @validator('tipo')
    def validar_tipo(cls, v):
        if v not in ['debito', 'credito']:
            raise ValueError('Tipo de transacción no soportado')
        return v
    @validator('fecha')
    def validar_fecha(cls, v):
        try:
            pd.to_datetime(v)
        except ValueError:
            raise ValueError('Formato de fecha no válido')
        return v

def validar_esquema(df: DataFrame) -> DataFrame:
    expected_columns = ['moneda', 'tipo', 'fecha']
    missing_columns = [col for col in expected_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f'Columnas faltantes en el esquema: {missing_columns}')
    return df

def aplicar_reglas_calidad(df: DataFrame, reglas: list) -> Dict[str, DataFrame]:
    result = {}
    for regla in reglas:
        result[regla.nombre] = regla.aplicar(df)
    return result

// === ARCHIVO: src/utils/idempotency_utils.py ===
from pyspark.sql import DataFrame
from pyspark.sql.functions import md5, concat_ws

def generar_hash_idempotencia(row: Dict) -> str:
    return md5(concat_ws('-', *[str(val) for val in row.values()])).alias('idempotency_key')

def estrategia_reintento(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f'Error: {e}. Reintentando...')
            return func(*args, **kwargs)
    return wrapper


// === ARCHIVO: tests/test_extract_transacciones.py ===
import pytest
from src.extract.extract_transacciones import extract_transacciones
from pyspark.sql import DataFrame

class TestExtractTransacciones:

    def setup_method(self):
        self.data_source = 'sample_data.csv'
        self.expected_columns = ['fecha', 'tipo', 'monto', 'moneda']

    def test_extract_transacciones(self):
        df = extract_transacciones(self.data_source)
        assert isinstance(df, DataFrame), 'El resultado debe ser un DataFrame'
        assert all(col in df.columns for col in self.expected_columns), 'El DataFrame debe contener las columnas esperadas'

    def test_extract_transacciones_invalid_source(self):
        invalid_source = 'non_existent_data.csv'
        with pytest.raises(FileNotFoundError):
            extract_transacciones(invalid_source)

// === ARCHIVO: tests/test_transform_transacciones.py ===
import pytest
from src.schemas.transacciones_schema import TransaccionPydantic, validar_esquema, aplicar_reglas_calidad
from pyspark.sql import DataFrame

class TestTransformTransacciones:

    def setup_method(self):
        self.sample_data = [('2024-07-21', 'pago', 100.0, 'USD'), ('2024-07-21', 'retiro', -50.0, 'USD')]
        self.invalid_data = [('2024-07-21', 'pago', 'invalid', 'USD')]

    def test_validar_esquema(self):
        df = DataFrame(self.sample_data, ['fecha', 'tipo', 'monto', 'moneda'])
        valid_df = validar_esquema(df)
        assert isinstance(valid_df, DataFrame), 'El resultado debe ser un DataFrame'
        assert valid_df.count() == 2, 'Debe haber 2 registros válidos'

    def test_aplicar_reglas_calidad(self):
        df = DataFrame(self.sample_data, ['fecha', 'tipo', 'monto', 'moneda'])
        reglas_calidad = aplicar_reglas_calidad(df)
        assert isinstance(reglas_calidad, dict), 'El resultado debe ser un diccionario'
        assert 'validos' in reglas_calidad and 'invalidos' in reglas_calidad, 'El diccionario debe contener claves 'validos' e 'invalidos''

    def test_invalid_data(self):
        df = DataFrame(self.invalid_data, ['fecha', 'tipo', 'monto', 'moneda'])
        reglas_calidad = aplicar_reglas_calidad(df)
        assert reglas_calidad['invalidos'].count() == 1, 'Debe haber 1 registro inválido'

// === ARCHIVO: tests/test_load_transacciones.py ===
import pytest
from src.load.load_transacciones import load_transacciones
from pyspark.sql import DataFrame

class TestLoadTransacciones:

    def setup_method(self):
        self.sample_data = [('2024-07-21', 'pago', 100.0, 'USD')]
        self.df = DataFrame(self.sample_data, ['fecha', 'tipo', 'monto', 'moneda'])

    def test_load_transacciones(self):
        load_transacciones(self.df)
        # Aquí iría la verificación de que los datos fueron cargados correctamente,
        # lo cual depende de la implementación específica de load_transacciones.
        # Por ejemplo, podría verificarse en una base de datos o un archivo de salida.
        # Este es un ejemplo simplificado.
        assert True, 'Carga de transacciones debe ser verificada'

    def test_idempotency(self):
        load_transacciones(self.df)
        load_transacciones(self.df)
        # Verificación de idempotencia, por ejemplo, contando registros únicos.
        # Este es un ejemplo simplificado.
        assert True, 'Carga idempotente debe ser verificada'

    def test_quarantine(self):
        invalid_data = [('2024-07-21', 'pago', 'invalid', 'USD')]
        invalid_df = DataFrame(invalid_data, ['fecha', 'tipo', 'monto', 'moneda'])
        load_transacciones(invalid_df)
        # Verificación de que los datos inválidos están en cuarentena.
        # Este es un ejemplo simplificado.
        assert True, 'Registros inválidos deben estar en cuarentena'

// === ARCHIVO: conf/config_dev.json ===
{
  "database": {
    "host": "localhost",
    "port": 5432,
    "username": "dev_user",
    "password": "dev_password",
    "name": "dev_db"
  },
  "s3": {
    "bucket_name": "dev-data-bucket",
    "access_key": "dev_access_key",
    "secret_key": "dev_secret_key"
  },
  "airflow": {
    "dags_folder": "dags/",
    "sql_alchemy_conn": "sqlite:////tmp/airflow.db"
  },
  "idempotency_key": "dev_idempotency_key",
  "quarantine_folder": "/tmp/quarantine/",  
  "log_level": "DEBUG"
}

// === ARCHIVO: README.md ===
# Proyecto de Consolidación de Transacciones Diarias

## Descripción
Este proyecto implementa un pipeline ETL para consolidar transacciones diarias en el modelo analítico de una institución financiera. El proceso asegura la calidad de los datos mediante reglas de validación y coloca en cuarentena los registros inválidos.

## Configuración del Entorno
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu-repositorio.git
   cd tu-repositorio
   ```
2. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Configurar el entorno de desarrollo:
   Copiar `conf/config_dev.json` a la raíz del proyecto y ajustar las configuraciones según sea necesario.

## Ejecución del Pipeline
1. Iniciar el servidor de Airflow:
   ```bash
   airflow db init
   airflow users create --username admin --password admin --firstname admin --lastname admin --role Admin --email admin@example.com
   airflow webserver &
   airflow scheduler
   ```
2. Ejecutar el DAG de ETL:
   ```bash
   airflow dags trigger -d transacciones_etl_dag
   ```

## Validación de Resultados
1. Verificar los datos cargados en la base de datos:
   ```sql
   SELECT * FROM transacciones_consolidadas;
   ```
2. Revisar los registros inválidos en la carpeta de cuarentena:
   ```bash
   ls /tmp/quarantine/
   ```

## Estructura de Carpetas
- `dags/`: Contiene los DAGs de Airflow.
- `src/`: Contiene el código fuente del pipeline.
  - `extract/`: Módulos para la extracción de datos.
  - `transform/`: Módulos para la transformación de datos.
  - `load/`: Módulos para la carga de datos.
  - `utils/`: Utilidades y funciones auxiliares.
- `tests/`: Contiene los casos de prueba.
- `conf/`: Configuraciones por ambiente.

## Dependencias
- `pyspark==3.5.0`
- `apache-airflow==2.9.2`
- `pandas==2.2.2`
- `pytest==8.1.1`
- `pydantic==2.7.1`
- `pyspark-sql==3.5.0`
- `python-dateutil==2.9.0.post0`
- `six==1.16.0`
- `numpy==1.26.4`
- `pyarrow==15.0.2`

```
