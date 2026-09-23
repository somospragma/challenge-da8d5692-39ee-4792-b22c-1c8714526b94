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