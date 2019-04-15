import pandas as pd
from tkinter import *
import matplotlib.pyplot as plt






columns = ['type', 'name', 'price', 'amount']
DF = pd.read_csv('/Users/sirazutdinefendiev/Desktop/vape_shop/Data/database_example.csv')
print(DF)




def PriceName():																			# Цена - Имя
	plt.pie(DF['price'], labels= DF['price'], shadow=5, autopct='%1.1f%%')
	plt.title("Цена - Имя")
	plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2, labels= DF['name'], )
	plt.show()

def AmountName():
	plt.pie(DF['amount'], labels=DF['amount'], shadow=5, autopct='%1.1f%%')
	plt.title("Количество - Имя")
	plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2, labels=DF['name'], )
	plt.show()


#def AmountType():
#	plt.pie(DF['amount'], labels=DF['amount'], shadow=5, autopct='%1.1f%%')
#	plt.title("Количество - Тип")
#	plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2, labels=DF['type'], )
#	plt.show()



main = Tk()




PriceNameButton = Button(main, text='Цена - Имя', background="gray", foreground="black", command=PriceName)
PriceNameButton.pack(side=LEFT)

AmountNameButton = Button(main, text='Количество - Имя', background="gray", foreground="black", command=AmountName)
AmountNameButton.pack(side=LEFT)

#AmountTypeButton = Button(main, text='Количество - Тип', background="gray", foreground="black", command=AmountType)
#AmountTypeButton.pack(side=LEFT)





main.mainloop()
