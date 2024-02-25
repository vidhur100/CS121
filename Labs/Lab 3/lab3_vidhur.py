############################################################
# Name: Vidhur Busannagari
# Pledge: I pledge my honor that I have abided by the Stevens Honor System. - VB
# CS115 Lab 3
#  
############################################################

def change(amount, coins):
    '''
    function returns a non-negative integer indicating the minimum number of
    coins required to make up the given amount
    '''
    if amount == 0:
        return 0
    elif len(coins) == 0:
        return float("inf")
    elif coins[0] > amount:
        return change(amount, coins[1:]) 
    else:
        use_it = 1 + change(amount - coins[0], coins)
        lose_it = change(amount, coins[1:])
        return min(use_it, lose_it)
