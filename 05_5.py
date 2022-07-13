
# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

my_str = list(input('Введите числа через пробел: ').split(sep=' '))
with open('05.txt', 'w+') as file:
    for line in my_str:
        file.writelines(f'{line} ')

with open('05.txt', 'r') as file2:
    numbers = list(file2.readline().rstrip().split(sep=' '))
    numbers = [int(x) for x in numbers]
    print(f'Сумма чисел в файле равна {sum(numbers)}')
