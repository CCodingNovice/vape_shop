import pandas as pd


def create_new_df(cols):
	"""
	функция создает и возвращает пустой датафрейм
	на вход принимает лист имен колонок
	"""
	df = pd.DataFrame(data=None, columns=cols)
	return df


def add_to_df(df, item):
	"""
	принимает на вход датафрейм и объект и добавляет его
	возвращает измененный датафрейм хотя можно было и не возвращать
	"""
	df.loc[item[0]] = item[1:]
	return df


def delete_from_df(df, item_id):
	"""удаляет итем из дф по его айди"""
	df.drop(item_id, inplace=True)
	return df


def save_df_as_csv(df, name):
	"""
	сохраняет дф в папку Data как csv с определенным именем
	возвращает путь до файла
	"""
	path = 'Data/' + name + '.csv'
	df.to_csv(path_or_buf=path)
	return path


def load_csv_to_df(name='database_example'):
	"""загружает ксв файл из папки Data с определенным именем"""
	path = 'Data/' + name + '.csv'
	df = pd.read_csv(filepath_or_buffer=path, index_col=0)
	return df


columns = ['type', 'name', 'price']  # column names
DF = load_csv_to_df()
print(DF)
