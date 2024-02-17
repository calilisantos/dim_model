from dim_model.read import Read
import pandas as pd
from unittest import TestCase
from unittest.mock import patch, Mock


class TestRead(TestCase):
    def setUp(self):
        self._read_instance = Read()

    @patch(
        'dim_model.read.pd.read_excel',
        return_value=Mock(spec=pd.DataFrame)
    )
    def test_set_data__with_success(self, mock_read_excel):
        mock_read_excel.return_value = Mock(spec=pd.DataFrame)
        self._read_instance._set_data()
        self.assertIsInstance(self._read_instance._data, list)

    @patch('dim_model.read.pd.read_excel')
    def test_set_data__with_failure(self, mock_read_excel):
        mock_read_excel.side_effect = Exception("Error")
        with self.assertRaises(Exception):
            self.read_instance._set_data()

    @patch(
        'dim_model.read.pd.concat',
        return_value=Mock(spec=pd.DataFrame)
    )
    def test_set_dataframe__with_success(self, mock_concat):
        mock_concat.return_value = Mock(spec=pd.DataFrame)
        self._read_instance._set_dataframe()
        self.assertIsInstance(self._read_instance._dataframe, pd.DataFrame)

    @patch(
        'dim_model.read.pd.concat',
        return_value=Mock(spec=pd.DataFrame)
    )
    @patch(
        'dim_model.read.pd.read_excel',
        return_value=Mock(spec=pd.DataFrame)
    )
    def test_read_data__with_success(self, mock_read_excel, mock_concat):
        self._read_instance._set_data()
        self._read_instance._set_dataframe()
        self._read_instance.read_data()
        self.assertIsInstance(self._read_instance._dataframe, pd.DataFrame)
