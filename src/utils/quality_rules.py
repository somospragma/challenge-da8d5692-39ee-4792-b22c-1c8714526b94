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