import numpy as np
from numpy import pi, cos, sin
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, subplot, xlabel, ylabel, title, grid, axis, figure, show
from scipy.signal import freqz
import scipy.signal as signal
import scipy.fftpack


sample_rate = 5000

# definindo a frequencia de corte
# tem que estar entre 0 e 0.5
fc = 0.014

# definindo o roll-off
# BW é a largura em samples da banda de transição
# Tem que estar em 0 e 0.5
BW = 0.5
# M = 4 / BW
M = 8

# constant K
K = 1

# -M/2 to M/2
i = np.arange(0, M, 1/sample_rate)

# 16-4
h_i = K * (sin(2*pi*fc*(i-M/2))/(i-M/2)) * (0.42 - 0.5*cos(2*pi*i/M) + 0.08*cos(4*pi*i/M))


###############
#   plot
subplot(2, 1, 1)
plt.plot(i, h_i, label="Windowed")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

yf = scipy.fftpack.fft(h_i)

subplot(2, 1, 2)
plot(i, yf, 'b')
plt.xlabel("Freq")
plt.ylabel("Magnitude")

grid()
show()
