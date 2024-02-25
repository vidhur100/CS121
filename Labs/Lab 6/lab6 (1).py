'''
Created on 10/19/2023
@author:   Vidhur Busannagari
Pledge:    I pledge my honor that I have abided by the Stevens Honor System - VB

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return not (n % 2 == 0)

# 42 base 10 = 101010 base 2

# For an odd base-10 number, the least-significant bit in its base-2 representation will always be 1, indicating that the number is not divisible by 2.
# For an even base-10 number, the least-significant bit in its base-2 representation will always be 0, indicating that the number is divisible by 2.

# the vlaue of the number gets halved if the least significant bit is eleiminated

# If N is an odd number, we append 1 to the base 2 representation
# If N is an even number, we append 0 to the base 2 representation
# This works because when the least significant bit is removed, the value is halved.
# When we add 0 or 1 to the end, we double the value and add 1 if it's odd

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    elif isOdd(n):
        return numToBinary(int(n /2)) + '1'
    else:
        return numToBinary(int(n/2)) + '0'

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    return 0 if s == "" else binaryToNum(s[:-1]) * 2  + int(s[-1]) 

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    return ('0' * 8 + numToBinary(binaryToNum(s) + 1))[-8:]

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n > 0:
        print(s)
        return count(increment(s), n-1)
    print(s)

# 59 base 10 = 2012 base 3
# 2*(3**3) + 0*(3**2) + 1*(3**1) + 2*(3**0) = 59

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    s = n % 3 
    return numToTernary(int(n/3)) + str(s)

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    return 0 if s == '' else ternaryToNum(s[:-1]) * 3 + int(s[-1])
