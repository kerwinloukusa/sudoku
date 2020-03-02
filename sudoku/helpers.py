import numpy as np

def checkRows (array):
    for x in range(9):
        seen = set()
        row = array[x,:]
        for n in row:
            if n != 0:
                if n in seen:
                    return False
                else:
                    seen.add(n) 
    return True

def checkColumns (array):
    for x in range(9):
        seen = set()
        column = array[:,x]
        for n in column:
            if n != 0:
                if n in seen:
                    
                    return False
                else:
                    seen.add(n)    
    return True

def checkSquares(array):
    for row in range(3):
        for column in range(3):
            seen = set()
            square = array[(row*3):(row*3+3), (column*3):(column*3+3)].flatten()
            for n in square:
                if n != 0:
                    if n in seen:
                        return False
                    else:
                        seen.add(n)  
    return True


def checkPuzzle (array):
    return (checkRows(array) & checkColumns(array) & checkSquares(array))

def findNextZero (array):
    row = 0;
    column = 0;
    solved = False
    if len(np.where(array == 0)[0]) != 0:
        for x in range(9):
            for y in range(9):
                if array[x,y] == 0:
                    row = x
                    column = y 
                    solved = True
                    return [row, column, solved]
                
    else:
        return [row, column, solved]

# each new cell needs to be a new function call?!..
def solvePuzzle (array):
    lis = findNextZero(array)
    if lis[2] == False:
        print(array)
        return True
    row = lis[0]
    column = lis[1]
    for n in range(1,10):
        array[row,column] = n
        if checkPuzzle(array):
            if solvePuzzle(array):
                return True
    array[row,column] = 0
    return False            
