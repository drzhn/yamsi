import math
import wave
import struct
import matplotlib.pyplot as plt
import numpy as np

# sox 53cbce472afa.mp3 -e signed-integer -r 44100 lost_children.wav remix 1,2


def local_maxima(a):
    ret = []
    for i in range(len(a)):
        if (np.r_[True, a[1:] > a[:-1]] & np.r_[a[:-1] > a[1:], True])[i] == True:
            ret.append(i)
    return ret


# nframes = 40000
fname =  "lost_children.wav" # "test.wav"
# framerate = 11025.0
wav = wave.open(fname, 'r')
(nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()
data = wav.readframes(nframes)
wav.close()
data = struct.unpack('{n}h'.format(n=nframes), data)
data = np.array(data)
window = 4096
freqs = np.fft.fftfreq(window)
x = []
y = []
max = 24450680.6205  # наибольшая амплитуда
ratio = 0.8  # частоты, с амплитудой, меньшей max*ratio не будем включать в график
steps = nframes // window
duration = nframes // framerate
print(duration,"s ",steps,"steps")
# nmaxima = 5 # сколько локальных максимумов будем включать
#
# for i in range(nframes // window):
#     w = np.fft.fft(data[i * window:(i + 1) * window])
#     # for f in freqs
#     # print(freqs.min(), freqs.max())
#     # (-0.5, 0.499975)
#     # Find the peak in the coefficients
#     mas = np.abs(w)
#     # print(abs(freqs[np.argmax(mas)]*framerate)) # Наибольшая частота
#     # maximas = local_maxima(mas)
#     # print(len(maximas))
#     for n in range(nmaxima):
#         imax = np.argmax(mas)
#         freq = freqs[imax]
#         freq_in_hertz = abs(freq * framerate)
#         #print(freq_in_hertz)
#         # 439.8975
#         x.append(i)
#         y.append(freq_in_hertz)
#         np.delete(mas, imax)
#     print(i/steps*100,"%")
#
# plt.figure(num=None, figsize=(24, 3), dpi=30)
#
# plt.xlabel('time')
# plt.ylabel('frequency')
# plt.title(fname)
# plt.grid(True)
#
# plt.plot(x, y, 'ro')
# plt.axis([0, nframes // window + 1, 0, 4000])
# # plt.show()
# plt.savefig("spectre.png")
#
# # plt.show()
