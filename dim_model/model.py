from dim_model.configs import model_layer as model_config
from functools import reduce
import pandas as pd
import numpy as np


class Model:
    def __init__(self, accur_data):
        self._accur_data = accur_data
        self._model_data = pd.DataFrame()

    def _set_primary_key(self):
        self._model_data = reduce(
            lambda df, col: df.assign(
                **{
                    f'{col.lower()}_id':
                        df[col].astype('category').cat.codes + 1
                }
            ),
            model_config.PRIMARY_KEY_COLUMNS,
            self._accur_data
        )

    def _create_is_client_column(self):
        self._model_data['is_client'] = np.where(
            self._model_data['OBSERVAÇÃO'].isnull() |
            self._model_data['CLIENTE'].isin(self._model_data['OBSERVAÇÃO']),
            True,
            False
        )

    def _rename_name_dim_columns(self):
        self._model_data = self._model_data.rename(
            columns=model_config.NEW_NAME_DIM_COLUMNS
        )

    def _create_client_name_column(self):
        self._model_data['client_name'] = np.where(
            self._model_data['is_client'] is True,
            self._model_data['name'],
            np.where(
                self._model_data['OBSERVAÇÃO'].isin(self._model_data['name']) &
                self._model_data['is_client'] is False,
                self._model_data['OBSERVAÇÃO'],
                ''
            )
        )

    def _rename_bank_dim_columns(self):
        self._model_data = self._model_data.rename(
            columns=model_config.NEW_BANK_DIM_COLUMNS
        )

    def _rename_check_dim_columns(self):
        self._model_data = self._model_data.rename(
            columns=model_config.NEW_CHECK_DIM_COLUMNS
        )

    def _create_check_id_column(self):
        self._model_data['check_id'] = (
            self._model_data
            .groupby(model_config.CHECK_ID_LABELS)
                .ngroup() + 1
        )

    def _rename_dest_dim_columns(self):
        self._model_data = self._model_data.rename(
            columns=model_config.NEW_DEST_DIM_COLUMNS
        )

    def _transform_exit_column(self):
        self._model_data['SAÍDA'] = np.where(
            self._model_data['SAÍDA'].isnull(),
            self._model_data['maturity_date'],
            self._model_data['SAÍDA']
        )

    def _rename_exit_column(self):
        self._model_data = self._model_data.rename(
            columns=model_config.NEW_EXIT_COLUMN
        )

    def _create_description_column(self):
        self._model_data['description'] = self._model_data['DESTINO']

    def _drop_columns(self):
        self._model_data = self._model_data.drop(
            columns=model_config.COLUMNS_TO_DROP
        )

    def _create_id_column(self):
        self._model_data['id'] = self._model_data.index + 1

    def create_model(self):
        self._set_primary_key()
        self._create_is_client_column()
        self._rename_name_dim_columns()
        self._create_client_name_column()
        self._rename_bank_dim_columns()
        self._rename_check_dim_columns()
        self._create_check_id_column()
        self._rename_dest_dim_columns()
        self._transform_exit_column()
        self._rename_exit_column()
        self._create_description_column()
        self._drop_columns()
        self._create_id_column()
        return self._model_data
