import pandas as pd
import os

RAW_PATH = 'data/raw/stores_sales_forecasting.csv'
PROCESSED_PATH = 'data/processed/clean_inventory.csv'


def clean_inventory_data():
    df = pd.read_csv(RAW_PATH,encoding='latin1')

    print('Original Shape:', df.shape)

    df.drop_duplicates(inplace=True)

    df.columns = [col.lower().replace(' ', '_') for col in df.columns]

    df.fillna(0, inplace=True)

    if 'inventory_level' in df.columns:
        df['inventory_level'] = df['inventory_level'].astype(int)

    if 'sales_last_month' in df.columns:
        df['sales_last_month'] = df['sales_last_month'].astype(float)

    if 'inventory_level' in df.columns:
        df['stock_status'] = df['inventory_level'].apply(
            lambda x: 'LOW' if x < 20 else 'AVAILABLE'
        )

    os.makedirs('data/processed', exist_ok=True)

    df.to_csv(PROCESSED_PATH, index=False)

    print('Cleaned Shape:', df.shape)
    print('Processed file saved successfully')

if __name__ == '__main__':
    clean_inventory_data()