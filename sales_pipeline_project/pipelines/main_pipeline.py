import os
from src.ingestion.ingest import load_data
from src.processing.transform import clean_data, feature_engineering, aggregate_data
from src.storage.load import load_to_db

def run_pipeline():
    file_path = "data/raw/sales_data.csv"

    df = load_data(file_path)
    df = clean_data(df)
    df = feature_engineering(df)

    summary = aggregate_data(df)

    load_to_db(df, "sales_cleaned")
    load_to_db(summary, "sales_summary")

    print("Pipeline Completed")

if __name__ == "__main__":
    run_pipeline()