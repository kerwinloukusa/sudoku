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
                return (True, array)
    array[row,column] = 0
    return (False, array) 

# finds the next zero in the puzzle grid and returns it to the puzzle solver
def findNextZero (array):
    row = 0;
    column = 0;
    if len(np.where(array == 0)[0]) != 0:
        for x in range(9):
            for y in range(9):
                if array[x,y] == 0:
                    row = x
                    column = y 
                    return [row, column, True]
                
    else:
        return [row, column, False]

# iterate through puzzle and make sure each row, column, and 3x3 box has no duplicates
def checkPuzzle(array):
    s = set()
    for x in range(0,len(array)):
        for y in range(0,len(array)):
            if array[x,y] == 0:
                continue
            row_str = "row_" + str(x) + "_val_" + str(array[x][y])
            col_str = "col_" + str(y) + "_val_" + str(array[x][y])
            mat_str = "mat_" + str(x//3)+ "_" + str(y//3) + "_val_" + str(array[x][y])
            if row_str not in s and col_str not in s and mat_str not in s:
                s.add(row_str)
                s.add(col_str)
                s.add(mat_str)
            else:
                return False

    return True





           
