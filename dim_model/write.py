from dim_model.configs import database as db_config


class Write:
    def __init__(self, df, table_name, set_index):
        self._df = df
        self._table_name = table_name
        self._set_index = set_index

    def write_data(self):
        self._df.to_sql(
            self._table_name,
            con=db_config.ENGINE,
            if_exists=db_config.WRITE_MODE,
            index=self._set_index
        )
