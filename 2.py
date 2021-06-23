Задача: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами. Найти наибольшее значение среди средних значений для каждой строки матрицы.

import numpy as np
print("Введите число строк:")
n = int(input())
print("Введите число столбцов:")
m = int(input())
arr = np.random.randint(10,20,(n,m))
arrav=arr.mean(axis=1)
print(arrav)
arrmax = arrav.max()
print(arrmax)
