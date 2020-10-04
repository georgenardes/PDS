import numpy as np
import matplotlib.pyplot as plt


w = np.arange(-1*np.pi, np.pi, np.pi/100)

X = 1 + 2 * np.cos(w)

Mod_X = np.abs(X)
Fase_X = np.angle(X)

plt.plot(Mod_X)
plt.plot(Fase_X)

plt.show()
