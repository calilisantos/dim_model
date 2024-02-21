ACCUR_TABLE_NAME: str = 'accur_data'
BANKS_ADJUST_DICT: dict = {
    'BB': 'BANCO DO BRASIL',
    'BD': 'BRADESCO',
    'BNB': 'BANCO DO NORDESTE',
    'BS': 'BRADESCO',
    'itau': 'ITAU',
    'SICOB': 'SICOOB',
    'SICRED': 'SICREDI',
    'SICREDII': 'SICREDI'
}
COD_DICT: dict = {
    'D': 'DEPOSITO',
    'O': 'OUTROS',
    'P': 'PAGAMENTO',
    'T': 'CAIXA'
}
DEFAULT_COD_VALUE: str = 'CAIXA'
COLUMNS_TO_DROP: list = [
    'BANCO',
    'CLIENTE'
]
COMMON_COLUMNS_LIST: list = [
    'BANCO',
    'CLIENTE',
    'Nº CHEQUE',
    'VALOR (R$)'
]
DATE_COLUMNS_TO_LIST: list = [
    'SAÍDA',
    'VENCIMENTO'
]
DATETIME_FORMAT: str = 'mixed'
DATES_TO_REPLACE_DICT: dict = {
    r'\s+': '',
    '00:00:00': '',
    '2216': '2016',
    '29/2/2017': '2017-02-28',
    '29/2/2018': '2018-02-28',
    '29/2/2019': '2019-02-28',
    '31/4/2017': '2017-04-30',
    '31/4/2018': '2018-04-30',
    '30/62017': '2017-06-30',
    '31/9/2017': '2017-09-30',
    '2017-09-31': '2017-09-30',
    '31/6/2018': '2018-06-30',
    '31/9/2018': '2018-09-30',
    ',15/04/2016': '2016-04-15',
    '15/04/2016': '2016-04-15',
    '15/04/201': '2016-04-15',
    '10/06/2016': '2016-06-10',
    '31/11': '30/11',
    '216': '2016',
    # '22016': '2016',
    # '22016-10-07': '2016-10-07',
    '217': '2017',
    '218': '2018',
    '219': '2019',
    '221': '2021',
    '10/112017': '2017-11-10',
    '227/9/2018': '2018-09-27'
}
DUPLICATED_COLUMNS_TO_DROP: list = [
    'BANCO',
    'CLIENTE',
    'Nº CHEQUE',
    'SAÍDA'
]
SET_INDEX: bool = True
