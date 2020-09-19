import numpy as np
import matplotlib.pyplot as plt


x = np.ones(6)
h = np.array([1, .5, .25, .125])

y = np.convolve(x, h)

length = len(x) + len(h) - 1

n = np.arange(0, length, 1)

plt.stem(n, y)
plt.show()
