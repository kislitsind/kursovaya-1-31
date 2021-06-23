Задача:Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами. Разделить элементы матрицы на элемент матрицы с наибольшим значением.

import numpy as np
N = 4
M = 5
V = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}\n".format(V))
Max = V.max()
print(Max)
V = V / Max
print("Новая матрица:\r\n{}\n".format(V))

