# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(arg1, arg2, arg3):
    min_arg = min(min(arg1, arg2), arg3)
    return arg1 + arg2 + arg3 - min_arg

x = float(input("Введите первое число: "))
y = float(input("Введите второе число: "))
z = float(input("Введите третье число: "))
print(f"Сумма наибольших двух значений равна {my_func(x,y,z)}")
