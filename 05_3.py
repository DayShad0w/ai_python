
# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32

sum_of_salary = 0
count_lines = 0
with open('03.txt', encoding='utf-8') as file:
    print('Сотрудники с ЗП менее 20 000:')
    for lines in file.readlines():
        new_line = lines.replace("\n", "").split(sep=" ")
        if float(new_line[1]) < 20000:
            print(new_line[0])
        sum_of_salary += float(new_line[1])
        count_lines += 1
    print(f'Средняя ЗП: {"%.2f" % (sum_of_salary/count_lines)}')
