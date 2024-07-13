# 0ld Camel's Sudoku

This is my version of Sudoku. My plan is to:
- Create a valide Sudoku board:
  - Create a valid filled Sudoku board
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