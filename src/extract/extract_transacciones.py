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