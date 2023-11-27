import numpy as np
import matplotlib.pyplot as plt


def curve_liss(a, b, delta, t):
    x = np.sin(a * t + delta)
    y = np.sin(b * t)
    return x, y

time = np.linspace(0, 2 * np.pi, 1000)

figure, axis = plt.subplots(2, 2, figsize=(10, 8))

axis[0, 0].plot(*curve_liss(3, 2, 0, time))
axis[0, 0].set_title('3:2')

axis[0, 1].plot(*curve_liss(3, 4, 0, time))
axis[0, 1].set_title('3:4')

axis[1, 0].plot(*curve_liss(5, 4, 0, time))
axis[1, 0].set_title('5:4')

axis[1, 1].plot(*curve_liss(5, 6, 0, time))
axis[1, 1].set_title('5:6')

plt.suptitle('Ряд Лисажу с разными соотношениями частот')
plt.show()