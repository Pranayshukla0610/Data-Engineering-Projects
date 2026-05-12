def validate_data(df):

    if df.isnull().sum().sum() > 0:
        raise Exception("Null values found")

    if df.empty:
        raise Exception("Dataframe is empty")

    return True