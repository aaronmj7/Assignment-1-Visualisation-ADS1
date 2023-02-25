# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 08:58:00 2023

@author: aaron
"""

import pandas as pd
import matplotlib.pyplot as plt


def lineplot(list):
    """ Function to plot the list as line plot from
    umemp_rate dataframe using matplotlib.pyplot
    """
    plt.figure(figsize=(13,5.75))

    for i in list:
        plt.plot(unemp_rate.index,unemp_rate[i],label=i)

    plt.xticks(range(2001,2021))
    plt.xlim(2001,2020)
    plt.xlabel("Year")
    plt.ylabel("Unemployment Rate")
    plt.title("Unemployment Rates of G7 Countries(2001-2020)")
    plt.legend()
    plt.show()


unemp_rate = pd.read_excel("g7_unemployment_rates.xlsx", index_col=0)
cpi = pd.read_excel("g7_cpi.xlsx", index_col=0)

countries = ["Canada","France","Germany","Italy","Japan",
             "United Kingdom","United States"]
lineplot(countries)

