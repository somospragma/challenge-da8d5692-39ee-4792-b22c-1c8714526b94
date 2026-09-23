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