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
    plt.xlabel("Year", fontsize=17)
    plt.ylabel("Unemployment Rate", fontsize=17)
    plt.title("Unemployment Rates of G7 Countries(2001-2020)", fontsize=20)
    plt.legend()
    '''plt.savefig("Unemployment Rates of G7 Countries(2001-2020).png")'''
    plt.show()


def piechart(i1, i2):
    """Function to produce two piecharts, using matplotlib.pyplot,
    from unemp_rate dataframe with arguments index of unemp_rate
    """

    plt.figure(figsize=(15, 20))

    plt.subplot(1, 2, 1)
    plt.pie(unemp_rate.iloc[int(i1)], labels=(countries), autopct='%1.0f%%')
    plt.title("Unemployment rates " + str(unemp_rate.index[int(i1)]),
              fontsize=20)

    plt.subplot(1, 2, 2)
    plt.pie(unemp_rate.iloc[int(i2)], labels=(countries), autopct='%1.0f%%')
    plt.title("Unemployment rates " + str(unemp_rate.index[int(i2)]),
              fontsize=20)

    '''plt.savefig("Unemployment Rates of G7 Countries" +
             str(unemp_rate.index[int(a)]) + " & " +
             +str(unemp_rate.index[int(b)]) + ".png")'''
    plt.show()


def bargraph(i):
    """Function to plot a bargraph, using matplotlib.pyplot,
    from cpi dataframe with argument index of cpi
    """
    plt.figure(figsize=(16, 6))
    plt.bar(cpi.columns, cpi.iloc[i])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xlabel("Country", fontsize=20)
    plt.ylabel("Consumer Price Index", fontsize=20)
    plt.title("Consumer Price Index of G7 countries in " + str(cpi.index[i]),
              fontsize=20)
    plt.show()


unemp_rate = pd.read_excel("g7_unemployment_rates.xlsx", index_col=0)
cpi = pd.read_excel("g7_cpi.xlsx", index_col=0)

countries = ["Canada", "France", "Germany", "Italy",
             "Japan", "United Kingdom", "United States"]

lineplot(countries)

piechart(5, 19)

bargraph(-1)
