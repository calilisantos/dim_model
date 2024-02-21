from dim_model.configs import accur_layer as accur_config
from functools import reduce
import pandas as pd
import numpy as np


class Transform:
    def __init__(self, raw_data):
        self._raw_data = raw_data
        self._accur_data = pd.DataFrame()

    def _drop_null_values(self):
        self._accur_data = (
            self._raw_data
            .dropna(
                subset=accur_config.COLUMNS_TO_DROP,
                how='any'
            )
        )

    def _drop_duplicated_columns(self):
        self._accur_data = (
            self._accur_data
            .drop_duplicates(
                subset=accur_config.DUPLICATED_COLUMNS_TO_DROP,
                keep='last'
            )
        )

    def _transform_bank_column(self):
        self._accur_data['BANCO'] = (
            self._accur_data['BANCO']
            .str.strip()
                .replace(accur_config.BANKS_ADJUST_DICT)
        )

    def _transform_cod_column(self):
        self._accur_data['COD'] = (
            self._accur_data['COD']
            .str.upper()
                .str.strip()
                    .replace(accur_config.COD_DICT)
                        .fillna(accur_config.DEFAULT_COD_VALUE)
        )

    def _transform_value_column(self):
        self._accur_data['VALOR (R$)'] = (
            self._accur_data['VALOR (R$)']
            .astype(str)
                .str.replace(',', '.')
                    .astype(float)
        )

    def _transform_date_columns(self):
        self._accur_data = reduce(
            lambda df, col: df.assign(
                **{
                    col: df[col].astype(str)
                    .replace(accur_config.DATES_TO_REPLACE_DICT, regex=True)
                }
            ),
            accur_config.DATE_COLUMNS_TO_LIST,
            self._accur_data
        )

    def _cast_date_columns(self):
        self._accur_data = reduce(
            lambda df, col: df.assign(
                **{
                    col: pd.to_datetime(
                        df[col],
                        format=accur_config.DATETIME_FORMAT
                    )
                }
            ),
            accur_config.DATE_COLUMNS_TO_LIST,
            self._accur_data
        )

    def _create_is_in_cash_column(self):
        checks_out = (
            self._accur_data[self._accur_data['SAÍDA'].notnull()]
            [accur_config.COMMON_COLUMNS_LIST]
        )

        self._accur_data['is_in_cash'] = np.where(
            self._accur_data['CLIENTE'].isin(checks_out['CLIENTE']) &
            self._accur_data['BANCO'].isin(checks_out['BANCO']) &
            self._accur_data['Nº CHEQUE'].isin(checks_out['Nº CHEQUE']) &
            self._accur_data['VALOR (R$)'].isin(checks_out['VALOR (R$)']),
            False,
            True
        )

    def transform_data(self):
        self._drop_null_values()
        self._drop_duplicated_columns()
        self._transform_bank_column()
        self._transform_cod_column()
        self._transform_value_column()
        self._transform_date_columns()
        self._cast_date_columns()
        self._create_is_in_cash_column()
        return self._accur_data
