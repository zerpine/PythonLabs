import numpy as np

vector = np.array([0,1,2,0,0,4,0,6,9])

indexes = np.where(vector != 0)

print(f'\nIndexes of non-zero elements: {indexes}')
print(f'Elements under subscripts of non-zero elements: {vector[indexes]}\n')