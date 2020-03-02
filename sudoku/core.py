import numpy as np
import helpers as su
import pandas as pd
df=pd.read_csv('puzzles/1.csv', sep=',',header=None)
df.style.hide_index()
arr = df.to_numpy()

#print(arr)
su.solvePuzzle(arr)