
# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# Используйте в нём формулу:: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

"""
Необходимые параметры:
hours - количество отработанных часов
hour_price - ставка часа
bonus - размер премии
"""
import sys

def salary(hours, hour_price, bonus):
    return float(hours) * float(hour_price) + float(bonus)

try:
    file, hours, hour_price, bonus = sys.argv
except:
    print("Недостаточно входных параметров для расчета. Для справки используйте команду help")
    hours = int(input("Введите количество отработанных часов: "))
    hour_price = int(input("Введите стоимость часа: "))
    bonus = int(input("Введите сумму премии: "))

print(f"Итоговая сумма равна {salary(hours, hour_price, bonus)}")