import sys

from simple_dataframe_generator import SDG
import numpy as np
sdg = SDG()

# add integer column with specified parameters
sdg.add_int_col(col_name='age', min_val=0, max_val=99)

# add integer column with specified parameters, allow missing values
sdg.add_int_col(col_name='favorite_number', min_val=-100, max_val=100, allow_none=True, none_proba=10)

# add float column with specified parameters
sdg.add_float_col('distance', min_val=0.0, max_val=200.0)

# add categorical column with pre-defined categories
categories = ['New York', 'Chicago', 'Los Angeles']
sdg.add_cat_col('city', categories=categories, allow_none=True)

# add datetime column
sdg.add_datetime_col('last_seen', min_date='2020-01-01', max_date='2023-02-01')

# generate pandas DataFrame with specific row count
df = sdg.generate_dataframe(rows=10)
print(df.to_markdown())
pass
