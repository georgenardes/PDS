import numpy as np
import matplotlib.pyplot as plt

a = .5

w = np.arange(-1*np.pi, np.pi, np.pi/100)

Num = 1
Den = 1 - a * np.exp(-1j*w)
X = Num / Den

Mod_X = np.abs(X)
Fase_X = np.angle(X)

plt.plot(Mod_X)
plt.plot(Fase_X)

plt.show()
