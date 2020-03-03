import numpy as np
import helpers as su
import pandas as pd
df=pd.read_csv('puzzles/2.csv', sep=',',header=None)
df.style.hide_index()

array_puzzle = df.to_numpy()
su.solvePuzzle(array_puzzle)