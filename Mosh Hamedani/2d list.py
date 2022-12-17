matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Column 2, row 1, value is {matrix[0][1]}")
matrix[1][1] = 55
print(f"Here we've changed the matrix value in 2nd row column 2 2nd number 5 to {matrix[1][1]}")

matrix[1][1] = 5
for row in matrix:
    for item in row:
        print(item)