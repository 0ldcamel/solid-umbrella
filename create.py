def create_top_rows():
    seed_start = list(range(1, 10)) * 2
    top_rows = []
    for i in range(3):
        row = seed_start[i * 3: i * 3 + 9]
        top_rows.append(row)
    return 

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
            print(row)
            matrix.append(row)
    return matrix

matrix = create_matrix()
for row in matrix:
    print(row)