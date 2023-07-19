"""
This module defines the following routines used by the 'ingest' step of the regression recipe:

- ``load_file_as_dataframe``: Defines customizable logic for parsing dataset formats that are not
  natively parsed by MLflow Recipes (i.e. formats other than Parquet, Delta, and Spark SQL).
"""
from pandas import DataFrame


def load_file_as_dataframe(file_path: str, file_format: str) -> DataFrame:
    """
    Load content from the specified dataset file as a Pandas DataFrame.

    This method is used to load dataset types that are not natively  managed by MLflow Recipes
    (datasets that are not in Parquet, Delta Table, or Spark SQL Table format). This method is
    called once for each file in the dataset, and MLflow Recipes automatically combines the
    resulting DataFrames together.

    :param file_path: The path to the dataset file.
    :param file_format: The file format string, such as "csv".
    :return: A Pandas DataFrame representing the content of the specified file.
    """

    if file_format == "csv":
        import pandas
        df = pandas.read_csv(file_path)
      
        df['norm_dl'] = df['deadlift']/df['weight']
        df['norm_j'] = df['candj']/df['weight']
        df['norm_s'] = df['snatch']/df['weight']
        df['norm_bs'] = df['backsq']/df['weight']
        df['total_lift'] = df['norm_dl']+df['norm_j']+df['norm_s']+df['norm_bs']

        col_to_drop=['age','athlete_id','name','region','team', 'affiliate','gender','eat','train','background','experience','schedule','howlong','norm_bs', 'norm_dl', 'norm_j', 'norm_s','filthy50','fgonebad','run400','run5k','pullups']
        df_select = df.drop(columns=col_to_drop)
        df_select=df_select.dropna()
      
        return df_select
    else:
        raise NotImplementedError
# lucy taiqiangle 
