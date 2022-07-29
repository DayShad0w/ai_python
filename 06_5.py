
# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title: str

    def draw(self):
        return "Запуск отрисовки"

class Pen(Stationery):

    def draw(self):
        return f"Тут ручка {self.title}"

class Pencil(Stationery):
    def draw(self):
        return f"Тут карандаш {self.title}"

class Handle(Stationery):
    def draw(self):
        return f"А тут маркер {self.title}"

pen    = Pen()
pencil = Pencil()
marker = Handle()

pen.title = "Parker"
pencil.title = "Derwent"
marker.title = "Molotow"

print(pen.draw())
print(pencil.draw())
print(marker.draw())