import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import csv
import pandas as pd
from pandas import read_csv
df1 = read_csv("Data\\database_example.csv", sep=',')
dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )

plt.title('Количество товаров (%)')

xs = range(len(df1['name']))

plt.pie(
    df1['amount'], autopct=None, radius = 1.1,
    explode = [0.15] + [0 for _ in range(len(df1['amount']) - 1)] )
plt.legend(
    bbox_to_anchor = (-0.16, 0.45, 0.25, 0.25),
    loc = 'lower left', labels = df1['name'] )
fig.savefig('pie.png')