import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, subplot, xlabel, ylabel, title, grid, axis, figure, show
from scipy.signal import freqz


sample_rate = 8000
fc = 400
M = 0.02

# -M/2 to M/2
i = np.arange(-M/2, M/2, 1/sample_rate)

h_truncated = np.sin(2*np.pi*fc*i)/(i*np.pi)

# 0 to M
i = np.arange(0, M, 1/sample_rate)

# função sinc (low-pass filter)
w_black = 0.42 - 0.5 * np.cos(2*np.pi*i/M) - 0.08 * np.cos(4*np.pi*i/M)

w_windowed = w_black * h_truncated


###############
#   plot
subplot(2, 1, 1)
plt.plot(i, w_windowed, label="Windowed")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

[w, h] = freqz(w_windowed, worN=sample_rate, fs=1)

subplot(2, 1, 2)
plot(w, abs(h), 'b')
plt.xlabel("Freq")
plt.ylabel("Magnitude")

grid()
show()
