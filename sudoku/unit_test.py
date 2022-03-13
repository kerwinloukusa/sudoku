import numpy as np
from helpers import *
import pandas as pd

#import data
df=pd.read_csv('puzzles/1.csv', sep=',',header=None)
df.style.hide_index()
good_puzzle = df.to_numpy()

df=pd.read_csv('puzzles/2.csv', sep=',',header=None)
df.style.hide_index()
bad_puzzle = df.to_numpy()

#run test
def test_answer():
    assert checkPuzzle(good_puzzle) == True, "should be "

def test_answer2():
    assert checkPuzzle(bad_puzzle) == False, "should be "

def test_nextZero():
    assert findNextZero(good_puzzle) == [0,1,True], "should be"

def test_nextZero2():
    assert findNextZero(bad_puzzle) == [1,0,True], "should be"


def test_nextZero3():
    assert findNextZero(bad_puzzle) == [1,0,True], "should be"



