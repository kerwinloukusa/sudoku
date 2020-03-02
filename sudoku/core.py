import numpy as np
import sudoku_functions as su
import pandas as pd
df=pd.read_csv('sudoko.csv', sep=',',header=None)
df.style.hide_index()
arr = df.to_numpy()

#print(arr)
su.solvePuzzle(arr,0)