#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 06:50:07 2017

@author: venusgrape

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur 
in alphabetical order.For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then
your program should print Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart. If you've 
spent more than a few hours on this problem, we suggest that you move on to a 
different part of the course. If you have time, come back to this problem after 
you've had a break and cleared your head.

"""

s = input('Please enter a string: ')

substring = s[0]
longest = s[0]
for i in range(1,len(s)):
	if substring[-1] <= s[i]:
		substring += s[i]
	else :
		substring = s[i]
	if len(substring) > len(longest):
			longest = substring	
            
print(longest)