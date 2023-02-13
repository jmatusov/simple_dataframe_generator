import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import warnings
import random
import re


def type_validator(types: list):
    """
    All input parameters must be of correct type. Column name is tested separately.
    """
    if any(x is False for x in types):
        raise TypeError('Incorrect type of input parameters.')


def col_name_validator(col_name):
    """
    Column name must be a non-empty string.
    """
    if col_name is None or not isinstance(col_name, str) or len(col_name) == 0:
        raise ValueError(f'Parameter col_name with value "{col_name}" is invalid. Use non-empty string.')


def col_name_warning(col_name: str, columns):
    """
    Warn if column with given name exists.
    """
    if col_name in columns:
        warnings.warn(f'Column with name "{col_name}" already in use. Overwriting.')


def none_ratio_validator(allow_none: bool, none_ratio: int):
    """
    Value must be between 0 and 100.
    """
    if allow_none and 0 > none_ratio > 100:
        raise ValueError('Value of none_ratio not in range 0-100.')


def cat_validator(categories: list):
    """
    At least 1 category must be provided.
    """
    if len(categories) == 0:
        raise ValueError('No categories provided.')


def date_validator(start_date: str, end_date: str):
    """
    Checks if provided dates are in YYYY-MM-DD format.
    Does not check if value is valid (eg. 2023-50-50 will pass the check).
    """
    if not (re.match(r'^\d{4}-[01][1-9]-\d{2}$', start_date) and re.match(r'^\d{4}-\d{2}-\d{2}$', end_date)):
        raise ValueError('Incorrect date format.')


def get_rand_int(min_val: int, max_val: int) -> int:
    """
    Returns random integer.
    """
    return np.random.randint(min_val, max_val + 1)


def get_rand_float(min_val: float, max_val: float) -> float:
    """
    Returns random float.
    """
    return np.random.uniform(min_val, max_val)


def get_rand_cat(categories: list):
    """
    Returns random category.
    """
    return random.choice(categories)


def get_rand_date(min_date: datetime, max_date: datetime):
    """
    Returns random datetime between start and end date.
    """
    min_timestamp = int(min_date.timestamp())
    max_timestamp = int((max_date + timedelta(days=1)).timestamp())
    random_timestamp = random.randint(min_timestamp, max_timestamp)

    return datetime.fromtimestamp(random_timestamp)


def prob_eval(max_prob: int):
    """
    Returns True or False with probability of max_prob [%].
    """
    return np.random.randint(0, 100) >= max_prob


class SDG:
    def __init__(self):
        """
        Simple dataframe generator.

        Define columns with add_int_col(), add_float_col(), add_categorical_col() or add_datetime_col().

        Generate pandas DataFrame using generate_dataframe().
        """
        self.columns = {}

    def add_int_col(self, col_name: str, min_val: int = 0, max_val: int = 100,
                    allow_none: bool = False, none_prob: int = 10):
        """
        Adds integer column with specified parameters.
        Performs basic parameter validation.

        :param col_name: Column name to be used in DataFrame. Use non-empty string.
        :param min_val: Minimum value in column.
        :param max_val: Maximum value in column.
        :param allow_none: Column may contain None values if True.
        :param none_prob: Probablity of None values in column. Int range 0-100.
        """
        type_validator([isinstance(min_val, int), isinstance(max_val, int),
                        isinstance(allow_none, bool), isinstance(none_prob, int)])
        col_name_validator(col_name)
        col_name_warning(col_name, self.columns.keys())
        none_ratio_validator(allow_none, none_prob)

        self.columns[col_name] = {'col_type': 'Int64', 'min_val': min_val, 'max_val': max_val,
                                  'allow_none': allow_none, 'none_prob': none_prob}

    def add_float_col(self, col_name: str, min_val: float = 0.0, max_val: float = 100.0,
                      allow_none: bool = False, none_prob: int = 10):
        """
        Adds float column with specified parameters.
        Performs basic parameter validation.

        :param col_name: Column name to be used in DataFrame. Use non-empty string.
        :param min_val: Minimum value in column.
        :param max_val: Maximum value in column.
        :param allow_none: Column may contain None values if True.
        :param none_prob: Probablity of None values in column. Int range 0-100.
        """
        type_validator([isinstance(min_val, float), isinstance(max_val, float),
                        isinstance(allow_none, bool), isinstance(none_prob, int)])
        col_name_validator(col_name)
        col_name_warning(col_name, self.columns.keys())
        none_ratio_validator(allow_none, none_prob)

        self.columns[col_name] = {'col_type': 'Float64', 'min_val': min_val, 'max_val': max_val,
                                  'allow_none': allow_none, 'none_prob': none_prob}

    def add_cat_col(self, col_name: str, categories: list, allow_none: bool = False, none_prob: int = 10):
        """
        Adds categorical column with specified parameters.
        Performs basic parameter validation.

        :param col_name: Column name to be used in DataFrame. Use non-empty string.
        :param categories: List of categories to choose from.
        :param allow_none: Column may contain None values if True.
        :param none_prob: Probablity of None values in column. Int range 0-100.
        """
        type_validator([isinstance(categories, list), isinstance(allow_none, bool), isinstance(none_prob, int)])
        col_name_validator(col_name)
        col_name_warning(col_name, self.columns.keys())
        none_ratio_validator(allow_none, none_prob)
        cat_validator(categories)

        self.columns[col_name] = {'col_type': 'object', 'categories': categories,
                                  'allow_none': allow_none, 'none_prob': none_prob}

    def add_datetime_col(self, col_name: str, min_date: str = '2000-01-01', max_date: str = '2023-12-31',
                         allow_none: bool = False, none_prob: int = 10):
        """
        Adds datetime column with specified parameters.
        Performs basic parameter validation.

        :param col_name: Column name to be used in DataFrame. Use non-empty string.
        :param min_date: Start date in YYYY-MM-DD format.
        :param max_date: End date in YYYY-MM-DD format.
        :param allow_none: Column may contain None values if True.
        :param none_prob: Probablity of None values in column. Int range 0-100.

        """
        type_validator([isinstance(min_date, str), isinstance(max_date, str),
                        isinstance(allow_none, bool), isinstance(none_prob, int)])
        col_name_validator(col_name)
        col_name_warning(col_name, self.columns.keys())
        none_ratio_validator(allow_none, none_prob)
        date_validator(min_date, max_date)

        min_date = datetime.strptime(min_date, '%Y-%m-%d')
        max_date = datetime.strptime(max_date, '%Y-%m-%d')

        self.columns[col_name] = {'col_type': 'datetime64', 'start_date': min_date, 'end_date': max_date,
                                  'allow_none': allow_none, 'none_prob': none_prob}

    def generate_dataframe(self, rows: int = 100) -> pd.DataFrame:
        """
        Generates pandas DataFrame with specified number rows.

        :param rows: Number of rows to generate.
        """
        if len(self.columns) == 0:
            raise ValueError('No columns defined.')

        df_data = {}
        d_types = {}

        for c, v in self.columns.items():  # c - col_name, v - values
            if v['allow_none'] and v['none_prob'] > 0:
                max_prob = v['none_prob']
            else:
                max_prob = 0

            if v['col_type'] == 'Int64':
                rand_values = [get_rand_int(v['min_val'], v['max_val']) if prob_eval(max_prob)
                               else pd.NA
                               for _ in range(rows)]
            elif v['col_type'] == 'Float64':
                rand_values = [get_rand_float(v['min_val'], v['max_val']) if prob_eval(max_prob)
                               else pd.NA
                               for _ in range(rows)]
            elif v['col_type'] == 'object':
                rand_values = [get_rand_cat(v['categories']) if prob_eval(max_prob)
                               else pd.NA
                               for _ in range(rows)]
            else:
                rand_values = [get_rand_date(v['start_date'], v['end_date']) if prob_eval(max_prob)
                               else pd.NA
                               for _ in range(rows)]

            d_types[c] = v['col_type']
            df_data[c] = rand_values

        df = pd.DataFrame(df_data)
        df = df.astype(d_types)

        return df
