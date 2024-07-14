matrix = []

for j in range(9):
    row = []
    row_values = (input("row: "))
    for i in range(9):
        row.append(int(row_values[i]))
    matrix.append(row)
    print(f'Row {j} complete')

for row in matrix:
    print(row)

