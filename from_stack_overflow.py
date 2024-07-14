# this code is from 
# https://stackoverflow.com/questions/45471152/how-to-create-a-sudoku-puzzle-in-python
# this is an amazing piece of code. It took me hours to understand
from random import sample
base  = 3
side  = base * base

# pattern for a baseline valid solution
# this function create a 3 x 3 matrix, which is a valid sudoku, amazing
def pattern(r,c): 
    return (base * (r % base ) + r // base + c) % side

# randomize rows, columns and numbers (of valid base pattern)
def shuffle(s): 
    return sample(s,len(s)) 

rBase = list(range(base))

row_indexes  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ]
col_indexes  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
print(row_indexes)
print(col_indexes)
# rows = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# cols = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# nums  = shuffle(range(1,base*base+1))
nums = list(range(1, 10))

# produce board using randomized baseline pattern
board = [ [nums[pattern(row, col)] for col in col_indexes] for row in row_indexes ]

# for line in board: print(line)


        

