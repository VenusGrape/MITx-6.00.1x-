#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 08:09:20 2017

@author: venusgrape

"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest_val(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    bgk = []
    val = aDict.values()
    ky = aDict.keys()
    
    biggest = 0
    for i in val:
        if len(i) > biggest:
            biggest = len(i)
            
    for k in ky:
       if len(aDict[k]) >= biggest:
           bgk.append(k)
            
    return bgk[0]
    
print(biggest_val(animals))

