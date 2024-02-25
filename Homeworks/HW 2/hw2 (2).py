'''
Created on September 26th 2023
@author: Vidhur Busannagari and Hemang Shankar
Pledge: I pledge my honor that I have abided by the Stevens Honor System. - VB & HS
CS115 - Hw 2
'''

import sys
from functools import reduce
# Be sure to submit hw2.py. Remove the '_template' from the file name.
# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)
# Leave the following lists in place.
scrabbleScores = \
[ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]
Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
'spam', 'spammy', 'zzyzva']

Dictionary = ["a", "am", "at", "apple", "bat", "bar", "babble", "can", "foo", "spam", "spammy", "zzyzva"]
scrabbleScores = [ ["a", 1], ["b", 3], ["c", 3], ["d", 2], ["e", 1],
["f", 4], ["g", 2], ["h", 4], ["i", 1], ["j", 8], ["k", 5], ["l", 1],
["m", 3], ["n", 1], ["o", 1], ["p", 3], ["q", 10], ["r", 1], ["s", 1],
["t", 1], ["u", 1], ["v", 4], ["w", 4], ["x", 8], ["y", 4], ["z", 10] ]

def letterScore(letter, scorelist):
    '''
    input is a single letter string called letter and a list where each element is a list 
    [character, value] where character is a letter and value is a number associated with that
    letter and returns a single number, namely the value associated with the given letter.
    '''
    return scorelist[0][1] if scorelist[0][0] == letter else letterScore(letter, scorelist[1:])

def wordScore(S, scorelist):
    '''
    takes an input string S and a scorelist, which will have only lowercase letters, 
    and should return as output the scrabble score of that string
    '''
    return 0 if not S else letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)

def scoreList(Rack):
    '''
    takes input a Rack which is a list of lower-case letters and returns a list of all of the 
    words in the global Dictionary that can be made from those letters and the score for each one.
    '''
    def checker(W, newRack):
        '''
        takes input W which is a word and newRack which is a copy of Rack and returns if the word
        can be made based on the rack
        '''
        def removeFromRack(char, rack_copy):
            '''
            takes an input char which is a letter and rack_copy which is a copy of rack and removes
            the letter from rack to ensure that when checking for a work the number of times a letter
            is used is considerd
            '''
            def remover(C, RC):
                '''
                takes an input C which is a letter and RC which is a copy of rack and is a helper 
                function to remove the letter from rack
                '''
                if not RC:
                    return []
                else:
                    if RC[0] == C:
                        return RC[1:]
                    return [RC[0]] + remover(C, RC[1:])
            return remover(char, rack_copy) if char in rack_copy else None
        
        def canFormWord(word, rack_copy):
            '''
            is a helper funciton and takes input word and rack_copy and returns if the word if the can be 
            made based on the rack
            '''
            if not word:
                return True
            char = word[0]
            newRack_copy = removeFromRack(char, rack_copy)
            if newRack_copy is not None:
                return canFormWord(word[1:], newRack_copy)
            return False
        return canFormWord(W, list(newRack))

    newDict = list(filter(lambda x: checker(x, list(Rack)), list(Dictionary)))
    return list(map(lambda W: [W, wordScore(W, scrabbleScores)], newDict))

def bestWord(Rack):
    '''
    takes as input a Rack and returns a list with two elements: the
    highest possible scoring word from that Rack followed by its score.
    '''
    return ["", 0] if not scoreList(Rack) else reduce(lambda x, y: x if x[1] > y[1] else y, scoreList(Rack))