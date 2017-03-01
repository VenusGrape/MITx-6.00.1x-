#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 13:53:05 2017

@author: venusgrape

In this problem, you'll create a program that guesses a secret number!

The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). 
The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, 
the computer will guess the user's secret number!

Here is a transcript of an example session:

Please think of a number between 0 and 100!
Is your secret number 50?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 75?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 87?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 81?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 84?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 82?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 83?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
Game over. Your secret number was: 83

Important
Hint: Endpoints
** Your program should use bisection search. So think carefully what that means. What will the first guess always be? 
   How should you calculate subsequent guesses?
** Your initial endpoints should be 0 and 100. Do not optimize your subsequent endpoints by making them be the halfway point plus or minus 1. Rather, just make them be the halfway point.
Python Trick: Printing on the same line


Note: your program should use input to obtain the user's input! Be sure to handle the case when the user's input is not one of h, l, or c.

When the user enters something invalid, you should print out a message to the user explaining you did not understand their input. Then, 
you should re-ask the question, and prompt again for input. For example:

Is your secret number 91?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. y
Sorry, I did not understand your input.
Is your secret number 91?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c


"""

n = 100
epsilon = 0.01
low = 0
high = n
ans = (low + high)/2.0
#print(ans)
while ans**2 - n >= epsilon:
    print('Is your secret number', end = ' ')
    print(ans,end = ' ')
    print('?')
    
    letter = input("Enter 'h' to indicate the guess is too high. \
                   Enter 'l' to indicate the guess is too low. \
                   Enter 'c' to indicate I guessed correctly.")
    if letter == 'h':
        high = ans
        ans = (high + low)/2
    elif letter == 'l':
        low = ans
        ans = (high + low)/2
    elif letter == 'c':
         print('Game over, My answer is:',end = ' ')
         print(ans)
         break    
    else:
         print("Sorry, I did not understand your input.")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        