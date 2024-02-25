#
# life.py - Game of Life lab
#
# Name: Vidhur Busannagari
# Pledge: I pledge my honor that I have abided by the Stevens Honor System - VB
#

import random
import sys

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [createOneRow(width)] 
    return A

def printBoard( A ):
    """ this function prints the 2d list-of-lists
    A without spaces (using sys.stdout.write)
    """
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )

def diagonalize(width,height):
    """ creates an empty board and then modifies it
    so that it has a diagonal strip of "on" cells.
    """
    A = createBoard(width, height)
    
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
                    
    return A

def innerCells(w, h):
    """
    Generate a 2D array with all live cells (value 1), except for a one-cell-wide border of empty cells (value 0)
    around the edge of the 2D array.
    """
    board = createBoard(w, h)

    for row in range(1, h - 1):
        for col in range(1, w - 1):
            board[row][col] = 1

    return board

def randomCells(w,h):
    """
    Generates a 2D array with randomly assigned 1's and 0's, leaving the outer edge empty (all 0's).
    """
    board = createBoard(w,h)
    for row in range(1, h - 1):
        for col in range(1, w - 1):
            board[row][col] = random.choice([0, 1])
    
    return board

def copy(A):
    """
    Create a deep copy of the 2D array 'A' and will output an array that is the same as the input array
    """
    copy = []
    for r in range(len(A)):
        temp = []
        for c in range(len(A[r])):
            temp.append(A[r][c])
        copy.append(temp)
    return copy

def innerReverse(A):
    """
    Generates a new 2D array representing the next generation of Conway's Game of Life based on the input array A.
    The new generation is created within the inner cells of the input array, with the outer edge always set to 0.
    """
    height = len(A)
    width = len(A[0])
    newA = createBoard(width, height)
    for row in range(1, height - 1):
        for col in range(1, width - 1):
            newA[row][col] = 1 if A[row][col] == 0 else 0
    return newA

def next_life_generation(A):
    """
    Advances one generation of Conway's Game of Life within the inner cells of the input board while keeping the outer edge 0
    """
    new_generation = copy(A)
    height = len(new_generation)
    width = len(new_generation[0])
    for row in range(1, height - 1):
        for col in range(1, width - 1):
            neighbor_count = countNeighbors(row, col, A)
            
            if neighbor_count < 2 or neighbor_count > 3:
                new_generation[row][col] = 0
            elif neighbor_count == 3:
                new_generation[row][col] = 1
    return new_generation

def countNeighbors(row, col, board):
    """
    Count the number of live neighbors for a cell at position (row, col) in the given board.
    """
    count = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if not (i == row and j == col) and board[i][j] == 1:
                count += 1
    return count

