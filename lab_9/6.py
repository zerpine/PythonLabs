import numpy as np

a = np.arange(16).reshape(4, 4)
print(f'\nmatrix: \n{a}\n')

a[[1, 3]] = a[[3, 1]]
print(f'New matrix: \n{a}\n')