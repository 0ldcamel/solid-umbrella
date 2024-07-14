# 0ld Camel's Sudoku

This is my version of Sudoku. My plan is to:
- Create a valide Sudoku board:
  - Create a valid filled Sudoku board
  - Swap rows and columns within their groups
  - Poke holes to creat unsolved Sudoku board
- Solve Sudoku.
  - Start with single value
  - Then back track

## Create a valid Sudoku board:
### Create a valid filled Sudoku board:
My initial solution was quite mechanical. I started off with creating an empty list `matrix = []`. Then follow with a top row which is a list using `list(range(9))`. The result is:    
```
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```  
Then manually offset each two rows by 3. The results is a block of three top rows. They are appended to the `matrix`:   
```
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[4, 5, 6, 7, 8, 9, 1, 2, 3]  
[7, 8, 9, 1, 2, 3, 4, 5, 6]
```

The columns (and rows) are grouped in 3 groups of 3.
From the top block, columns in a group are rotated. In this case, 1 becomes 0, 2 becomes 1 and 0 becomes 3.   
```
[2, 3, 1, 5, 6, 4, 8, 9, 7]
[5, 6, 4, 8, 9, 7, 2, 3, 1]
[8, 9, 7, 2, 3, 1, 5, 6, 4]
```
These three rows are appended to the `matrix`. Repeating the same step, rotating the second group of row, to get the third group, which complete the 9 rows of the `matrix`. Here is my code:

```
def create_top_rows():
    seed_start = list(range(1, 10)) * 2
    top_rows = []
    for i in range(3):
        row = seed_start[i * 3: i * 3 + 9]
        top_rows.append(row)
    return top_rows

def shift_column(row, shift):
    new_row = []
    for column in range(9):
        left_most = column // 3 * 3
        local_index = (column + shift) % 3 + left_most
        new_row.append(row[local_index])
    return new_row

def create_matrix():
    top_rows = create_top_rows()
    matrix = []
    for shift in range(3):
        for i in range(3):
            row = shift_column(top_rows[i], shift)
            matrix.append(row)
    return matrix
```
Then I found this solution on [Stack Overflow](https://stackoverflow.com/questions/45471152/how-to-create-a-sudoku-puzzle-in-python). Is is so elegant, it took me hours to understand the code.
```
# base = 3, which is the size of each box
# side = base * base, which is the size of the game board
def pattern(row, columns): 
    return (base * (row % base) + row // base + column) % side
```
The code above creates a 9 x 9 board, with indexes from 0 to 8. If they were from 1 to 9, the board would be a valid Sudoku. This is the output:
```
[0, 1, 2, 3, 4, 5, 6, 7, 8]
[3, 4, 5, 6, 7, 8, 0, 1, 2]
[6, 7, 8, 0, 1, 2, 3, 4, 5]
[1, 2, 3, 4, 5, 6, 7, 8, 0]
[4, 5, 6, 7, 8, 0, 1, 2, 3]
[7, 8, 0, 1, 2, 3, 4, 5, 6]
[2, 3, 4, 5, 6, 7, 8, 0, 1]
[5, 6, 7, 8, 0, 1, 2, 3, 4]
[8, 0, 1, 2, 3, 4, 5, 6, 7]
```
It is so impressive, with just one liner. The author of this code didn't want the output to be a valid Sudoku board, but rather the indexes of a valid one. You'd see why later.

### Swapping rows and columns within their groups:
The next two lines of code is even more impressive. First, let's have a look at my code. As the swappings have to happen within their own group of 3. That means rows 0, 1 and 2 could be swap and the Sudoku board remains valid. Similarly, columns 3, 4 and 5 or (6, 7 and 8) or (0, 1, 2) can be swapped. So my code starts with given an index (for row or column), I need to get another index in the same group randomly.
```
def other_index(index):
    indexes = [0, 1, 2]
    indexes.remove(index % 3)
    other_index = index // 3 * 3 + random.choice(indexes)
    return other_index
```
Then I defined 2 more fucntions, to swap the rows and columns
```
def swap_rows(matrix, row):
    other_row = other_index(row)
    for column in range(9):
        matrix[row][column], matrix[other_row][column] = matrix[other_row][column], matrix[row][column]

def swap_columns(matrix, column):
    other_column = other_index(column)
    for row in range(9):
        matrix[row][column], matrix[row][other_column] = matrix[row][other_column], matrix[row][column]
```
To randomly call swap columns and rows, another function is created (uncecessarily), before the swap function can be defined (and called) for the whole matrix. The code below swaps the rows and columns 100 times.
```
def swap_what():
    return random.choice(["row", "column"])

SWAPS = 100

def swap_matrix(matrix):
    for _ in range(SWAPS):
        if swap_what() == 'row':
            row = random.randint(0, 8)
            swap_rows(matrix, row)
        elif swap_what() == 'column':
            column = random.randint(0, 8)
            swap_columns(matrix, column)
```
Now, the amazing code does the swapping in 2 magical lines:
```
def shuffle(s): 
    return sample(s,len(s)) 
rBase = range(base) 

row_indexes  = [ g * base + r for g in shuffle(rBase) for r in shuffle(rBase) ]
col_indexes  = [ g * base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
```
These two lines of code produce lists of indexes, randomly swap within their groups. Looking at the `row_indexes`, one can easily see `2, 0, 1` are in the same group, and so `7, 8, 6` and so on.
```
row_indexes = [2, 0, 1, 7, 8, 6, 3, 4, 5]
col_indexes = [7, 8, 6, 0, 2, 1, 5, 3, 4]
```