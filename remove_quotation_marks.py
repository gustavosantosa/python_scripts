# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#remove quotation marks from file

filename = 'bacterial_candidates_trimmed.txt'
output = 'bacterial_candidates_trimmed_no_quotations.txt'

with open(filename, 'r') as f, open(output, 'w') as fo:
    for line in f:
        fo.write(line.replace('"', '').replace("'", ""))