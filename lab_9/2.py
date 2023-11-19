import numpy as np

x = np.array([2, 2, 2, 3, 3, 5])
elem = np.array([], dtype=int)
k = np.array([], dtype=int)

i = 0
while i < len(x):
    tempCnt = 1
    elem = np.append(elem, x[i])
    while i < len(x)-1 and x[i] == x[i+1]:
        tempCnt += 1
        i += 1
    k = np.append(k, tempCnt)
    i += 1

print(f'digits: {x}')
print(f'Answer: {elem}, {k}')