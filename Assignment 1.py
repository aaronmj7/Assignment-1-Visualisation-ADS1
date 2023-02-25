# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 08:58:00 2023

@author: aaron
"""

import pandas as pd
import matplotlib.pyplot as plt

unemp_rate = pd.read_excel("g7_unemployment_rates.xlsx", index_col=0)
cpi = pd.read_excel("g7_cpi.xlsx", index_col=0)

plt.figure()
plt.plot(unemp_rate.index,unemp_rate["Canada"])
plt.xlim(2001,2020)
plt.show()

