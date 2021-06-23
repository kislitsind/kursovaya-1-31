Задача:Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами. Найти сумму элементов всей матрицы. Определить, какую долю в этой сумме составляет сумма элементов каждой строки. Результат оформить в виде матрицы из N строк и M+1 столбцов.

import numpy as np
print("Введите число строк:")
n = int(input())
print("Введите число столбцов:")
m = int(input())
arr = np.random.randint(1,20,(n,m))
arrsu = arr.sum()
print(arrsu)
arrsum = arr.sum(axis=1)
c = arrsu/arrsum
print(c)
c1 = np.transpose(c)
print(c1)
c2 = np.column_stack((arr,c1))
print(c2)
