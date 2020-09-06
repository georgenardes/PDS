import numpy as np
import matplotlib.pyplot as plt

Fs = 8000
t1 = 1/1     # 1 ms
t2 = 1.5/1   # 1.5 ms

n1 = int(t1 * Fs)
n2 = int(t2 * Fs)

a0 = .5
a1 = .3
a2 = .2

with open('../voz_ruido_.pcm', 'rb') as f:
    buf = f.read()
    data_i = np.frombuffer(buf, dtype='int16')

entrada = data_i.reshape((data_i.shape[0], 1)).copy()
tam_entrada = len(entrada)
entrada[0][0] = 1
saida = np.zeros((tam_entrada, 1))
buf = np.zeros((n2, 1))

for i in range(len(entrada)):
    buf[0, 0] = entrada[i, 0]

    saida[i, 0] = a0 * buf[0, 0] + a1 * buf[n1-1, 0] + a2 * buf[n2-1, 0]

    # desloca
    buf[1:n2, 0] = buf[0:n2-1, 0]


with open('../voz_ruido_com_eco.pcm', 'wb') as f:
    for d in saida:
        f.write(d.astype(np.int16))

plt.stem(saida)
plt.title('Teste Delay')
plt.show()


