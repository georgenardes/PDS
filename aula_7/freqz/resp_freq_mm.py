from scipy.signal import freqz
import scipy.signal as signal
import numpy as np
from numpy import pi, sin, log10, zeros
from matplotlib.pyplot import plot, subplot, xlabel, ylabel, title, grid, axis, figure, show


# Variaveis
passo = pi / 1000
w = np.arange(0, pi, passo)
L = 8
Fs = 8000

num = sin(w * L / 2)
den = sin(w / 2)

temp = num/den

# Rad
X = (1 / L) * (abs(temp))

subplot(3, 1, 1)
plot(w, X)
xlabel('Frquência')
title('Frequêncua Rad')
grid()


# Hz
F_Hz = (w / pi) * (Fs / 2)
subplot(3, 1, 2)
plot(F_Hz, X)
xlabel('Frequência')
title('Frequência em Hz')
grid()


# Db
X_Db = 20 * log10(X)
subplot(3, 1, 3)
plot(F_Hz, X_Db)
ylabel('Atenuação DB')
xlabel('Frequência')
title('Frequência em Hz')
grid()

axis([0, 4000, -70, 0])

figure(2)

# Usando freqz para obter a resposta em frequencia
# num = [.25 .25 .25 .25];
num_ = zeros((1, L), dtype='float64')
num_[0, :] = 1 / L

den_ = float(1)

[w, h] = freqz(num_.T, den_, worN=Fs, fs=Fs)

plot(w, 20 * log10(abs(h)), 'b')

title('Magnitude da resposta em frequencia')
grid()

show()

