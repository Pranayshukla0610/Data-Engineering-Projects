import pandas as pd
from logs.logger import logger

def extract_data():
    try:
        logger.info("Starting data extraction")
        df = pd.read_csv('data/raw/sales_data.csv')
        logger.info('Data Extracted Successfully')
        return df
    except Exception as e:
        logger.error(f"Error in Extraction: {e}")
        raise