import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, subplot, xlabel, ylabel, title, grid, axis, figure, show


sample_rate = 8000
fc = 400
M = 0.02

# para calcular os valores
i = np.arange(0, M, 1/sample_rate)

# função sinc (low-pass filter)
w_i = 0.54 - 0.46 * np.cos(2*np.pi*i/M)

###############
#   plot
subplot(1, 1, 1)
plt.plot(i, w_i, label="Output")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
grid()
show()
