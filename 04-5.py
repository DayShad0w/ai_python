
# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
from functools import reduce
import random
my_list = []

def my_odd(prev, x):
    return prev*x

for x in range(1, 5):
    my_list.append(random.randrange(100, 1001, 2))
print(f"Полученный список: {my_list}")
print(f"Произведение равно {reduce(my_odd, my_list)}")
