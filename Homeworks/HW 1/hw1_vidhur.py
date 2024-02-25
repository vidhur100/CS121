############################################################
# Name: Vidhur Busannagari
# Pledge: I pledge my honor that I have abided by the Stevens Honor System. - VB
# CS115 Homework 1
#  
############################################################
from functools import reduce

'''Returns the product of 2 inputs'''
def mult(x,y):
    return x * y

'''Takes a positive integer n and returns n!'''
def factorial(n):
    return reduce(mult, range(1, 1+n))

'''Returns the sum of 2 inputs'''
def add(x, y):
    return x + y

'''Takes a list as input and returns the mean'''
def mean(L):
    return (reduce(add, L)/len(L))
