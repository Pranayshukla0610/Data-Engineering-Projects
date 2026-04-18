def clean_data(df):
    df.drop_duplicates(inplace=True)
    return df

def feature_engineering(df):
    if 'Order Date' in df.columns:
        df['Order Date'] = pd.to_datetime(df['Order Date'])
        df['Year'] = df['Order Date'].dt.year
        df['Month'] = df['Order Date'].dt.month
    return df

def aggregate_data(df):
    if 'Sales' in df.columns:
        return df.groupby('Month')['Sales'].sum().reset_index()
    return df