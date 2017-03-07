#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 12:33:52 2017

@author: venusgrape

Write a function to flatten a list. The list contains other lists, strings, or ints. For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into [1,'a','cat',2,3,'dog',4,5] (order matters).

"""
flaten = []
def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    
    '''
    
    for l in aList:
        if type(l) != list:
            flaten.append(l)
        else:
            flatten(l)
    return flaten

aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten(aList))