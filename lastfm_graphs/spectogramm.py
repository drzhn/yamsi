import math
import wave
import struct
import matplotlib.pyplot as plt
import numpy as np

# sox 53cbce472afa.mp3 -e signed-integer -r 44100 lost_children.wav remix 1,2


def local_maxima(a):
    maximas = []
    for i in range(len(a)):
        if (np.r_[True, a[1:] > a[:-1]] & np.r_[a[:-1] > a[1:], True])[i] == True:
            maximas.append(i)
    # Отсортируем максимумы
    ret = []
    max = 0
    max_index = 0
    max_i = 0
    while len(maximas) > 0:
        for i in range(len(maximas)):
            if a[maximas[i]] > max:
                max = a[maximas[i]]
                max_index = maximas[i]
                max_i = i
        ret.append(max_index)
        del maximas[max_i]
        max = 0
    return ret


window = 2048
freqs = np.fft.fftfreq(window)
# max = 32565224.1956  # наибольшая амплитуда
ratio = 0.8  # частоты, с амплитудой, меньшей max*ratio не будем включать в график
delta = 0.8 # допуск при нормализации для октавной системы
real = window // 2 # реальная часть спектра
seconds = 10

fname = "lost_children.wav"# "test.wav" "test.wav"
wav = wave.open(fname, 'r')
(nchannels, bytespersample, framerate, nframes, comptype, compname) = wav.getparams()
print(nchannels, bytespersample, framerate, nframes, comptype, compname)
steps = nframes // window
duration = nframes // framerate
print(duration,"s ",steps,"steps")
print(window/framerate, "seconds per window")
print(seconds, "seconds is", seconds*framerate//window,"steps")
data = wav.readframes(nframes)
wav.close()

data = struct.unpack('{n}h'.format(n=nframes), data)
data = np.array(data)


frqLabel = freqs*framerate
# print(frqLabel)
octave = []
for i in range(real):
    octave.append(12*np.log2(frqLabel[i]/27.5))
    # print(octave[i], frqLabel[i])
# print(len(octave), len(frqLabel))
X = []
Y = []


# w = np.fft.fft(data[1301 * window:(1301 + 1) * window])
# mas = np.abs(w[:real])
# flag = [0 for i in range(real)]
# maxima_x = []
# maxima_y = []
# locmax = local_maxima(mas)
# for i in range(10):
#     maxima_x.append(octave[locmax[i]])
#     maxima_y.append(np.abs(w)[:real][locmax[i]])
#     print(octave[locmax[i]])
# plt.plot(octave[:real],np.abs(w)[:real],'b')
# plt.stem(maxima_x,maxima_y, '-.')
# # plt.plot(0,1000000,"r.")
# plt.show()


# plt.plot(octave[:l],np.abs(w)[:l],'r')
# print(octave[np.argmax(np.abs(w)[:l])],frqLabel[np.argmax(np.abs(w)[:l])])
# plt.show()
# z = np.empty((89, seconds*framerate//window, 3), dtype=np.uint32)
# # max = 0

# counter = 0.0
nsteps = seconds*framerate//window
for i in range(nsteps):
    w = np.fft.fft(data[i * window:(i + 1) * window])
    mas = np.abs(w[:real])
    locmax = local_maxima(mas)
    print(i,"of",nsteps,"steps ")
    for n in range(20):
        plt.plot(i,octave[locmax[n]],".")
        # X.append(octave[locmax[n]])
        # Y.append(i)
    # counter = i/(nframes//window)*100
    # print(counter,"%")

plt.show()
#     for n in range(89):
#         max = 0
#         for k in range(l):
#             if np.modf(octave[k]) == k:
#                 if mas[k] > max:
#                     max = mas[k]
#         z[n][i][0] = np.uint32(max)
#         z[n][i][1] = np.uint32(max)
#         z[n][i][2] = np.uint32(max)
#
# # print(z)
# max = z[np.unravel_index(z.argmax(), z.shape)]
# print(max)
# print(z)

# print(z[max])
# for i in range(seconds*framerate//window):
#     for n in range(89):
#         for k in range(3):
#             z[n][i][k] = z[n][i][k]/max*255
# print(z)


# # plt.figure(num=None, figsize=(24, 6), dpi=30)
# plt.imshow(z, interpolation='nearest')
# # plt.savefig("spectre.png")
# plt.show()
