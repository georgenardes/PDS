from scipy.signal import freqz
import scipy.signal as signal
import numpy as np
from numpy import pi, sin, log10, zeros, exp
from matplotlib.pyplot import plot, subplot, xlabel, ylabel, title, grid, axis, figure, show


# usando freqz
# A
num = [3, -3.2]
den = [1, -1.4, 0.45]
w, h = freqz(num, den)
subplot(3, 1, 1)
plot(w, 20 * log10(abs(h)), 'b')
grid()

# B
num = [1, 0]
den = [1, -2.1, 1.08]
w, h = freqz(num, den)
subplot(3, 1, 2)
plot(w, 20 * log10(abs(h)), 'g')
grid()

# C
num = [1, 0.9]
den = [1, 1, 0.41]
w, h = freqz(num, den)
subplot(3, 1, 3)
plot(w, 20 * log10(abs(h)), 'r')
grid()

# modo manual
figure(2)

# A
w = np.arange(0, pi, pi/1000)
num_m = 3 * (1*exp(-1j*w) - 1.2)
den_m = (exp(-1j*w) - 0.5) * (exp(-1j*w) - 0.9)
subplot(3, 1, 1)
plot(w, 20 * log10(abs(num_m/den_m)), 'b')
grid()

# B
num_m = exp(-1j*w)
den_m = (exp(-1j*w) - 0.9) * (exp(-1j*w) - 1.2)
subplot(3, 1, 2)
plot(w, 20 * log10(abs(num_m/den_m)), 'g')
grid()

# C
num_m = (exp(-1j*w) + 0.9)
den_m = exp(-2j*w) + exp(-1j*w) + 0.41
subplot(3, 1, 3)
plot(w, 20 * log10(abs(num_m/den_m)), 'r')
grid()


show()
