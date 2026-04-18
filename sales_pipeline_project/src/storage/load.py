from sqlalchemy import create_engine
import os

def load_to_db(df, table_name):
    db_url = os.getenv("DB_URI")
    engine = create_engine(db_url)

    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"{table_name} loaded to DB")