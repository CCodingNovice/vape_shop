import pandas as pd
from tkinter import *
import matplotlib.pyplot as plt
from shop_database import load_csv_to_df
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib



def save_chart(name, name_chart):
	"""
	Сохраняет пайчарТ в папку Output
	"""
	name_chart.savefig('Output/' + str(name) + '.png', bbox_inches='tight')



def plot_the_graph():
	columns = ['type', 'name', 'price', 'amount']

	DF = load_csv_to_df('database_example')

	def PriceName():

		"""
		строит пайчарТ Цена - Имя
		"""
		plt.clf()
		plt.pie(DF['price'], labels= DF['price'], shadow=5, autopct='%1.1f%%', radius = 0.8, textprops={'size': 'smaller'})
		plt.title("Цена - Имя")
		plt.legend(loc='upper center', bbox_to_anchor=(0.5 , 0.1), shadow=True, ncol=3, labels= DF['name'], prop={'size': "smaller"})


		chart1 = Tk()  # окно в котором построится пайчарТ Цена - Имя
		chart1.config(bg='#49464c')

		pn = plt.figure(1)
		pn.patch.set_facecolor('xkcd:gray')
		canvas = FigureCanvasTkAgg(pn, master=chart1)

		plot_widget = canvas.get_tk_widget()

		plot_widget.pack()
		save_chart('PriceName', pn)
		chart1.mainloop()



	def AmountName():
		"""
		строит пайчарТ Количество - Имя
		"""
		plt.clf()
		plt.pie(DF['amount'], labels=DF['amount'], shadow=5, autopct='%1.1f%%', radius = 0.8, textprops={'size': 'smaller'})
		plt.title("Количество - Имя")
		plt.legend(loc='upper center', bbox_to_anchor=(0.5, 0.1), shadow=True, ncol=3, labels=DF['name'], prop={'size': "smaller"})

		chart2 = Tk() # окно в котором построится пайчарТ Цена - Количество
		chart2.config(bg='#49464c')
		an = plt.figure(1)
		an.patch.set_facecolor('xkcd:gray')
		canvas = FigureCanvasTkAgg(an, master=chart2)

		plot_widget = canvas.get_tk_widget()

		plot_widget.pack()
		save_chart('AmountName', an)
		chart2.mainloop()



	def AmountType():
		"""
		строит пайчарТ Количество - Тип
		"""

		typecol1 = [] # список содержащий элементы type без повторений
		amountcol = [] # список содержащий количество вейпов всех типов без повторений
		plt.clf()
		for i in list(DF.index):
			j = 0
			flag = False

			while j < len(typecol1):
				if typecol1[j] == DF['type'][i]:
					amountcol[j] += DF['amount'][i]
					flag = True
				j += 1
			if not flag:
				typecol1.append(DF['type'][i])
				amountcol.append(DF['amount'][i])


		plt.pie(amountcol, labels=amountcol, shadow=5, autopct='%1.1f%%', radius = 0.8, textprops={'size': 'smaller'})
		plt.title("Количество - Тип")
		plt.legend(loc='upper center', bbox_to_anchor=(0.5, 0.1), shadow=True, ncol=3, labels=typecol1, prop={'size': "smaller"})

		chart3 = Tk() # окно в котором построится пайчарТ Количество - Тип
		chart3.config(bg='#49464c')
		at = plt.figure(1)
		at.patch.set_facecolor('xkcd:gray')
		canvas = FigureCanvasTkAgg(at, master=chart3)

		plot_widget = canvas.get_tk_widget()

		plot_widget.pack()
		save_chart('AmountType', at)
		chart3.mainloop()



	def PriceType():
		"""
		строит пайчарТ Цена - Тип
		"""
		typecol2=[] # список содержащий элементы type без повторений
		pricecol=[] # список содержащий цену вейпов всех типов без повторений

		chart4 = Tk() # окно в котором построится пайчарТ Цена - Тип
		chart4.config(bg='#49464c')

		for i in list(DF.index):
			j = 0
			flag = False

			while j < len(typecol2):
				if typecol2[j] == DF['type'][i]:
					pricecol[j] += DF['price'][i]
					flag = True
				j += 1
			if not flag:
				typecol2.append(DF['type'][i])
				pricecol.append(DF['price'][i])

		plt.clf()
		plt.pie(pricecol, labels=pricecol, shadow=5, autopct='%1.1f%%', radius = 0.8, textprops={'size': 'smaller'})
		plt.title("Цена - Тип")
		plt.legend(loc='upper center', bbox_to_anchor=(0.5, 0.1), shadow=True, ncol=3, labels=typecol2, prop={'size': "smaller"})




		pt = plt.figure(1)
		pt.patch.set_facecolor('xkcd:gray')
		canvas = FigureCanvasTkAgg(pt, master=chart4)

		plot_widget = canvas.get_tk_widget()

		plot_widget.pack()
		save_chart('PriceType', pt)
		chart4.mainloop()



	matplotlib.use('TkAgg')

	main = Tk()
	main.config(bg='#49464c')
	main.geometry("250x150+600+300")



	def func(value):
		if str(value) == "Цена - Имя":
			PriceName()
		elif str(value) == "Количество - Имя":
			AmountName()
		elif str(value) == "Количество - Тип":
			AmountType()
		elif str(value) == "Цена - Тип":
			PriceType()

	options = ["Цена - Имя", "Количество - Имя", "Количество - Тип", "Цена - Тип"]
	var = StringVar()
	var.set("Выбрать график")

	drop = OptionMenu(main, var, *options, command=func).pack(expand=1)

	main.mainloop()


plot_the_graph()
