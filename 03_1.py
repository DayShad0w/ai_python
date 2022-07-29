# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division_func(arg1, arg2):
    try:
        return arg1 / arg2
    except ZeroDivisionError:
        return None
arg_1 = float(input("введите числитель: "))
arg_2 = float(input("Введите знаменатель: "))

print(f"Частное от деления равно {division_func(arg_1, arg_2)}")
