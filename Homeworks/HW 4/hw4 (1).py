'''
Created on 10/24/2023
@author:   Vidhur Busannagari
Pledge:    I pledge my honor that I have abided by the Stevens Honor System - VB

CS115 - HW 4
'''

def pascal_row(r):
    '''Returns a list of elements found in the row corresponding to the given single integer.'''
    def helper(lst):
        '''Generates a new list containing the sum of adjacent elements from the input list.'''
        if len(lst) == 1:
            return [1]
        return [lst[0]+lst[1]] + helper(lst[1:])
    
    if r == 0:
        return [1]
    return [1] + helper(pascal_row(r-1))

def pascal_triangle(n):
    '''
    When provided with a single integer, this function generates a list of lists. Each inner list 
    contains the values from the rows starting from the first row up to and including the nth row.
    '''
    if n < 0:
        return []
    return pascal_triangle(n-1) + [pascal_row(n)]

def test_pascal_row():
    '''tests the function pascal_row'''
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1, 1]
    assert pascal_row(4) == [1, 4, 6, 4, 1]
    assert pascal_row(5) == [1, 5, 10, 10, 5, 1]

def test_pascal_triangle():
    '''tests the function pascal_triangle'''
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(1) == [[1], [1, 1]]
    assert pascal_triangle(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]