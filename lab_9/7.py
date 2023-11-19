import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

with_out = iris[:, :-1]
unique = np.unique(with_out)

print(f'\nUnique values: \n{unique}\n')
print(f'Count of unique values: {len(unique)}\n')