'''
Created on October 5th 2023
@author: Vidhur Busannagari
Pledge: I pledge my honor that I have abided by the Stevens Honor System. - VB
CS115 - Lab 4
'''
def knapsack(capacity, items):
    '''
    Solve the 0/1 knapsack problem recursively, finding the maximum value within the given capacity; 
    returns a list [max_value, selected_items].
    '''
    if not items:
        return [0, []]

    weight, value = items[0]

    if weight > capacity:
        return knapsack(capacity, items[1:])

    without_first, without_items = knapsack(capacity, items[1:])
    with_first, with_items = knapsack(capacity - weight, items[1:])
    with_first += value

    if with_first > without_first:
        return [with_first, [items[0]] + with_items]
    else:   
        return [without_first, without_items]