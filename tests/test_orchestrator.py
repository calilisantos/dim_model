from dim_model.orchestrator import Orchestrator
from dim_model.write import Write
import pandas as pd
from unittest import TestCase
from unittest.mock import patch, Mock


class TestOrchestrator(TestCase):
    def setUp(self):
        self._orchestrator = Orchestrator()

    @patch(
        'dim_model.orchestrator.Orchestrator._configure_logger',
        return_value=Mock()
    )
    def test_configure_logger__return(self, mock_configure_logger):
        self._orchestrator._configure_logger()
        self.assertTrue(hasattr(self._orchestrator, '_logger'))

    @patch(
        'dim_model.orchestrator.Orchestrator.create_database',
        return_value=Mock()
    )
    def test_create_database__has_called(self, mock_create_database):
        self._orchestrator.create_database()
        self.assertTrue(mock_create_database.called)

    @patch(
        'dim_model.orchestrator.Orchestrator.set_raw_dataframe',
        return_value=Mock(spec=pd.DataFrame)
    )
    def test_set_raw_dataframe__return(self, mock_set_raw_dataframe):
        self._orchestrator.set_raw_dataframe()
        self.assertIsInstance(self._orchestrator._raw_dataframe, pd.DataFrame)

    @patch(
        'dim_model.orchestrator.Orchestrator.write_raw_data',
        return_value=Mock()
    )
    def test_write_raw_data_calls_write_data(self, mock_write_raw_data):
        self._orchestrator.write_raw_data()
        self.assertTrue(self._orchestrator._write.write_data)

    @patch(
        'dim_model.orchestrator.Orchestrator.write_accur_data',
        return_value=Mock()
    )
    def test_write_accur_data_calls_write_data(self, mock_write_accur_data):
        self._orchestrator.write_accur_data()
        self.assertTrue(self._orchestrator._write.write_data)

    @patch(
        'dim_model.orchestrator.Orchestrator.set_model_data',
        return_value=Mock(spec=pd.DataFrame)
    )
    def test_set_model_data__return(self, mock_set_model_data):
        self._orchestrator.set_model_data()
        self.assertIsInstance(self._orchestrator._model_data, pd.DataFrame)

    @patch(
        'dim_model.orchestrator.Orchestrator.write_bank_dim',
        return_value=Mock()
    )
    def test_write_bank_dim_calls_write_data(self, mock_write_bank_dim):
        self._orchestrator.write_bank_dim()
        self.assertTrue(self._orchestrator._write.write_data)

    @patch(
        'dim_model.orchestrator.Orchestrator.write_check_dim',
        return_value=Mock()
    )
    def test_write_check_dim_calls_write_data(self, mock_write_check_dim):
        self._orchestrator.write_check_dim()
        self.assertTrue(self._orchestrator._write.write_data)

    @patch(
        'dim_model.orchestrator.Orchestrator.write_dest_dim',
        return_value=Mock()
    )
    def test_write_dest_dim_calls_write_data(self, mock_write_dest_dim):
        self._orchestrator.write_dest_dim()
        self.assertTrue(self._orchestrator._write.write_data)

    @patch(
        'dim_model.orchestrator.Orchestrator.write_name_dim',
        return_value=Mock()
    )
    def test_write_name_dim_calls_write_data(self, mock_write_name_dim):
        self._orchestrator.write_name_dim()
        self.assertTrue(self._orchestrator._write.write_data)

    @patch(
        'dim_model.orchestrator.Orchestrator.write_check_fact',
        return_value=Mock()
    )
    def test_write_check_fact_calls_write_data(self, mock_write_check_fact):
        self._orchestrator.write_check_fact()
        self.assertTrue(self._orchestrator._write.write_data)

    @patch(
        'dim_model.orchestrator.Orchestrator.run',
        return_value=Mock()
    )
    def test_run_calls__with_success(self, mock_run):
        self._orchestrator.run()
        self.assertTrue(self._orchestrator._logger.info)

    @patch(
        'dim_model.orchestrator.Orchestrator.run',
        side_effect=Exception
    )
    def test_run_calls__with_exception(self, mock_run):
        with self.assertRaises(Exception):
            self._orchestrator.run()
        self.assertTrue(self._orchestrator._logger.error)
