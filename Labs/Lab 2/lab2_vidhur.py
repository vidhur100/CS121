############################################################
# Name: Vidhur Busannagari
# Pledge: I pledge my honor that I have abided by the Stevens Honor System. - VB
# CS115 Lab 2
#  
############################################################

'''Outputs the dot product of the lists L and K'''
def dot(L, K):
    if L == [] and K != [] or K == [] and L != []:
        return -1

    if not L or not K:
        return 0.0
    else:
        return L[0] * K[0] + dot(L[1:], K[1:])

'''Takes a string S as input and should return a list of the characters in that string'''
def explode(S):
    if S == '':
        return []
    else:
        return [S[0]] + explode(S[1:])
    
'''Takes in an element e and a sequence L and returns the index at which e is first found in L'''
def ind(e, L):
    if not L or L[0] == e:
        return 0
    else:
        return 1 + ind(e, L[1:])

'''Takes in an element e and a list L and return another list that is identical to L except that all elements identical to e have been removed'''
def removeAll(e, L):
    if not L:
        return []
    else:
        if L[0] == e:
            return removeAll(e, L[1:])  
        else:
            return [L[0]] + removeAll(e, L[1:])  

'''Returns a new list that contains all of the elements that are even'''
def myFilter(f, L):
    if not L:
        return []
    else:
        if f(L[0]):
            return [L[0]] + myFilter(f, L[1:])
        else:
            return myFilter(f, L[1:])

'''Takes as input a list of elements where some of those elements may be lists
themselves and returns the reversal of the list where, additionally, any element that is
a list is also reversed'''
def deepReverse(L):
    if not L:
        return []
    else:
        if isinstance(L[0], list):
            return deepReverse(L[1:]) + [deepReverse(L[0])]
            
        else:
            return deepReverse(L[1:]) + [L[0]]




            
    
