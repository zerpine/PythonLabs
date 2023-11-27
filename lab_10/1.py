import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

x_values = np.linspace(-1, 1, 400)

degrees = [1, 2, 3, 4, 5, 6, 7]

plt.figure(figsize=(10, 6))
plt.title("Полиномы Лежандра")

for n in degrees:
    y_values = legendre(n)(x_values)
    plt.plot(x_values, y_values, label=f'n = {n}')

plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

plt.xlabel('x')
plt.ylabel('P_n(x)')

plt.grid(True)
plt.show()