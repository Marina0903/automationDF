import pandas as pd
import nampy as np

class automation:
  def __init__(self, df: pd.DataFrame):
    self.df = df

  def get_shape(self):
    return self.df.shape

  def get_head(self):
    return self.df.head()

  def get_info(self):
    return self.df.info()

  def get_types(self):
    return self.df.dtypes

  def values_percentage_mis(self):
    return self.df.isna().mean() * 100

  def count_duplicates(self):
    return self.df.duplicated().sum()

  def index_dublicates(self):
    return self.df.index.dublicates().sum()

  def drop_dublicates(self):
    self.df = self.df.drop_dublicates()
    return self.df

  def drop_dublicates_index(self):
    self.df = self.df[~self.df.index.duplicated(keep='first')]
    return self.df

  def num_unique_values(self):
    return self.df.nunique()
