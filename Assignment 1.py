# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 08:58:00 2023.

@author: aaron
"""

import pandas as pd
import matplotlib.pyplot as plt


def lineplot(clist):
    """Function to plot line plot from unemp_rate dataframe
       using matplotlib.pyplot with the argument country list
    """

    plt.figure(figsize=(15, 5.75))

    for i in clist:  # for loop to plot each country
        plt.plot(unemp_rate.index, unemp_rate[i], label=i)

    plt.xticks(range(2001, 2021, 2), fontsize=15)  #
    plt.yticks(fontsize=15)
    plt.xlim(2001, 2020)
    plt.xlabel("Year", fontsize=17)
    plt.ylabel("Unemployment Rate", fontsize=17)
    plt.title("Unemployment Rates of G7 Countries(2001-2020)", fontsize=22)
    plt.legend()
    plt.savefig("Unemployment Rates of G7 Countries(2001-2020).png")
    plt.show()


def piechart(i1, i2):
    """Function to produce two piecharts, using matplotlib.pyplot,
       from unemp_rate dataframe with arguments indexes of unemp_rate
    """

    plt.figure(figsize=(20, 10))

    plt.subplot(1, 2, 1)  # first pie chart
    plt.pie(unemp_rate.iloc[int(i1)], labels=(unemp_rate.columns), autopct='%1.0f%%',
            textprops={'fontsize': 20})
    plt.title("Unemployment rates " + str(unemp_rate.index[int(i1)]),
              fontsize=25)

    plt.subplot(1, 2, 2)  # second pie chart
    plt.pie(unemp_rate.iloc[int(i2)], labels=unemp_rate.columns,
            autopct='%1.0f%%', textprops={'fontsize': 20})
    plt.title("Unemployment rates " + str(unemp_rate.index[int(i2)]),
              fontsize=25)

    plt.savefig("Unemployment Rates of G7 Countries" +
                str(unemp_rate.index[int(i1)]) + " & " +
                str(unemp_rate.index[int(i2)]) + ".png")
    plt.show()


def bargraph(i):
    """Function to plot a bargraph, using matplotlib.pyplot,
       from cpi dataframe with argument index of cpi
    """
    plt.figure(figsize=(15, 6))
    plt.bar(unemp_rate.columns, cpi.iloc[i], width=0.5)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xlabel("Country", fontsize=17)
    plt.ylabel("Consumer Price Index", fontsize=17)
    plt.title("Consumer Price Index of G7 countries in " + str(cpi.index[i]),
              fontsize=22)
    plt.savefig("Consumer Price Index of G7 countries in " +
                str(cpi.index[i]) + ".png")
    plt.show()


unemp_rate = pd.read_excel("g7_unemployment_rates.xlsx", index_col=0)
cpi = pd.read_excel("g7_cpi.xlsx", index_col=0)

countries = ["Canada", "France", "Germany", "Italy",
             "Japan", "United Kingdom", "United States"]

lineplot(countries)

piechart(0, -1)

bargraph(-1)
