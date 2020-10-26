import numpy as np
import matplotlib.pyplot as plt


sample_rate = 8000
t = np.arange(-0.5, 0.5, 1/sample_rate)     # o passo deve ser um numero possivel de representar em bin
tlen = len(t)
t0 = int(tlen/2)
print(tlen)

###############
#   impulso
sig_imp = np.zeros((tlen, 1), dtype=np.int16)
sig_imp[t == t[t0]] = 1

with open(r'../sig_imp.pcm', 'wb') as f:
    for d in sig_imp:
        f.write(d)

###############
#   degrau unitario
sig_deg = np.zeros((tlen, 1), dtype=np.int16)
sig_deg[t > 0] = 1

with open(r'../sig_deg.pcm', 'wb') as f:
    for d in sig_deg:
        f.write(d)

###############
#   seno
f = 10
sig_sin = (np.sin(2*np.pi*t*f)*1000).astype(np.int16)

with open(r'../sig_sin.pcm', 'wb') as f:
    for d in sig_sin:
        f.write(d.astype(np.int16))

###############
#   exp
sig_exp = np.exp2(-t)

with open(r'../sig_exp.pcm', 'wb') as f:
    for d in sig_exp:
        f.write(d.astype(np.int16))

###############
#   plot
fig, axs = plt.subplots(4, 1)
axs[0].stem(t, sig_imp, "k-", "ko", "k-")
axs[1].stem(t, sig_deg, "k-", "ko", "k-")
axs[2].stem(t, sig_sin, "k-", "ko", "k-")
axs[3].stem(t, sig_exp, "k-", "ko", "k-")
plt.show()
