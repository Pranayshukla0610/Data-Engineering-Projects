from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

def run_pipeline():
    df = extract_data()

    transformed_df = transform_data(df)

    transformed_df.to_csv(
        'data/processed/processed_sales_data.csv',
        index=False
    )

    load_data(transformed_df)

    transformed_df.to_csv(
        'data/exports/final_export.csv',
        index=False
    )

    print("ETL Pipeline Completed Successfully")

if __name__ == "__main__":
    run_pipeline()