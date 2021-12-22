# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 19:52:47 2021

@author: santo
"""
import pandas as pd
import matplotlib.pyplot as plt
import ntpath

filename = ('08072021_Gustavo_hahella.csv')
data = pd.read_csv(filename, sep=",", decimal=".")

print (ntpath.splitext(filename)[0])
print (data.head())

data.plot(0,[1,2,3],linestyle="--",linewidth=0.5 , marker="o" ,markersize=4)
plt.xlabel('Time [min]')
plt.ylabel('ABS [473nm]')
plt.title(ntpath.splitext(filename)[0])

plt.savefig(ntpath.splitext(filename)[0]+' no errors',dpi=300)#