
# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.


class ZeroDiv(Exception):

    def __init__(self, text):
        self.text = text

first_num = int(input('Введите число:'))
second_num = int(input('Введите еще число:'))

if second_num == 0:
    raise ZeroDiv("В рамках стандартных арифметических операций деление на 0 не допускается")
else:
    print(first_num/second_num)
