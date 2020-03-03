# Sudoku Solver
A simple python sudoku solver using backtracking:

* puzzles are read using pandas/numpy from CSV
* output is also written to csv 
* run by opening core.py, adding puzzles to /puzzles in CSV format (sample puzzle available) and editing script to target your chosen CSV


### To Do
* add image processing features to allow users to input png/jpg or other picture format
* create some sort of gui or tool to overlay on top of puzzle
* update helper functions to improve efficency
  * clean up row/column/square function to process more efficently
  * create candidate number suggestor based upon set of row/column and square (should siginifiganly reduce number of recursion calls)
  
