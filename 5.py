Задача: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами. Определить средние значения по всем строкам и столбцам матрицы. Результат оформить в виде матрицы из N + 1 строк и M + 1 столбцов.

import numpy as np
print("Введите число строк:")
n = int(input())
print("Введите число столбцов:")
m = int(input())
arr = np.random.sample((n,m))
arrav = arr.mean(axis=0)
arr1 =  np.vstack((arr, arrav))
print(arr1)
arrav1 = arr1.mean(axis=1)
arr1 = np.column_stack((arr1,arrav1))
print(arr1)
