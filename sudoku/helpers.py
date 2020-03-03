import numpy as np

# main function to solve the puzzle
def solvePuzzle (array):
    
    # find next zero in puzzle, if there is no zero that indicates the puzzle has been solved
    lis = findNextZero(array)
    if lis[2] == False:
        print(array)
        return True
    row = lis[0]
    column = lis[1]
    
    # backtracking algorithim, attempt a candidate number if the solution is feasible proceed
    # by calling the function call again and continue until a solution is found
    for n in range(1,10):
        array[row,column] = n
        if checkPuzzle(array):
            if solvePuzzle(array):
                return True
    array[row,column] = 0
    return False 

# finds the next zero in the puzzle grid and returns it to the puzzle solver
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

# make sure that the puzzle rows/columns/squares are okay to proceed with solving
def checkPuzzle (array):
    return (checkRows(array) & checkColumns(array) & checkSquares(array))

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





           
