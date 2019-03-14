import pandas as pd
from tkinter import *
import matplotlib.pyplot as plt


def load_csv_to_df(name='database_example'):
	"""
	загружает ксв файл из папки Data с определенным именем
	:param name: имя ксв файла без расширения
	:return: загруженнный дф
	"""
	path =  name + '.csv'
	df = pd.read_csv(filepath_or_buffer=path, index_col=0)
	return df




columns = ['type', 'name', 'price']  # column names
DF = load_csv_to_df()
print(DF)




def price():
	plt.pie(DF['price'], labels= DF['name'], shadow=5, autopct='%1.1f%%')
	plt.title("Цена")
	plt.pie(DF['price'])
	plt.show()



main = Tk()

main.configure(background="#49464c")
main.geometry("800x600")
zzz = Frame(main)
zzz.config(bg='dimgray')

pp = Label(background="#49464c", text=' ')
pp.grid(row=0, rowspan=4, column=0, columnspan=3)



MainLabel = Label(main, text='Выберите диаграму')
MainLabel.grid(row=3, columns=2)


PriceButton = Button(main, text='цена', background="gray", foreground="black", command=price)
PriceButton.grid(row=7, columns=2)






main.mainloop()
