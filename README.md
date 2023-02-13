# simple_dataframe_generator
___

**_Personal project to generate pandas DataFrame quick and easy._**

## Installation

```
pip install simple-dataframe-generator==1.0.2
```

## Supported column types

1. Integer - ```add_int_col()```
2. Float - ```add_float_col()```
3. Categorical - ```add_cat_col()```
4. Datetime - ```add_datetime_col()```

All column types support ```allow_none```.


## Usage

```python
import pandas as pd
import numpy as np
from simple_dataframe_generator import simple_dataframe_generator


sdg = simple_dataframe_generator.SDG()

# add integer column with specified parameters
sdg.add_int_col(col_name='age', min_val=0, max_val=99)

# add integer column with specified parameters, allow missing values
sdg.add_int_col(col_name='favorite_number', min_val=-100, max_val=100, allow_none=True, none_prob=10)

# add float column with specified parameters
sdg.add_float_col('distance', min_val=0.0, max_val=200.0)

# add categorical column with pre-defined categories
categories = ['New York', 'Chicago', 'Los Angeles']
sdg.add_cat_col('city', categories=categories, allow_none=True)

# add datetime column
sdg.add_datetime_col('last_seen', min_date='2020-01-01', max_date='2023-02-01')

# generate pandas DataFrame with specific row count
df = sdg.generate_dataframe(rows=10)
```

## Result

|     | age | favorite_number | distance | city        | last_seen           |
|----:|----:|:----------------|---------:|:------------|:--------------------|
|   0 |  69 | 81              |  184.517 | Chicago     | 2022-08-12 10:39:59 |
|   1 |  73 | 1               |  118.874 | Chicago     | 2021-01-06 11:57:22 |
|   2 |  10 | 33              |  199.226 | New York    | 2020-05-29 10:37:36 |
|   3 |  47 | -36             |  194.205 | Chicago     | 2022-05-30 21:26:24 |
|   4 |  25 | -66             |  24.9345 | \<NA>       | 2021-03-26 03:19:09 |
|   5 |  36 | -12             |  21.0734 | New York    | 2021-01-19 03:22:27 |
|   6 |  21 | \<NA>           |  165.243 | Chicago     | 2022-01-24 04:20:39 |
|   7 |  37 | \<NA>           |  3.48131 | Chicago     | 2020-05-30 18:37:24 |
|   8 |  61 | -77             |  90.0552 | New York    | 2021-01-07 14:43:35 |
|   9 |  21 | -19             |    173.3 | Los Angeles | 2020-01-01 00:53:00 |

## Author
- [jmatusov](https://github.com/jmatusov)