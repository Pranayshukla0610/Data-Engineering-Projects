import pandas as pd
from etl.transform import transform_data

def test_total_sales():

    data = {
        'quantity': [2],
        'price': [100]
    }

    df = pd.DataFrame(data)

    transformed = transform_data(df)

    assert transformed['total_sales'][0] == 200