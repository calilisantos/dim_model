from dotenv import load_dotenv
from os import getenv
from sqlalchemy import create_engine

load_dotenv()

DB_HOST: str = getenv('DB_HOST')
DB_NAME: str = getenv('DB_NAME')
DB_PASSWORD: str = getenv('DB_PASSWORD')
DB_USER: str = getenv('DB_USER')
CONNECTION_STRING: str = f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
ENGINE: str = create_engine(CONNECTION_STRING)
WRITE_MODE: str = 'replace'
