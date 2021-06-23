Задача: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами. Найти сумму элементов всей матрицы. Определить, какую долю в этой сумме составляет сумма элементов каждого столбца. Результат оформить в виде матрицы из N + 1 строк и M столбцов.

import numpy as np
print("Введите число строк:")
n = int(input())
print("Введите число столбцов:")
m = int(input())
arr = np.random.randint(1,20,(n,m))
arrsu = arr.sum()
print(arrsu)
arrsum = arr.sum(axis=0)
c = arrsu/arrsum
arr1 =  np.vstack((arr, c))
print(arr1)
