import pandas as pd
from tkinter import *
import matplotlib.pyplot as plt
from shop_database import load_csv_to_df





columns = ['type', 'name', 'price', 'amount']

#DF = load_csv_to_df()                      # проблемс: при использовании ваниной функции ломаются цена-тип количество-тип... при использовании ссылки на database - все нормас
DF = pd.read_csv('/Users/sirazutdinefendiev/Desktop/vape_shop/Data/database_example.csv')
print(DF)




def PriceName():
	plt.pie(DF['price'], labels= DF['price'], shadow=5, autopct='%1.1f%%')
	plt.title("Цена - Имя")
	plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2, labels= DF['name'], )
	plt.show()

def AmountName():
	plt.pie(DF['amount'], labels=DF['amount'], shadow=5, autopct='%1.1f%%')
	plt.title("Количество - Имя")
	plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2, labels=DF['name'], )
	plt.show()


def AmountType():

	icol1=0

	typecol1 = [] # список содержащий элементы type без повторений
	amountcol = [] # список содержащий количество вейпов всех типов без повторений

	for i in DF['type']:
		j = 0
		flag = False

		while j < len(typecol1):
			if typecol1[j] == i:
				amountcol[j] += DF['amount'][icol1]
				flag = True
			j += 1
		if not flag:
			typecol1.append(i)
			amountcol.append(DF['amount'][icol1])    ########

		icol1 += 1

	plt.pie(amountcol, labels=amountcol, shadow=5, autopct='%1.1f%%')
	plt.title("Количество - Тип")
	plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2, labels=typecol1)
	plt.show()


def PriceType():

	icoll=0

	typecol2=[] # список содержащий элементы type без повторений
	pricecol=[] # список содержащий цену вейпов всех типов без повторений

	for i in DF['type']:
		j = 0
		flag = False

		while j < len(typecol2):
			if typecol2[j] == i:
				pricecol[j] += DF['price'][icoll]
				flag = True
			j += 1
		if not flag:
			typecol2.append(i)
			pricecol.append(DF['price'][icoll])

		icoll += 1

	plt.pie(pricecol, labels=pricecol, shadow=5, autopct='%1.1f%%')
	plt.title("Цена - Тип")
	plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2, labels=typecol2)
	plt.show()





main = Tk()
main.config(bg='dimgray')
main.geometry("250x150+600+300")


def func(value):
	if str(value) == "Цена - Имя":
		PriceName()
	elif str(value) == "Количество - Имя":
		AmountName()
	elif str(value) == "Количество - Тип":
		AmountType()
	elif str(value) == "Цена - тип":
		PriceType()

options = ["Цена - Имя", "Количество - Имя", "Количество - Тип", "Цена - Тип"]
var = StringVar()
var.set("Выбрать график")
drop = OptionMenu(main, var, *options, command=func).pack(expand=1)




main.mainloop()
