import poke_holes

matrix = poke_holes.poking()
print('My matrix')
for row in matrix:
    print(row)

def row_valid(matrix, row, number):
    if number in matrix[row]:
        return False
    return True

def column_valid(matrix, column, number):
    for row in range(9):
        if matrix[row][column] == number:
            return False
    return True

def box_valid(matrix, row, column, number):
    left = column // 3 * 3
    top = row // 3 * 3
    for r in range(3):
        for c in range(3):
            if matrix[top + r][left + c] == number:
                return False
    return True

def valid(matrix, row, column):
    for number in range(1, 10):
        if row_valid(matrix, row, number) and column_valid(matrix, column, number) and box_valid(matrix, row, column, number):
            matrix[row][column] = number
            return number
            break
        else:
            continue


def solve(matrix):
    for row in range(9):
        for column in range(9):
            if matrix[row][column] == 0:
                matrix[row][column] = valid(matrix, row, column)
            else:
                continue


solve(matrix)

print('Solved')
for row in matrix:
    print(row)