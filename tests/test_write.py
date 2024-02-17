from dim_model.write import Write
import pandas as pd
from unittest import TestCase
from unittest.mock import Mock


class TestWrite(TestCase):
    def setUp(self):
        mock_df = Mock(spec=pd.DataFrame)
        self._write = Write(mock_df, 'table_name', False)

    def test_write_data__exists(self):
        self._write.write_data()
        self.assertTrue(hasattr(self._write, 'write_data'))

    def test_table_name__has_setter(self):
        self.assertEqual(self._write._table_name, 'table_name')

    def test_set_index__has_setter(self):
        self.assertFalse(self._write._set_index, False)

    def test_df__has_setter(self):
        self.assertIsInstance(self._write._df, pd.DataFrame)
