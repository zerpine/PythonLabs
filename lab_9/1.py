matrix = []

with open("matrix.txt") as file:
    for line in file:
        row = []
        for element in line.strip().split(','):
            row.append(int(element))
        matrix.append(row)

row = len(matrix)
column = len(matrix[0])

print('\n', 'Matrix:')
for i in range(row):
    print(*matrix[i])

sum = 0
for i in range(row):
    for j in range(column):
        sum += matrix[i][j]
print('\n')
print(f'Sum of elements of matrix: {sum}')

maxel = -(10**100)
minel = 10**100
for i in range(row):
    for j in range(column):
        if matrix[i][j] > maxel:
            maxel = matrix[i][j]
        elif matrix[i][j] < minel:
            minel = matrix[i][j]
print(f'Max element: {maxel}')
print(f'Min element: {minel}')