# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
#
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    items: list

    def __init__(self):
        self.items = []
        for i in range(1,4):
            line = input(f"Введите {i}-ую линию матрицы через пробел, три символа:").split(sep=" ")
            self.items.append(line)

    def __str__(self):
        line = ""
        for i in self.items:
            line = line + f"{i} \n".replace("'", "")
        return line

    def __add__(self, other):
        lst = self.items
        for i in range(len(self.items)):
            for j in range(len(self.items[0])):
                lst[i][j] = int(self.items[i][j]) + int(other.items[i][j])
        for i in lst:
            print(i)


print("Сложение матриц возможно только при их одинаковой размерности")
print("Введите 3 матрицы 3х3 построчно")
matrix_1 = Matrix()
matrix_2 = Matrix()
print(matrix_1)
print(matrix_2)
print('Результат сложения двух матриц: ')
matrix_3 = matrix_1.__add__(matrix_2)