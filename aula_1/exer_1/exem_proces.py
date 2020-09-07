import numpy as np
import matplotlib.pyplot as plt


gain = 0.5
sample_rate = 8000

read_path = "../teste.pcm"
with open(read_path, 'rb') as f:
    buf = f.read()
    data_i = np.frombuffer(buf, dtype='int16')
    data_len = len(data_i)
    for i in range(data_len):
        print("pos", i, data_i[i])

    # replica do arquivo lido para salvar o resultado
    data_o = np.zeros_like(data_i)

    for i in range(data_len):
        data_o[i] = data_i[i] * gain

    t = np.arange(0, data_len/sample_rate, 1 / sample_rate)

    plt.plot(t, data_i[: len(t)], label="Input")
    plt.plot(t, data_o[: len(t)], label="Output")
    plt.legend()
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.show()

    ''' 
    fig, axs = plt.subplots(2, 1)
    axs[0].plot(t, data_i[: len(t)])
    axs[1].plot(t, data_o[: len(t)])
    plt.show()
    '''


with open(r'../result.pcm', 'wb') as f:
    for d in data_o:
        f.write(d)
