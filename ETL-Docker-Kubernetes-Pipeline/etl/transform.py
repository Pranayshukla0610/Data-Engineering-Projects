from logs.logger import logger

def transform_data(df):
    try:
        logger.info("Starting transformation")

        # Remove duplicates
        df = df.drop_duplicates()

        # Total sales column
        df['total_sales'] = df['quantity'] * df['price']

        # Uppercase customer names
        df['customer_name'] = df['customer_name'].str.upper()

        logger.info("Transformation completed")

        return df

    except Exception as e:
        logger.error(f"Transformation error: {e}")
        raise