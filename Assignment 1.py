# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 08:58:00 2023.

@author: aaron
"""

import pandas as pd
import matplotlib.pyplot as plt


def lineplot(list):
    """Function to plot the list as line plot from
    unemp_rate dataframe using matplotlib.pyplot
    """

    plt.figure(figsize=(13, 5.75))

    for i in list:
        plt.plot(unemp_rate.index, unemp_rate[i], label=i)

    plt.xticks(range(2001, 2021))
    plt.xlim(2001, 2020)
    plt.xlabel("Year")
    plt.ylabel("Unemployment Rate")
    plt.title("Unemployment Rates of G7 Countries(2001-2020)")
    plt.legend()
    '''plt.savefig("Unemployment Rates of G7 Countries(2001-2020).png")'''
    plt.show()


def piechart(a, b):
    """Function to produce two piecharts, using matplotlib.pyplot,
    from unemp_rate dataframe with arguments index of unemp_rate
    """

    plt.figure(figsize=(15, 20))

    plt.subplot(1, 2, 1)
    plt.pie(unemp_rate.iloc[int(a)], labels=(countries), autopct='%1.0f%%')
    plt.title("Unemployment rates " + str(unemp_rate.index[int(a)]))
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.pie(unemp_rate.iloc[int(b)], labels=(countries), autopct='%1.0f%%')
    plt.title("Unemployment rates " + str(unemp_rate.index[int(b)]))
    plt.legend()

    '''plt.savefig("Unemployment Rates of G7 Countries" +
             str(unemp_rate.index[int(a)]) + " & " +
             +str(unemp_rate.index[int(b)]) + ".png")'''
    plt.show()


unemp_rate = pd.read_excel("g7_unemployment_rates.xlsx", index_col=0)
cpi = pd.read_excel("g7_cpi.xlsx", index_col=0)

countries = ["Canada", "France", "Germany", "Italy",
             "Japan", "United Kingdom", "United States"]

lineplot(countries)

piechart(0, 19)

plt.figure(figsize=(11,6))
plt.bar(cpi.columns, cpi.iloc[-1])
plt.xlabel()
plt.ylabel()
plt.title()
plt.show()
