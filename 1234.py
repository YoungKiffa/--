import random


def create_matrix(rows, cols):
    matrix = [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]
    return matrix


rows = 3
cols = 4
matrix = create_matrix(rows, cols)
for row in matrix:
    print(row)

# def create_matrix(rows, cols): - Это объявление функции create_matrix, которая принимает два аргумента: rows (количество строк) и cols (количество столбцов).
# matrix = [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)] - В этой строке создается матрица при помощи list comprehension. Внешний цикл (для строк) проходит rows раз, а внутренний цикл (для столбцов) проходит cols раз. В каждой ячейке матрицы генерируется случайное число от 1 до 100 при помощи random.randint(1, 100).
# return matrix - Эта строка возвращает созданную матрицу после ее заполнения случайными числами.
# rows = 3 и cols = 4 - В этих строках определяются переменные rows и cols, задающие количество строк и столбцов матрицы, которые мы хотим создать.
# matrix = create_matrix(rows, cols) - Вызываем функцию create_matrix с указанным количеством строк и столбцов и сохраняем возвращенную матрицу в переменной matrix.
# for row in matrix: и print(row) - Эти строки позволяют вывести на экран все строки созданной матрицы. Каждая строка матрицы выводится отдельно.



