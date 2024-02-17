from dim_model.model import Model
import pandas as pd
from unittest import TestCase
from unittest.mock import patch, Mock


class TestModel(TestCase):
    def setUp(self):
        mock_df = Mock(spec=pd.DataFrame)
        self.model = Model(mock_df)

    @patch(
        'dim_model.model.Model._set_primary_key',
        return_value=Mock(spec=pd.DataFrame)
    )
    def test_set_primary_key__return(self, mock_set_primary_key):
        self.model._set_primary_key()
        self.assertIsInstance(self.model._model_data, pd.DataFrame)

    @patch(
        'dim_model.model.Model._create_is_client_column',
        return_value=Mock(spec=pd.DataFrame)
    )
    def test_create_is_client_column__return(self, mock_create_is_client_column):
        self.model._create_is_client_column()
        self.assertIsInstance(self.model._model_data, pd.DataFrame)

    @patch(
        'dim_model.model.Model._rename_name_dim_columns',
        return_value=Mock(spec=pd.DataFrame)
    )
    def test_rename_name_dim_columns__return(self, mock_rename_name_dim_columns):
        self.model._rename_name_dim_columns()
        self.assertIsInstance(self.model._model_data, pd.DataFrame)
    
    @patch(
        'dim_model.model.Model._create_client_name_column',
        return_value=Mock(spec=pd.DataFrame)
    )
    def test_create_client_name_column__return(self, mock_create_client_name_column):
        self.model._create_client_name_column()
        self.assertIsInstance(self.model._model_data, pd.DataFrame)
    
    @patch(
        'dim_model.model.Model._rename_bank_dim_columns',
        return_value=Mock(spec=pd.DataFrame)
    )
    def test_rename_bank_dim_columns__return(self, mock_rename_bank_dim_columns):
        self.model._rename_bank_dim_columns()
        self.assertIsInstance(self.model._model_data, pd.DataFrame)
    
    @patch(
        'dim_model.model.Model._rename_check_dim_columns',
        return_value=Mock(spec=pd.DataFrame)
    )
    def test_rename_check_dim_columns__return(self, mock_rename_check_dim_columns):
        self.model._rename_check_dim_columns()
        self.assertIsInstance(self.model._model_data, pd.DataFrame)

    @patch(
        'dim_model.model.Model._create_check_id_column',
        return_value=Mock(spec=pd.DataFrame)
    )
    def test_create_check_id_column__return(self, mock_create_check_id_column):
        self.model._create_check_id_column()
        self.assertIsInstance(self.model._model_data, pd.DataFrame)

    @patch(
        'dim_model.model.Model._rename_dest_dim_columns',
        return_value=Mock(spec=pd.DataFrame)
    )
    def test_rename_dest_dim_columns__return(self, mock_rename_dest_dim_columns):
        self.model._rename_dest_dim_columns()
        self.assertIsInstance(self.model._model_data, pd.DataFrame)

    @patch(
        'dim_model.model.Model._transform_exit_column',
        return_value=Mock(spec=pd.DataFrame)
    )
    def test_transform_exit_column__return(self, mock_transform_exit_column):
        self.model._transform_exit_column()
        self.assertIsInstance(self.model._model_data, pd.DataFrame)

    @patch(
        'dim_model.model.Model._rename_exit_column',
        return_value=Mock(spec=pd.DataFrame)
    )
    def test_rename_exit_column__return(self, mock_rename_exit_column):
        self.model._rename_exit_column()
        self.assertIsInstance(self.model._model_data, pd.DataFrame)

    @patch(
        'dim_model.model.Model._create_description_column',
        return_value=Mock(spec=pd.DataFrame)
    )
    def test_create_description_column__return(self, mock_create_description_column):
        self.model._create_description_column()
        self.assertIsInstance(self.model._model_data, pd.DataFrame)

    @patch(
        'dim_model.model.Model._drop_columns',
        return_value=Mock(spec=pd.DataFrame)
    )
    def test_drop_columns__return(self, mock_drop_columns):
        self.model._drop_columns()
        self.assertIsInstance(self.model._model_data, pd.DataFrame)

    @patch(
        'dim_model.model.Model._create_id_column',
        return_value=Mock(spec=pd.DataFrame)
    )
    def test_create_id_column__return(self, mock_create_id_column):
        self.model._create_id_column()
        self.assertIsInstance(self.model._model_data, pd.DataFrame)

    @patch(
        'dim_model.model.Model.create_model',
        return_value=Mock(spec=pd.DataFrame)
    )
    def test_create_model__return(self, mock_create_model):
        self.model.create_model()
        self.assertIsInstance(self.model._model_data, pd.DataFrame)
