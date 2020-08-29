import numpy as np
import matplotlib.pyplot as plt


sample_rate = 100
index = int(sample_rate/2)
t = np.arange(-index*0.125, index*0.125, 0.125)     # o passo deve ser um numero possivel de representar em bin


###############
#   impulso
sig_imp = np.zeros((sample_rate, 1))
sig_imp[t == 0] = 1


###############
#   degrau unitario
sig_deg = np.zeros((sample_rate, 1))
sig_deg[t > 0] = 1

###############
#   seno
sig_sin = np.sin(t)

###############
#   exp
sig_exp = np.exp2(t)

fig, axs = plt.subplots(4, 1)
axs[0].plot(t, sig_imp)
axs[1].plot(t, sig_deg)
axs[2].plot(t, sig_sin)
axs[3].plot(t, sig_exp)
plt.show()
