#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 13:06:57 2020

@author: meg

le site de CodinGame : https://www.codingame.com/ide/puzzle/scrabble
"""
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
words = []
n = int(input())
for i in range(n):
    w = input()
    words.append(w)
letters = input()
# print(letters, file=sys.stderr, flush=True)
letterGiven = [i for i in letters]
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
pointsdicte = {'1':['e', 'a', 'i', 'o', 'n', 'r', 't', 'l', 's', 'u'],
        '2':['d', 'g'],
        '3':['b', 'c', 'm', 'p'],
        '4':['f', 'h', 'v', 'w', 'y'],
        '5':['k'],
        '8':['j', 'x'],
        '10':['q', 'z']}


valideWords = list(words)
points = []
#  trouver les valides mots
for word in words:
    letters = list(letterGiven)
    # parcourir chaque mot dans la liste words
    # letterList = [i for i in word] 
    # voir si tous les mots sont dans la liste letterList
    for letter in word:
        if letter in letterGiven:
            if letter in letters:
                letters.remove(letter)
            else:
                valideWords.remove(word)
                break
        else:
            valideWords.remove(word)
            break

#  trouver le mot dont le point est le plus évelé
for word in valideWords:
    point = 0 # initialization de point 
    # letterList = [i for i in word]
    for letter in word:
        for k,v in pointsdicte.items():
            if letter in v:
                point += int(k)
    
    points.append(point)

max = 0
pos = 0
for i in range(len(points)):
    if points[i] > max:
        max = points[i]
        pos = i

valide = valideWords[pos]
print(valide)
