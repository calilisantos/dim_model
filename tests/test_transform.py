from dim_model.transform import Transform
import pandas as pd
from unittest import TestCase
from unittest.mock import patch, Mock


class TestTransform(TestCase):
    def setUp(self):
        mock_df = Mock(spec=pd.DataFrame)
        self._transform = Transform(mock_df)

    @patch(
        'dim_model.transform.Transform._drop_null_values',
        return_value=Mock(spec=pd.DataFrame)
    )
    def test_drop_null_values__return(self, mock_drop_null_values):
        self._transform._drop_null_values()
        self.assertIsInstance(self._transform._accur_data, pd.DataFrame)

    @patch(
        'dim_model.transform.Transform._drop_duplicated_columns',
        return_value=Mock(spec=pd.DataFrame)
    )
    def test_drop_duplicated_columns__return(self, mock_drop_duplicated_columns):
        self._transform._drop_duplicated_columns()
        self.assertIsInstance(self._transform._accur_data, pd.DataFrame)

    @patch(
        'dim_model.transform.Transform._transform_bank_column',
        return_value=Mock(spec=pd.DataFrame)
    )
    def test_transform_bank_column__return(self, mock_transform_bank_column):
        self._transform._transform_bank_column()
        self.assertIsInstance(self._transform._accur_data, pd.DataFrame)

    @patch(
        'dim_model.transform.Transform._transform_cod_column',
        return_value=Mock(spec=pd.DataFrame)
    )
    def test_transform_cod_column__return(self, mock_transform_cod_column):
        self._transform._transform_cod_column()
        self.assertIsInstance(self._transform._accur_data, pd.DataFrame)

    @patch(
        'dim_model.transform.Transform._transform_value_column',
        return_value=Mock(spec=pd.DataFrame)
    )
    def test_transform_value_column__return(self, mock_transform_value_column):
        self._transform._transform_value_column()
        self.assertIsInstance(self._transform._accur_data, pd.DataFrame)

    @patch(
        'dim_model.transform.Transform._transform_date_columns',
        return_value=Mock(spec=pd.DataFrame)
    )
    def test_transform_date_columns__return(self, mock_transform_date_columns):
        self._transform._transform_date_columns()
        self.assertIsInstance(self._transform._accur_data, pd.DataFrame)

    @patch(
        'dim_model.transform.Transform._cast_date_columns',
        return_value=Mock(spec=pd.DataFrame)
    )
    def test_cast_date_columns__return(self, mock_cast_date_columns):
        self._transform._cast_date_columns()
        self.assertIsInstance(self._transform._accur_data, pd.DataFrame)

    @patch(
        'dim_model.transform.Transform._create_is_in_cash_column',
        return_value=Mock(spec=pd.DataFrame)
    )
    def test_create_is_in_cash_column__return(self, mock_create_is_in_cash_column):
        self._transform._create_is_in_cash_column()
        self.assertIsInstance(self._transform._accur_data, pd.DataFrame)

    @patch(
        'dim_model.transform.Transform.transform_data',
        return_value=Mock(spec=pd.DataFrame)
    )
    def test_transform_data__return(self, mock_transform_data):
        self._transform.transform_data()
        self.assertIsInstance(self._transform._accur_data, pd.DataFrame)
