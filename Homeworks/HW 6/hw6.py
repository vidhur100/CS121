'''
Created on Nov 6 2023
@author:   Vidhur Busannagari
Pledge:    I pledge my honor that I have abided by the Stevens Honor System - VB

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return not (n % 2 == 0)

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
    return 0 if s == '' else binaryToNum(s[:-1]) * 2  + int(s[-1]) 
    
def counter(s, b):
    '''returns the number of bits which are repeated'''
    if not s:
        return 0
    elif s[0] != b:
        return 0
    else:
        return 1 + counter(s[1:], b)

def compress(S):
    '''This function accepts a binary string S with a length of 64 as input and produces a run-length encoded binary string as output'''
    def compress_helper(S, b):
        '''Compresses a string 'S' using run-length encoding with base 'b' and returns the compressed result'''
        if S == '':
            return ''
        else:
            n = counter(S, b)
            if(n > MAX_RUN_LENGTH):
                n = MAX_RUN_LENGTH
            r = 1 - int(b)
            return ((COMPRESSED_BLOCK_SIZE-len(numToBinary(n))) * '0' + numToBinary(n)) + compress_helper(S[n:], str(r))
    return compress_helper(S, '0')

# The maximum number of bits our compression algorithm could utilize to encode a 64-bit string or image is determined by the Compressed Block Size, which is calculated as 5 times 64, resulting in 320 bits.

def uncompress(C):
    ''' Uncompresses a binary compressed string using a recursive helper function, where COMPRESSED_BLOCK_SIZE 
    specifies the size of each compressed block, and returns the original uncompressed binary string.'''
    def uncompress_helper(C, b):
        '''uncompresses a compressed binary string using a specified compression factor'''
        if not C:
            return ''
        else:
            r = 1 - int(b)
            return (binaryToNum(C[:COMPRESSED_BLOCK_SIZE])* b) + uncompress_helper(C[COMPRESSED_BLOCK_SIZE:], str(r))
    return uncompress_helper(C, '0')


def compression(S):
    '''Computes the compression ratio between a compressed string and an uncompressed string'''
    return len(compress(S)) / len(S)

#Test Images Provided
print(compression("00011000"+"00111100"*3 +"01111110"+"11111111"+"00111100"+"00100100"))
print(compression("0"*8 + "01100110"*2 + "0"*8 + "00001000" + "01000010" + "01111110" + "0"*8))
print(compression("1"*9 + "0"*7 + "10000000"*2 + "1"*7 + "0" + "00000001"*2 + "1"*7 + "0"))

# We performed tests named Penguin, Smile, and Five. The compression ratios we obtained for these tests were 1.484375, 1.328125, and 1.015625, respectively.

'''
Professor Lai is Lai-ing. The existence of an algorithm that consistently reduces the size of a file is impossible. If such an algorithm were to exist, it 
would compress the file to 0 bits while preserving all the data. However, 0 bits cannot hold any information, making it evident that a compression algorithm that
always decreases the file size is not feasible.
'''