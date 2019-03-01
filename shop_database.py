import pandas as pd


def create_new_df(cols):
    df = pd.DataFrame(data=None, columns=cols)
    return df


def add_to_df(df, item):
    df.loc[item[0]] = item[1:]
    return df


def save_df_as_csv(df, path='database_example.csv'):
    df.to_csv(path_or_buf=path)


def load_csv_to_df(path='database_example.csv'):
    df = pd.read_csv(filepath_or_buffer=path, index_col=0)
    return df


cols = ['type', 'name', 'price']  # column names
DF = create_new_df(cols)
