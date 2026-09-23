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