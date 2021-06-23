Задача: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами. Найти наименьший элемент столбца матрицы A, для которого сумма абсолютных значений элементов максимальна.

import numpy as np
print("Введите число строк:")
n = int(input())
print("Введите число столбцов:")
m = int(input())
arr = np.random.randint(10,20,(n,m))
arrt = np.transpose(arr)
arrabs = np.abs(arrt)
sums = np.sum(arrabs, axis=1)
max = np.argmax(sums)
m = np.min(arrt[max])
print(m)
