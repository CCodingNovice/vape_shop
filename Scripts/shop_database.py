import pandas as pd
import pickle


def create_new_df(cols):
	"""
	создает новый дф
	:param cols: лист с именами столбцов
	:return: созданный датафрейм
	"""
	df = pd.DataFrame(data=None, columns=cols)
	return df


def add_to_df(df, item):
	"""

	:param df: в какой дф добавить запись
	:param item: новый элемент(лист, нулевой элемент-айди)
	:return: измененный дф
	"""
	df.loc[item[0]] = item[1:]
	return df


def delete_from_df(df, item_id):
	"""
	удаляет итем из дф по его айди
	:param df: из какого дф удалить
	:param item_id: айди удаляемого элемента
	:return: измененный дф
	"""
	df.drop(item_id, inplace=True)
	return df


def get_from_df(index):
	df = load_csv_to_df("database_example")
	return df.iloc[int(index)]


def save_df_as_csv(df, name):
	"""

	:param df: дф который нужно сохранить
	:param name: имя сохраняемого дф без расширения
	:return: путь до сохраненного файла
	"""
	path = '../Data/' + name + '.csv'
	df.to_csv(path_or_buf=path)
	return path


def save_df_as_binary(df, name):
	"""
	честно говоря не ебу что это но в тз есть значит надо
	:param df:наш дф
	:param name: имя сохраненняемого файла
	:return: путь до него
	"""
	path = '../Data/' + name + '_binary.pickle'
	with open(path, 'wb') as f:
		pickle.dump(df, f)
	return path


def load_csv_to_df(name='database_example'):
	"""
	загружает ксв файл из папки Data с определенным именем
	:param name: имя ксв файла без расширения
	:return: загруженнный дф
	"""
	path = '../Data/' + name + '.csv'
	df = pd.read_csv(filepath_or_buffer=path, index_col=0)
	return df


def load_binary_to_df(name='database_example'):
	"""
	создает дф из банарного файла
	:param name: имя бинарного файла без расширения
	:return: загруженнный датафрейм
	"""
	# TODO придумать как обарабатывать ошибки
	path = '../Data/' + name + '_binary.pickle'
	try:
		with open(path, 'rb') as f:
			df = pickle.load(f)
	except (FileNotFoundError, pickle.PickleError, pickle.PicklingError, pickle.UnpicklingError):
		print("something has gone wrong with unpickling...")
		df = 0
	return df


def change_value(df, item_id, column_name, new_value):
	"""
	изменяет значение в дф
	:param df: дф который нужно изменить
	:param item_id: айди элемента
	:param column_name: имя поля
	:param new_value: новое значение
	:return: измененный дф(скорее всего потом уберу это ибо нахера)
	"""
	try:
		df.at[item_id, column_name] = new_value
	except ValueError:
		print("something has gone wrong with changing")
	return df


if __name__ == "__main__":
	# DF = load_csv_to_df()
	# print(DF)
	# change_value(DF, 62, "amount", ["lol", 1])
	# print(DF)
	# """
	# print(DF.index.array)
	DF = load_binary_to_df("ll")
	print(DF)
