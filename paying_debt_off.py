#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 15:23:03 2017

@author: venusgrape

Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly 
payment required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, 
print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print

Remaining balance: 813.41
instead of
Remaining balance: 813.4141998135 
So your program only prints out one thing: the remaining balance at the end of the year in the format:
Remaining balance: 4784.0

A summary of the required math is found below:

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)


"""

def pay_debt(b, air, mmpr):
    mir = air / 12
    mmp = mmpr * b
    mub = b - mmp
    updated_balance = mub + mir * mub
    return updated_balance
    
def show_balance(b, air, mmpr, month):
    if month == 0:
        return b
    else:
        while month > 0:
            b = pay_debt(b, air, mmpr)
            month -= 1
        return "{0:.2f}".format(b)
        
print(show_balance(5000, 0.18, 0.02, 12))



