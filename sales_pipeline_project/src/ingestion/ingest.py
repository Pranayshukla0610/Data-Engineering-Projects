import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path, encoding='latin1')
    print("Data Loaded Successfully")
    return df