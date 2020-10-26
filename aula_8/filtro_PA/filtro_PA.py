import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, subplot, xlabel, ylabel, title, grid, axis, figure, show
from scipy.signal import freqz
import scipy.signal as signal
import numpy as np
from numpy import pi, sin, log10, zeros

sample_rate = 8000
buffer = np.zeros(2)
saida = 0

Fc = 1000
Fs = sample_rate

# calcula FC
wc = 2 * np.pi * Fc

# F'
F1 = 2 * Fs

# coeficientes
a = F1/(F1+wc)
b = (wc-F1)/(F1+wc)

print(a)
print(b)

read_path = "../swip.pcm"
with open(read_path, 'rb') as f:
    buf = f.read()
    data_i = np.frombuffer(buf, dtype='int16')
    data_len = len(data_i)

    # replica do arquivo lido para salvar o resultado
    data_o = np.zeros_like(data_i)

    for i in range(data_len):
        buffer[0] = data_i[i]

    # y[n] = a * x[n]     - a * x[n-1]    - b * y[n-1]
        m = a * buffer[0] - a * buffer[1] - b * saida

        saida = m     # y-1

        data_o[i] = m

        # deslocamento
        buffer[1:2] = buffer[0:1]

# amostra de 100 ms
t = np.arange(0, data_len/sample_rate, 1 / sample_rate)

###############
#   plot
subplot(2, 1, 1)
plt.stem(t, data_i[: len(t)], "k-", "ko", "k-", label="Input")
plt.plot(t, data_o[: len(t)], label="Output")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")


###############
#   plot
# Usando freqz para obter a resposta em frequencia
num_ = [F1, -F1]
den_ = [F1+wc, wc-F1]

[w, h] = freqz(num_, den_, worN=Fs, fs=Fs)

subplot(2, 1, 2)
plot(w, 20 * log10(abs(h)), 'b')

title('Magnitude da resposta em frequencia')
grid()
show()

file_name = "../media_manual_result.pcm"
with open(file_name, 'wb') as f:
    for d in data_o:
        f.write(d)

