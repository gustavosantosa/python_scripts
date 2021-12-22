# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 14:23:07 2021

@author: gustasan
"""

import pandas as pd
import matplotlib.pyplot as plt

# reading the file, , decimal place is a "," and separator is a ";"
# printing the 5 first rows of the data

data1 = pd.read_csv('pH_dependence.txt', decimal=("."), sep=("\t"), header=None,usecols=[0,1,2])
data2 = pd.read_csv('pH_dependence.txt', decimal=("."), sep=("\t"), header=None,usecols=[3,4,5])

ax = data1.plot(0,1,yerr=2,linestyle='--',marker='.')

data2.plot(3,4,yerr=5,linestyle='--',marker='.',ax=ax)

#plt.show()

