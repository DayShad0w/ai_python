
# 7. Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import io
import functools
import json

my_list_headers = []
my_list_values = []
def count_av_profit(total, amount):
    return total + amount

with io.open('07.txt', encoding='utf-8') as file:
    for line in file.readlines():
        every_line = line.replace('\n', '').split(sep=' ')
        print(every_line)
        my_list_headers.append(every_line[0])
        profit = float(every_line[2]) - float(every_line[3])
        print(f'Выручка (убыток) составили: {profit}')
        my_list_values.append(profit)
    numbers = functools.reduce(count_av_profit, [0 if i < 0 else i for i in my_list_values])
    print(f'Средняя прибыль без учета убыточных составила {numbers/len(my_list_values)}. '
          f'В расчете учтены убыточные фирмы по количеству')
    headers = dict(zip(my_list_headers, my_list_values))
    dict_average = {'Average_profit': numbers/len(my_list_values)}
    firms = [headers, dict_average]
    print(firms)
    with open('07.json', 'w') as file_stream:
        json.dump(firms, file_stream)
        print('Сохранение данных выполнено')
