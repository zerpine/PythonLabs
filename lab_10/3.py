import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def curve_liss(a, b, delta, time):
    x = np.sin(a * time + delta)
    y = np.sin(b * time)
    return x, y

figure, axis = plt.subplots()
line, = axis.plot([], [], lw=2)


def init():
    axis.set_xlim(-1.5, 1.5)
    axis.set_ylim(-1.5, 1.5)
    return line,


def update(frame):
    a = 3
    b = frame
    delta = 0
    t = np.linspace(0, 2 * np.pi, 1000)
    x, y = curve_liss(a, b, delta, t)
    line.set_data(x, y)
    return line,

ani = FuncAnimation(figure, update, frames=np.linspace(0, 1, 100),
                    init_func=init, blit=True)

plt.title('Анимация вращения фигуры')
plt.show()