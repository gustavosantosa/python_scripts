# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 14:39:05 2021

@author: gustasan
"""

import pandas as pd
import matplotlib.pyplot as plt
import glob

for filename in glob.glob('*.txt'):
        data = pd.read_csv(filename, sep='\t', skiprows=0, decimal='.')
        ax = data.plot(0,1, title = filename)
        plt.xlabel('Time (min')
        plt.ylabel('ABS (a.u.)')
        plt.plot()
        #plt.show()
        #plt.savefig(fname="Hahella#2_no_CPD",dpi=300)