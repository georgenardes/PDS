import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, subplot, xlabel, ylabel, title, grid, axis, figure, show


sample_rate = 8000
fc = 400
M = 0.02

# para calcular os valores
i = np.arange(0, M, 1/sample_rate)
i2 = np.arange(-M/2, M/2, 1/sample_rate)

# função sinc (low-pass filter)
w_i = 0.42 - 0.5 * np.cos(2*np.pi*i/M) - 0.08 * np.cos(4*np.pi*i/M)
w_i_2 = np.sinc(i2)

###############
#   plot
subplot(2, 1, 1)
plt.plot(i, w_i, label="feito a mao")
plt.legend()

subplot(2, 1, 2)
plt.plot(i2, w_i_2, label="sinc do python")
plt.legend()

grid()
show()
