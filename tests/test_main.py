from dim_model.main import Main
from unittest import TestCase
from unittest.mock import patch


class TestMain(TestCase):
    def setUp(self):
        self._main = Main()

    @patch('dim_model.main.Main.run_pipeline')
    def test_run_pipeline__has_called(self, mock_run_pipeline):
        self._main.run_pipeline()
        self.assertTrue(mock_run_pipeline.called)
        self.assertTrue(self._main._orchestrator.run)
