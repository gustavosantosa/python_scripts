# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 14:23:07 2021

@author: gustasan
"""


import os
import pandas as pd
import matplotlib.pyplot as plt

#reading the file, skipping the first row, decimal place is a "," and separator is a ";")
#printing the data 5 first rows

folder_path = 'C:/Users/gustasan/.spyder-py3'

fileList = os.listdir(folder_path)  
for filename in fileList:
    if(filename.endswith('.txt')):  
         print(filename)


data = pd.read_csv('investimentos.txt', delimiter = '\t', header=0, decimal='.')
print(data.head())

#data.plot(subplots=True,layout=(5, 1),figsize=(10, 20),grid=True)
#plt.xticks(rotation=45)
#plt.ylabel('EUR')
#plt.xlabel('Date')
#plt.legend(loc='best')
#plt.autoscale()
#plt.savefig('teste',dpi=300)

#data.plot(0,[2,5],grid=True)
#plt.xticks(rotation=45)
#plt.ylabel('EUR')
#plt.xlabel('Date')
#plt.legend(loc=4)

data.plot(0,4, grid=True)
plt.xticks(rotation=45)
plt.ylabel('EUR')
plt.xlabel('Date')





