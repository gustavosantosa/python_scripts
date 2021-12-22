# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 19:01:18 2021

@author: santo
"""

import pandas as pd
import matplotlib.pyplot as plt
import ntpath

filename = ('08072021_Gustavo_hahella.csv')
data = pd.read_csv(filename, sep=",", decimal=".")

print (ntpath.splitext(filename)[0])
print (data.head())


x = data['Min']
y1 = data['Blank']
y2 = data['avg(2mg)']
y3 = data['avg(10mg)']
stdev1 = data['stdev(0mg)']
stdev2 = data['stdev(2mg)']
stdev3 = data['stdev(10mg)']


plt.errorbar(x, y1, yerr=stdev1, elinewidth=0.5, capsize=1, linestyle="--",linewidth=0.5 , marker="o" ,markersize=3)
plt.errorbar(x, y2, yerr=stdev2, elinewidth=0.5, capsize=1 ,linestyle="--",linewidth=0.5 , marker="o" ,markersize=3)
plt.errorbar(x, y3, yerr=stdev3, elinewidth=0.5, capsize=1 ,linestyle="--",linewidth=0.5 , marker="o" ,markersize=3)

plt.xlabel("Time (min)")
plt.ylabel("ABS [473 nm]")
plt.title(ntpath.splitext(filename)[0])
plt.legend(['Blank','avg(2mg)','avg(10mg)'])

plt.savefig(ntpath.splitext(filename)[0]+' errrr bars', dpi=300)

plt.show()
