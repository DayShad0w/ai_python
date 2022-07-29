
# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_file = open('01.txt', 'a')
while True:
    str_input = input('Введите строку: ')
    if len(str_input) == 0:
        break
    my_file.write(f'{str_input}\n')

my_file.close()
