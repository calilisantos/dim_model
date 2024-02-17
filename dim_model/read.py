from dim_model.configs import read as read_config
import pandas as pd


class Read:
    def __init__(self):
        self._months_list = read_config.MONTHS_LIST
        self._first_year = read_config.FIRST_YEAR
        self._last_year = read_config.LAST_YEAR
        self._data = list()
        self._dataframe = pd.DataFrame

    def _set_data(self):
        for year in range(self._first_year, self._last_year + 1):
            arquivo_excel = f"dim_model/sheets/CONTROLE CHEQUE {year}.xlsx"
            for month in self._months_list:
                try:
                    df = pd.read_excel(arquivo_excel, sheet_name=month)
                    self._data.append(df)
                except Exception as e:
                    print(f'Erro ao ler a planilha {month} de {year}:\n{str(e)}')

    def _set_dataframe(self):
        self._dataframe = pd.concat(
            self._data,
            ignore_index=read_config.IGNORE_INDEX
        )

    def read_data(self):
        self._set_data()
        self._set_dataframe()
        return self._dataframe
