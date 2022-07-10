
# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

from random import randint
import collections

def generator():
    for x in range(1, 11):
        yield(randint(1, 15))

my_list = generator()
print(f"Получен список элементов")

unique_el = collections.Counter(my_list)
print(unique_el)
print("Уникальные элементы:")
for key in unique_el:
    if unique_el[key] == 1:
        print(key, end=" ")
