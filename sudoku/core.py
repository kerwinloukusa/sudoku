import numpy as np
import helpers as su
import pandas as pd
import time


start = time.time()

#read puzzle
df=pd.read_csv('puzzles/1.csv', sep=',',header=None)
df.style.hide_index()


#convert to numpy array and solve
array_puzzle = df.to_numpy()
su.solvePuzzle(array_puzzle)


end = time.time()
print(end - start)

