import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

print("DATABASE_URL =", DATABASE_URL)

engine = create_engine(DATABASE_URL)



def load_inventory_data():
    df = pd.read_csv('data/processed/clean_inventory.csv')

    df.to_sql(
        'inventory',
        engine,
        if_exists='replace',
        index=False
    )

    print('Data loaded into PostgreSQL successfully')


if __name__ == '__main__':
    load_inventory_data()