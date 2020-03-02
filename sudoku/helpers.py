import numpy as np

def checkRows (arr):
    for x in range(9):
        seen = set()
        row = arr[x,:]
        for n in row:
            if n != 0:
                if n in seen:
                    return False
                else:
                    seen.add(n) 
    return True

def checkColumns (arr):
    for x in range(9):
        seen = set()
        column = arr[:,x]
        for n in column:
            if n != 0:
                if n in seen:
                    
                    return False
                else:
                    seen.add(n)    
    return True

def checkSquares(arr):
    for row in range(3):
        for column in range(3):
            seen = set()
            square = arr[(row*3):(row*3+3), (column*3):(column*3+3)].flatten()
            for n in square:
                if n != 0:
                    if n in seen:
                        return False
                    else:
                        seen.add(n)  
    return True

def checkPuzzle (arr):
    return (checkRows(arr) & checkColumns(arr) & checkSquares(arr))

def solvePuzzle (array, count):
    if len(np.where(array == 0)[0]) != 0:
            for x in range(9):
                row = array[x,:].flatten()
                for n in range(9):
                    #print (array)
                    if row[n] == 0:
                        for y in range(1,10):
                            array[x,n] = y
                            if checkPuzzle(array):
                                solvePuzzle (array,(count+1))
    else:
        print(array)