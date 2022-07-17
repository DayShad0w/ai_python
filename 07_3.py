
# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству
# ячеек клетки (целое число). В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
# и целочисленное (с округлением до целого) деление клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества
# ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение
# количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как
# целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****...,
# где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.

class Cells:
    cell_anount: int
    def __init__(self, cell_amount):
        self.cell_amount = cell_amount

    def __add__(self, other, common):
        common.cell_amount = self.cell_amount + other.cell_amount
        return common.cell_amount

    def __sub__(self, other, common):
        common.cell_amount = self.cell_amount - other.cell_amount
        if common.cell_amount > 0:
            return common.cell_amount
        elif common.cell_amount < 0:
            return "Первая клетка меньше второй. Вычитание невозможно"
        else:
            return "Вычитание невозможно, клетки равны"

    def __mul__(self, other, common):
        common.cell_amount = self.cell_amount * other.cell_amount
        return common.cell_amount

    def __truediv__(self, other, common):
        if self.cell_amount>other.cell_amount:
            common.cell_amount = self.cell_amount // other.cell_amount
        else:
            common.cell_amount = other.cell_amount // self.cell_amount
        return common.cell_amount

    def make_order(self, amount, rows):
        line = ""
        row = amount//rows
        for i in range(row):
            for j in range(rows):
                line = line + "*"
            line = line + "\n"
        last = amount % rows
        for x in range(last):
            line = line + "*"
        return line

first_cell  = Cells(cell_amount=10)
second_cell = Cells(cell_amount=20)
common_cell = Cells(cell_amount=0)
print(f'First + second: {first_cell.__add__(second_cell, common_cell)}')
print(f'First min second {first_cell.__sub__(second_cell, common_cell)}')
print(f'Divide first by second: {first_cell.__truediv__(second_cell, common_cell)}')
print(f'Multiply first and second: {first_cell.__mul__(second_cell, common_cell)}')
another_cell = Cells(cell_amount=25)
print(another_cell.make_order(26, 4))
