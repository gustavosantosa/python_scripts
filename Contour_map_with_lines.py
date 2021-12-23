# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 10:33:55 2021

@author: gustasan
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import matplotlib.cm as cm # matplotlib's color map library

#reading the file
df = pd.read_csv('final.csv', decimal='.', header=None)
df.round(1)

#printing the head of the dataframe
print(df.head())

#creating the X and Y values and the array
y = np.arange(250,460,10)
x = np.arange(200,360,10)

X,Y = np.meshgrid(x,y)

# Initialize plot objects
rcParams['figure.figsize'] = 8, 8 # sets plot size
fig = plt.figure()
ax = fig.add_subplot(111)

# Define levels in z-axis where we want lines to appear
levels = np.array([-5,0,15,30,45,60,75,85])

# Generate a color mapping of the levels we've specified

cp = ax.contourf(X,Y,df, levels=len(levels),) #cmap=cm.hot

# Set all level lines to black
line_colors = ['black' for l in levels]

# Make plot and customize axes
cp = ax.contour(X,Y,df, levels=levels, colors=line_colors)

#edit level line format
ax.clabel(cp, fontsize=12, fmt='%d')

ax.set_xlabel('Excitation \u03BB (nm)',fontsize=15)
ax.set_title('Hahella#1 Fluorescence spectra',fontsize=15)
ax.set_ylabel('Emission \u03BB (nm)',fontsize=15)
ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=12)

#saving the figure
plt.savefig('hahella#1 fluorescence spectra.pdf')

#creating the contour
#plt.contour(X,Y,df)
#plt.colorbar()






