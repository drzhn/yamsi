# -*- coding: utf-8 -*-

from math import sqrt, log2, exp, fsum, log


class Glcm:
    _glcm = []
    X = []
    Y = []
    mX = 0.0
    mY = 0.0
    Dx = 0.0
    Dy = 0.0
    length = 0

    def __init__(self, mas, offset, quantization):
        self.length = quantization
        if offset < 1:
            raise ValueError
        # Заполняем нулями
        for i in range(quantization):
            self._glcm.append([])
            for j in range(quantization):
                self._glcm[-1].append(0)
        max_mas = max(mas[i][j] for i in range(len(mas)) for j in range(len(mas[i])))
        print("max:", max_mas)
        for i in range(len(mas)):
            for j in range(len(mas[i])):
                mas[i][j] = int(mas[i][j] / max_mas * quantization)
        print(mas)
        for i in range(len(mas) - offset):
            for j in range(len(mas[i])):
                self._glcm[mas[i][j] - 1][mas[i + 1][j] - 1] += 1
        # Нормируем матрицу
        sum_glcm = sum(self._glcm[i][j] for i in range(quantization) for j in range(quantization))
        print("sum glcm:", sum_glcm)
        for i in range(quantization):
            for j in range(quantization):
                self._glcm[i][j] = self._glcm[i][j] / sum_glcm
        # Вычислим мат. ожидание, диперсию, сигма
        for i in range(quantization):
            self.X.append(sum(self._glcm[i][j] for j in range(quantization)))
            self.Y.append(sum(self._glcm[j][i] for j in range(quantization)))
        self.mX = sum(i * self.X[i] for i in range(quantization))
        self.mY = sum(j * self.Y[j] for j in range(quantization))
        self.Dx = sum(i * i * self.X[i] for i in range(quantization)) - self.mX
        self.Dy = sum(j * j * self.Y[j] for j in range(quantization)) - self.mY

    def __str__(self):
        ret = ""
        for i in range(self.length):
            ret += "{0:>7} | ".format(str(self.X[i]))
            for j in range(self.length):
                ret += "{0:>7}, ".format(self._glcm[i][j])
            ret += "\n"
        ret += "_" * 100 + "\n"
        ret += "{0:>9} ".format("")
        for i in range(self.length):
            ret += "{0:>7}, ".format(self.Y[i])
        return ret

    def get_stat(self):
        print("X:", self.X)
        print("Y:", self.Y)
        print("mX:", self.mX)
        print("mY:", self.mY)
        print("Dx:", self.Dx)
        print("Dy:", self.Dy)

    def autc(self):
        return (fsum(
            i * j * self._glcm[i][j] for i in range(self.length) for j in
            range(self.length)) - self.mX * self.mY) / sqrt(
            self.Dx * self.Dy)

    def ent(self):
        return -1 * sum(
            self._glcm[i][j] * log2(self._glcm[i][j]) for i in range(self.length) for j in range(self.length) if
            self._glcm[i][j] != 0)

    def imc2(self):
        return sqrt(1 - exp(-2 * fsum(
            (self._glcm[i][j] * log(self._glcm[i][j] / (self.X[i] * self.Y[j])))
            for i in range(self.length) for j in range(self.length)
            if self._glcm[i][j] != 0 and self.X[i] != 0 and self.Y[j] != 0)))

    def ener(self):
        return sqrt(fsum(self._glcm[i][j] ** 2 for i in range(self.length) for j in range(self.length)))

    def cont(self):
        return sqrt(fsum(self._glcm[i][j] * (i - j) ** 2 for i in range(self.length) for j in range(self.length)))

    def diss(self):
        return sqrt(fsum(self._glcm[i][j] * abs(i - j) for i in range(self.length) for j in range(self.length)))

    def clsh(self):
        return sqrt(fsum(self._glcm[i][j] * (i + j - self.mX - self.mY) ** 3
                         for i in range(self.length) for j in range(self.length)))

    def clpr(self):
        return sqrt(fsum(self._glcm[i][j] * (i + j - self.mX - self.mY) ** 4
                         for i in range(self.length) for j in range(self.length)))
