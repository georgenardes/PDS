import numpy as np
from numpy import pi, cos, sin, log10
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, subplot, xlabel, ylabel, title, grid, axis, figure, show
from scipy.signal import freqz


sample_rate = 8000

# numero de coefs
n = 320

# inicia vetor de coefs
wn = np.zeros(n, dtype=np.float64)

# taxa de aprendizado
mi = 0.0000000001       # 0,1 nano

# le sistema
coefs_name = "../coefs_pa.dat"
with open(coefs_name, 'r') as f:
    cof = f.read().replace("\n", "").split(",")
    cof.remove('')

    coefs = np.asarray(cof, dtype=np.float16)

# le ruido
read_path = "../ruido_branco.pcm"
with open(read_path, 'rb') as f:
    buf = f.read()
    data_i = np.frombuffer(buf, dtype='int16')
    data_len = len(data_i)
    xn = data_i[0:n]

    # aplica coefs sistema desconhecido
    dn = coefs.T * xn
    # dn = dn.astype(dtype='int16')p

erro = []
iteracoes = 400000
for i in range(iteracoes):

    # aplica coefs sistema aux
    yn = wn.T * xn

    # descobre erro
    en = dn - yn

    erro.append(sum(abs(en)))
    print(erro[i])

    # atualiza coefs
    wn = wn + 2 * mi * en * xn

print("adaptado", wn[0:2])
print("sistema", coefs[0:2])

# salva resultado do filtro
file_name = "../resultado_coefs.pcm"
with open(file_name, 'wb') as f:
    yn = np.convolve(wn, data_i, mode="same")
    for d in yn:
        f.write(d.astype(np.float16))

# salva coeficientes
coefs_name = "../coefs_adptados.dat"
with open(coefs_name, 'w') as f:
    for d in wn:
        f.write(str(d.astype(np.float16))+",\n")


# amostra de 100 ms
t = np.arange(0, data_len/sample_rate, 1 / sample_rate)

###############
#   plot
subplot(2, 1, 1)
plt.plot(np.arange(0, len(erro), 1), erro, "k-", label="Erro")
plt.legend()
plt.xlabel("Erro")
plt.ylabel("Mag")


print("calculating freqz")
[w1, h1] = freqz(coefs, worN=sample_rate, fs=1)
[w2, h2] = freqz(wn, worN=sample_rate, fs=1)

print("printing freqz")
subplot(2, 1, 2)
# plot(w1, 20 * log10(abs(h1)), label="freqz1")
# plot(w2, 20 * log10(abs(h2)), label="freqz2")
plot(w1, abs(h1), label="Desconhecido")
plot(w2, abs(h2), label="Adaptado")
plt.legend()
plt.xlabel("Freq")
plt.ylabel("Amplitude")

grid()
show()
