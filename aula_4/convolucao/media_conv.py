import numpy as np
import matplotlib.pyplot as plt


# tamanho da média
k = 8
filtro = np.ones(k) / k
print(filtro)

# impulso unitario
imp_u = np.zeros(k)
imp_u[int(k/2)] = 1

y_conv = np.convolve(filtro, imp_u)

length = len(filtro) + len(imp_u) - 1
n = np.arange(0, length, 1)
plt.stem(n, y_conv)
plt.show()
