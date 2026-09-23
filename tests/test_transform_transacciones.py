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