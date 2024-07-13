from swap import swap_matrix
from create import create_matrix
import random

HOLES = 40

def main():
    pass

def poking():
    matrix = create_matrix()
    swap_matrix(matrix)
    vector_list = list(range(81))
    for i in range(HOLES):
        number = random.choice(vector_list)
        row = number // 9
        column = number % 9
        vector_list.remove(number)
        matrix[row][column] = 0
    return matrix

# matrix = poking()
# for row in matrix:
#     print(row)

if __name__ == '__main__':
    main()