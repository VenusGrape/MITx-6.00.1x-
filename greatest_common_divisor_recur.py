#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 10:07:12 2017

@author: adriana

The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,

gcd(2, 12) = 2

gcd(6, 12) = 6

gcd(9, 12) = 3

gcd(17, 12) = 1

A clever mathematical trick (due to Euclid) makes it easy to find greatest common divisors. Suppose that a and b are two positive integers:

If b = 0, then the answer is a

Otherwise, gcd(a, b) is the same as gcd(b, a % b)

See this website for an example of Euclid's algorithm being used to find the gcd.

Write a function gcdRecur(a, b) that implements this idea recursively. This function takes in two positive integers and returns one integer.

"""
def gcdRecur(a, b):
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)
