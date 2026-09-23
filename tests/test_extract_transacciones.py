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