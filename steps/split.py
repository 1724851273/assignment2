"""
This module defines the following routines used by the 'split' step of the regression recipe:

- ``create_dataset_filter``: Defines customizable logic for filtering the training
  datasets produced by the data splitting procedure. Note that arbitrary transformations
  should go into the transform step.
"""

from pandas import DataFrame, Series


def create_dataset_filter(df: DataFrame) -> Series(bool):
    """
    Mark rows of the split datasets to be additionally filtered. This function will be called on
    the training datasets.

    :param dataset: The {train,validation,test} dataset produced by the data splitting procedure.
    :return: A Series indicating whether each row should be filtered
    """
    # FIXME::OPTIONAL: implement post-split filtering on the dataframes, such as data cleaning.

    return (
      (~df['region','age','weight','height','howlong','gender','eat','train','background','experience','schedule','howlong','deadlift',
       'candj','snatch','backsq','experience','background','schedule','howlong'].isna().any(axis=1) |
       (df['weight'] < 1500) & (df['gender']!='--') & (df['age']>=18) & ((df['height']<96)&(df['height']>48)) & 
       ((df['deadlift']>0)&(df['deadlift']<=1105)|((df['gender']=='Female')&(df['deadlift']<=636))) & 
       ((df['candj']>0)&(df['candj']<=395)) & ((df['snatch']>0)&(df['snatch']<=496)) & ((df['backsq']>0)&(df['backsq']<=1069))))
