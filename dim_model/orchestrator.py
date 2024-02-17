from dim_model.configs import (
    database as db_config,
    raw_layer as raw_config,
    accur_layer as accur_config,
    model_layer as model_config,
    logs as logs_config
)
from dim_model.model import Model
from dim_model.read import Read
from dim_model.transform import Transform
from dim_model.write import Write
import logging
import pandas as pd
from sqlalchemy_utils.functions import create_database, database_exists


class Orchestrator:
    def __init__(self):
        self._raw_dataframe = pd.DataFrame()
        self._raw_data = pd.DataFrame()
        self._accur_data = pd.DataFrame()
        self._model_data = pd.DataFrame()
        self._write = Write
        self._logger = logging.getLogger(__name__)
        self._configure_logger()

    def _configure_logger(self):
        logging.basicConfig(
            format=logs_config.LOG_FORMAT,
            datefmt=logs_config.LOG_DATE_FORMAT,
            style=logs_config.LOG_STYLE,
            level=logging.INFO
        )

    def create_database(self):
        if not database_exists(db_config.CONNECTION_STRING):
            create_database(db_config.CONNECTION_STRING)

    def set_raw_dataframe(self):
        self._raw_dataframe = Read().read_data()

    def write_raw_data(self):
        self._raw_data = (
            self._raw_dataframe[raw_config.RAW_COLUMNS_LIST]
                .dropna(thresh=raw_config.REQUIRED_COLUMNS)
        )
        self._write(
            self._raw_data,
            raw_config.RAW_TABLE_NAME,
            raw_config.SET_INDEX
        ).write_data()

    def write_accur_data(self):
        self._accur_data = Transform(self._raw_data).transform_data()
        self._write(
            self._accur_data,
            accur_config.ACCUR_TABLE_NAME,
            accur_config.SET_INDEX
        ).write_data()

    def set_model_data(self):
        self._model_data = Model(self._accur_data).create_model()

    def write_bank_dim(self):
        self._write(
            self._model_data[model_config.BANK_DIM_COLUMNS].drop_duplicates(),
            model_config.BANK_DIM_TABLE_NAME,
            model_config.SET_INDEX
        ).write_data()

    def write_check_dim(self):
        self._write(
            self._model_data[model_config.CHECK_DIM_COLUMNS].drop_duplicates(),
            model_config.CHECK_DIM_TABLE_NAME,
            model_config.SET_INDEX
        ).write_data()

    def write_dest_dim(self):
        self._write(
            self._model_data[model_config.DEST_DIM_COLUMNS].drop_duplicates(),
            model_config.DEST_DIM_TABLE_NAME,
            model_config.SET_INDEX
        ).write_data()

    def write_name_dim(self):
        self._write(
            self._model_data[model_config.NAME_DIM_COLUMNS].drop_duplicates(),
            model_config.NAME_DIM_TABLE_NAME,
            model_config.SET_INDEX
        ).write_data()

    def write_check_fact(self):
        self._write(
            self._model_data[model_config.CHECK_FACT_COLUMNS],
            model_config.CHECK_FACT_TABLE_NAME,
            model_config.SET_INDEX
        ).write_data()

    def run(self):
        self._logger.info("Starting the data pipeline")
        self._logger.info("Creating database if not exists")
        try:
            self.create_database()
            self._logger.info("Database has been created or already exists")
        except Exception as error:
            raise error(
                self._logger.error(f"Error while creating database: {error}")
            )
        self._logger.info("Reading raw data")
        try:
            self.set_raw_dataframe()
            self._logger.info("Raw data has been read")
        except Exception as error:
            raise error(
                self._logger.error(f"Error while reading raw data: {error}")
            )
        self._logger.info("Writing raw data")
        try:
            self.write_raw_data()
            self._logger.info("Raw data has been written")
        except Exception as error:
            raise error(
                self._logger.error(f"Error while writing raw data: {error}")
            )
        self._logger.info("Writing accurate data")
        try:
            self.write_accur_data()
            self._logger.info("Accurate data has been written")
        except Exception as error:
            raise error(
                self._logger.error(
                    f"Error while writing accurate data: {error}"
                )
            )
        self._logger.info("Setting model data")
        try:
            self.set_model_data()
            self._logger.info("Model data has been set")
        except Exception as error:
            raise error(
                self._logger.error(f"Error while setting model data: {error}")
            )
        self._logger.info("Writing bank dim")
        try:
            self.write_bank_dim()
            self._logger.info("Bank dim has been written")
        except Exception as error:
            raise error(
                self._logger.error(f"Error while writing bank dim: {error}")
            )
        self._logger.info("Writing check dim")
        try:
            self.write_check_dim()
            self._logger.info("Check dim has been written")
        except Exception as error:
            raise error(
                self._logger.error(f"Error while writing check dim: {error}")
            )
        self._logger.info("Writing dest dim")
        try:
            self.write_dest_dim()
            self._logger.info("Dest dim has been written")
        except Exception as error:
            raise error(
                self._logger.error(f"Error while writing dest dim: {error}")
            )
        self._logger.info("Writing name dim")
        try:
            self.write_name_dim()
            self._logger.info("Name dim has been written")
        except Exception as error:
            raise error(
                self._logger.error(f"Error while writing name dim: {error}")
            )
        self._logger.info("Writing fact table")
        try:
            self.write_check_fact()
            self._logger.info("Fact table has been written")
        except Exception as error:
            raise error(
                self._logger.error(f"Error while writing fact table: {error}")
            )
        self._logger.info("Data pipeline has finished")
