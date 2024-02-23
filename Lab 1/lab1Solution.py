############################################################
# Name: Vidhur Busannagari
# Pledge: I pledge my honor that I have abided by the Stevens Honor System. - VB
# CS115 Lab 1
#  
############################################################

from math import factorial
from functools import reduce

def inverse(x):
    # Finds a number's reciprocal 
    return 1/x

def e(n):
    # approximates the value e using a Taylor expansion
    
    def add(x, y):
        # returns x + y 
        return x + y
    
    arr = list(range(1, n+1))
    arr = map(factorial, arr)
    arr = map(inverse, arr)
    arr = reduce(add, arr)
    return arr+1
