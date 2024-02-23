PRIMARY_KEY_COLUMNS: list = [
    "BANCO",
    "CLIENTE",
    "COD"
]
SET_INDEX: bool = False

BANK_DIM_COLUMNS: list = [
    'bank_id',
    'bank_name'
]
BANK_DIM_TABLE_NAME: str = 'bank_dim'
NEW_BANK_DIM_COLUMNS: dict = {
    'BANCO': 'bank_name',
    'banco_id': 'bank_id'
}

CHECK_DIM_COLUMNS: list = [
    'check_id',
    'check_number',
    'check_amount',
    'maturity_date'
]
CHECK_DIM_TABLE_NAME: str = 'check_dim'
NEW_CHECK_DIM_COLUMNS: dict = {
    'Nº CHEQUE': 'check_number',
    'VALOR (R$)': 'check_amount',
    'VENCIMENTO': 'maturity_date'
}
CHECK_ID_LABELS: list = [
    'bank_name',
    'check_amount',
    'check_number',
    'name',
    'maturity_date'
]

DEST_DIM_COLUMNS: list = [
    'destination_id',
    'destination_type'
]
DEST_DIM_TABLE_NAME: str = 'dest_dim'
NEW_DEST_DIM_COLUMNS: dict = {
    'cod_id': 'destination_id',
    'COD': 'destination_type'
}

NAME_DIM_COLUMNS: list = [
    'client_name',
    'is_client',
    'name',
    'name_id'
]
NAME_DIM_TABLE_NAME: str = 'name_dim'
NEW_NAME_DIM_COLUMNS: dict = {
    'CLIENTE': 'name',
    'cliente_id': 'name_id'
}

NEW_EXIT_COLUMN: dict = {
    'SAÍDA': 'registration_date'
}

COLUMNS_TO_DROP: list = [
    'DESTINO',
    'OBSERVAÇÃO'
]

CHECK_FACT_COLUMNS: list = [
    'id',
    'name_id',
    'bank_id',
    'check_id',
    'destination_id',
    'is_in_cash',
    'description',
    'registration_date'
]
CHECK_FACT_TABLE_NAME: str = 'check_fact'
