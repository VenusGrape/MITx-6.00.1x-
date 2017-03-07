#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 11:55:35 2017

@author: venusgrape

Implement a function that meets the specifications below.

"""
def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    L = L[::-1]
    for l in L:
        l.reverse()
    return L


L = [[1, 2], [3, 4], [5, 6, 7]]
print(deep_reverse(L))