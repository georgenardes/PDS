import numpy as np
from numpy import pi, cos, sin, log10
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, subplot, xlabel, ylabel, title, grid, axis, figure, show
from scipy.signal import freqz


sample_rate = 8000

# numero de coefs
n = 160

# inicia vetor de coefs
wn = np.zeros(n, dtype=np.float64)

# taxa de aprendizado
mi = 0.00000001       # 0,1 nano

# le saida
read_path = "far_apcm.pcm"
with open(read_path, 'rb') as f:
    buf = f.read()
    data_out = np.frombuffer(buf, dtype='int16')
    data_len = len(data_out)
    far = data_out  # [0:n]

# le retorno
read_path = "near_apcm.pcm"
with open(read_path, 'rb') as f:
    buf = f.read()
    data_in = np.frombuffer(buf, dtype='int16')
    near = data_in  # [0:n]


data_o = []

# partes do sample
for j in range(data_len//n):

    print("next sample", data_len//n, j)

    iteracoes = 10000
    for i in range(iteracoes):

        # aplica coefs sistema aux
        estimativa_eco = wn.T * far[j*n: (j*n)+n]

        # descobre erro
        en = near[j*n: (j*n)+n] - estimativa_eco

        # atualiza coefs
        wn = wn + 2 * mi * en * far[j*n: (j*n)+n]

    data_o.append(en)

# salva resultado do filtro
file_name = "../resultado_coefs.pcm"
with open(file_name, 'wb') as f:
    data_o = np.asarray(data_o)

    for d in data_o:
        f.write(d.astype(np.int16))


# salva coeficientes
coefs_name = "../coefs_adptados.dat"
with open(coefs_name, 'w') as f:
    for d in wn:
        f.write(str(d.astype(np.float16))+",\n")


# amostra de 100 ms
t = np.arange(0, data_len/sample_rate, 1 / sample_rate)

###############
#   plot

print("calculating freqz")
[w2, h2] = freqz(wn, worN=sample_rate, fs=1)

print("printing freqz")
subplot(2, 1, 1)
# plot(w2, 20 * log10(abs(h2)), label="freqz2")
plot(w2, abs(h2), label="Adaptado")
plt.legend()
plt.xlabel("Freq")
plt.ylabel("Amplitude")

grid()
show()
