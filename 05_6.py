
# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
import io
import functools
import re
my_list_headers = []
my_list_values = []

def my_sum(total, amount):
    try:
        return float(total) + float(amount)
    except:
        # кто-то не число, проверим кто
        if total.isdigit():
            return total
        elif amount.isdigit():
            return amount

with io.open('06.txt', encoding='utf-8') as file:
    for line in file.readlines():
        every_line = line.replace('\n', '').split(sep=' ')
        print(every_line)
        my_list_headers.append(every_line[0])
        del every_line[0]
        numbers = functools.reduce(my_sum, [re.sub('[\D]', '', i) for i in every_line])
        my_list_values.append(numbers)
    headers = dict(zip(my_list_headers, my_list_values))
    print('Результат обработки: ')
    print(headers)
