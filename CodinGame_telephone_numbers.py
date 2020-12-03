#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 13:39:56 2020

@author: meg
"""
'''
CodinGame telephone number : https://www.codingame.com/training/medium/telephone-numbers
'''

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.



# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
class Node:
    """
    Un nœud de trie. Il a un caractère et des nœuds enfants (vide à l'initialisation)
    """
    def __init__(self, char):
        self.value = char
        self.children = {}

class Trie:
    """
    trie
    """
    def __init__(self):
        """
        À l'initialisation on a juste un nœud racine vide
        """
        self.root = Node("")
        self.count = 0
        
    def insert(self, number):
        """
        Un nouveau mot dans le trie
        """
        node = self.root
        
        for char in number:
            if char in node.children:
                node = node.children[char]
            else:
                # Si un caractère du mot est inconnu
                # on ajoute un nouveau nœud
                new_node = Node(char)
                node.children[char] = new_node
                node = new_node
                self.count += 1

    def getter_count(self):
        return self.count


def main():
    n = int(input())
    telephone_Number = Trie()
    for i in range(n):
        telephone = input()
        telephone_Number.insert(telephone)


    # The number of elements (referencing a number) stored in the structure.
    
    print(telephone_Number.getter_count())

if __name__ == '__main__':
    main()