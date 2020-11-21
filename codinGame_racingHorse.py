#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 11:16:55 2020

@author: mei
"""

'''
il faut copier le script dans le site Codingame : https://www.codingame.com/ide/puzzle/horse-racing-duals

'''

import sys
import math



# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
stren_list = []
for i in range(n):
    pi = int(input())
    stren_list.append(pi)
    
stren_list.sort()
#make a compare list by copying the original
compare_list= list(stren_list)
compare_list.insert(0,0)
stren_list.append(0)
# print(stren_list)

#initializaition the closest value 
closest = int(stren_list[0])

#compare begins
for i in range(0,len(stren_list)-1):
    diff = abs(int(stren_list[i]) - int(compare_list[i]))
    if diff < closest:
        closest = diff


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(closest)