#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 09:45:53 2020

@author: mei
"""


'''
le code pour ASCII art sur le CodinGame 
Il faut copier le code sur ce site https://www.codingame.com/ide/puzzle/ascii-art et le lancer

'''
import syss
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

alp="ABCDEFGHIJKLMNOPQRSTUVWXYZ?"

l = int(input())
h = int(input())
t = input().upper()
rows = []
for i in range(h):
    rows.append(input())


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
for item in rows:
    for lettre in t:
        pos = alp.find(lettre)
        if pos != -1:
            print(item[l*pos:l*(pos+1)], end="")
        else:
            print(item[-l:],end="")
    print()
