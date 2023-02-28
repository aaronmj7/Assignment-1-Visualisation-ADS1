# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 08:58:00 2023.

@author: aaron
"""

import pandas as pd
import matplotlib.pyplot as plt


def lineplot(df, headers):
    """Function to create a lineplot. Arguments:
        A dataframe with labelled index and columns to be taken as y.
        A list containing the headers of the columns to plot.
    """

    plt.figure(figsize=(17, 6.5))

    # plotting each head
    for head in headers:
        plt.plot(df.index, df[head], label=head)

    # increasing size of ticks
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)

    # removing white space left and right
    plt.xlim(df.index.min(), df.index.max())

    # labelling
    plt.xlabel("Year", fontsize=17)
    plt.ylabel("Consumer Price Index", fontsize=17)

    # titling
    plt.title("Consumer Price Index from " + str(df.index.min()) + " to " +
              str(df.index.max()), fontsize=25)

    plt.legend(fontsize=17)

    # saving as png
    plt.savefig("lineplot.png")

    plt.show()

    return


def piechart(df, i1, i2):
    """Function to create two piecharts. Arguments:
        A dataframe with rows to plot piecharts.
        Index of the row to be plotted in first piechart.
        Index of the row to be plotted in second piechart.
    """

    plt.figure(figsize=(20, 10))

    # first pie chart
    plt.subplot(1, 2, 1)
    plt.pie(df.iloc[int(i1)], labels=(df.columns),
            autopct='%1.0f%%', textprops={'fontsize': 20})
    # titling
    plt.title("Unemployment rates " + str(df.index[int(i1)]), fontsize=25)

    # second pie chart
    plt.subplot(1, 2, 2)
    plt.pie(df.iloc[int(i2)], labels=df.columns,
            autopct='%1.0f%%', textprops={'fontsize': 20})
    # titling
    plt.title("Unemployment rates " + str(df.index[int(i2)]), fontsize=25)

    # saving as png
    plt.savefig("piechart.png")

    plt.show()

    return


def bargraph(df, i):
    """Function to create a bargraph. Arguments:
        A dataframe with columns to be taken as x and rows to be taken as y.
        Index of the row to be taken as y.
    """
    plt.figure(figsize=(15, 6))

    plt.bar(df.columns, df.iloc[i], width=0.5)

    # increasing size of ticks
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)

    # labelling
    plt.xlabel("Country", fontsize=17)
    plt.ylabel("Unemployment rates", fontsize=17)

    # titling
    plt.title("Unemployment rates in " + str(df.index[i]), fontsize=22)

    # saving as png
    plt.savefig("bargraph.png")

    plt.show()

    return


# creating dataframe from the data
df_unemp_rate = pd.read_excel("g7_unemployment_rates.xlsx", index_col=0)
df_cpi = pd.read_excel("g7_cpi.xlsx", index_col=0)

# creating list of countries to be plotted
countries = ["Canada", "France", "Germany", "Italy",
             "Japan", "United Kingdom", "United States"]

# calling lineplot with dataframe and columns to be plotted
lineplot(df_cpi, countries)

# calling piechart with dataframe and row indexes to be plotted
piechart(df_unemp_rate, 0, -1)

# calling bargraph withdataframe and row index to be plotted
bargraph(df_unemp_rate, -1)
