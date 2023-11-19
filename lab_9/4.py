import numpy as np

x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
max_value = -(10 ** 10)

i = 0
while i < len(x):
    while (i < len(x) - 1) and (x[i] == 0) and (x[i+1] > max_value):
        max_value = x[i + 1]
    i += 1

print(f'Vector: {x}')
print(f'Max value: {max_value}')