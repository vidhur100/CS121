############################################################
# Name: Vidhur Busannagari
# Pledge: I pledge my honor that I have abided by the Stevens Honor System - VB
# CS115 Lab 1
#
############################################################
def same(word):
    '''
    checks if first and last letter of an input string has the
    same char (not case sensitive)
    '''
    return word[-1].lower() == word[0].lower()
def consecutiveSum(x, y):
    '''
    finds the sum of consecutive
    integers between two numbers
    '''
    return ((x+y)/2) * (y-x-1)
