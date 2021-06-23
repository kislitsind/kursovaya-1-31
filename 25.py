Задача:Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами. Определить, сколько нулевых элементов содержится в каждом столбце и в каждой строке матрицы. Результат оформить в виде матрицы из N + 1 строк и M + 1 столбцов.

import numpy as np

N = 4
M = 5

V = np.random.randint(-10, 10, (N, M))
print("Матрица:\r\n{}\n".format(V))

bool = V == 0
col = np.sum(bool, axis=1)
V = np.insert(V, M, col, axis=1)
row = np.append(np.sum(bool, axis=0), 0)
V = np.insert(V, N, row, axis=0)
print("Новая матрица:\r\n{}\n".format(V))
