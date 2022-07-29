
# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.

# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Clothes:
    name: str

    @property
    def amount(self):
        if isinstance(self, Costum):
            return f'Для костюма требуется {"%.2f" % (self.height * 2 + 0.3)} м ткани'
        elif isinstance(self, Coat):
            return f'Для пальто требуется {"%.2f" % (self.size / 6.5 + 0.5)} м ткани'

class Coat(Clothes):
    size: int

    def __init__(self, size):
        self.size = size
        self.name = "Coat"

class Costum(Clothes):
    height: float

    def __init__(self, size):
        self.height = size
        self.name  = "Costum"

size = input("Введите размер пальто: ")
height = input("Введите рост для костюма в метрах (например, 1.63): ")
coat = Coat(float(size))
costum = Costum(float(height))
print(coat.amount)
print(costum.amount)
