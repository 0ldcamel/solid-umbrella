def main():
    pass

def check_rows(matrix):
    for row in range(9):
        if sum(matrix[row]) != 45:
            return False
    return True

def check_columns(matrix):
    for column in range(9):
        total = 0
        for row in range(9):
            total += matrix[row][column]
        if total != 45:
            return False
    return True

def check_box(matrix, row, column):
    left = column // 3 * 3
    top = row // 3 * 3
    total = 0
    for r in range(3):
        for c in range(3):
            total += matrix[top + r][left + c]
    if total != 45:
        return False
    return True

def check_boxes(matrix):
    for row in range(9):
        for column in range(9):
            if not check_box(matrix, row, column):
                return False
        return True

def check_matrix(matrix):
    return check_boxes(matrix) and check_columns(matrix) and check_rows(matrix)

if __name__ == '__main__':
    main()
