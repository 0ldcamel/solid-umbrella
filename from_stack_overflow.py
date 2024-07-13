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

rBase = range(base) 

rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ]
cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
nums  = shuffle(range(1,base*base+1))

# produce board using randomized baseline pattern
board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

# for line in board: print(line)

# my code from here
# matrix = []
# for r in range(9):
#     row = []
#     for c in range(9):
#         row.append(pattern(r, c))
#     matrix.append(row)

# for row in matrix:
#     print(row)
print(rows)
print(cols)
        

