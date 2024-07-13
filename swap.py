from create import create_matrix
import random

matrix = create_matrix()
SWAPS = 100

def swap_matrix(matrix):
    for _ in range(SWAPS):
        if swap_what() == 'row':
            row = random.randint(0, 8)
            swap_rows(matrix, row)
        elif swap_what() == 'column':
            column = random.randint(0, 8)
            swap_columns(matrix, column)

def swap_columns(matrix, column):
    other_column = other_index(column)
    for row in range(9):
        matrix[row][column], matrix[row][other_column] = matrix[row][other_column], matrix[row][column]


def other_index(index):
    indexes = [0, 1, 2]
    indexes.remove(index % 3)
    other_index = index // 3 * 3 + random.choice(indexes)
    return other_index

def swap_rows(matrix, row):
    other_row = other_index(row)
    for column in range(9):
        matrix[row][column], matrix[other_row][column] = matrix[other_row][column], matrix[row][column]

def swap_what():
    return random.choice(["row", "column"])
