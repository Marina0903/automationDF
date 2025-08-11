from typing import Tuple

import pandas as pd
import numpy as np


class automation:
  """
  A small helper class for quick pandas DataFrame checks and cleanup.
  """
  def __init__(self, df: pd.DataFrame):
   """
    Keep a DataFrame inside the class.

    :param df: pandas DataFrame to work with
    """
   self.df = df

  def get_shape(self) -> Tuple[int, int]:
    """
    Get number of rows and columns.

    :return: (rows, columns)
    """
    return self.df.shape

  def get_head(self) -> pd.DataFrame:
    """
    Show the first 5 rows.
    :return: DataFrame with first rows
    """
    return self.df.head()

  def get_info(self) -> None:
    """
    Show info about the DataFrame (types, nulls, etc.).
    """
    return self.df.info()

  def get_types(self) -> pd.Series:
    """
    Get data types for each column.
    :return: Series with column types
    """
    return self.df.dtypes

  def values_percentage_mis(self) -> pd.Series:
    """
    Get % of missing values per column.
    :return: Series with missing value percentage
    """
    return self.df.isna().mean() * 100

  def count_duplicates(self) -> int:
    """
    Count duplicated rows.
    :return: number of duplicates
    """
    return self.df.duplicated().sum()

  def index_duplicates(self) -> int:
    """
    Count duplicated index values.
    :return: number of duplicate index entries
    """
    return self.df.index.duplicates().sum()

  def drop_duplicates(self) -> pd.DataFrame:
    """
    Remove duplicated rows.
    :return: DataFrame without duplicates
    """
    self.df = self.df.drop_duplicates()
    return self.df

  def drop_duplicates_index(self) -> pd.DataFrame:
    """
    Remove duplicated index values (keep first).
    :return: DataFrame with unique index
    """
    self.df = self.df[~self.df.index.duplicated(keep='first')]
    return self.df

  def num_unique_values(self) -> pd.Series:
    """
    Count unique values in each column.
    :return: Series with number of unique values
    """
    return self.df.nunique()
