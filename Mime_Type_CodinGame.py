#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 09:45:30 2020

@author: mei 
"""
'''
l'exercice sur CodinGame https://www.codingame.com/ide/puzzle/mime-type
'''
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
table = {}
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    table[ext.lower()] = mt
# print(table)

output_list = []
for i in range(q):
    fname = input()  # One file name per line.

    if "." in fname:
        name,ext = fname.rsplit(".",1)
        try:
            print(table[ext.lower()])
        except KeyError:
            print("UNKNOWN")
    else:
        print("UNKNOWN")