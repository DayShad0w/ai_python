
# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

import random
import time

class Car:
    speed: float
    color: str
    name: str
    is_police: bool

    def go(self):
        return "running"

    def stop(self):
        return "stopped"

    def turn(self, direction):
        return f"turning {direction}"

    def show_speed(self):
        return self.speed

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return "Превышение лимита скорости в 60 км"
        else:
            return self.speed

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return "Превышение лимита скорости в 40 км"
        else:
            return self.speed

class SportCar(Car):
    pass

class PoliceCar(Car):
    pass

town   = TownCar()
town.name = "TownCar"
work   = WorkCar()
work.name = "WorkCar"
police = PoliceCar()
police.name = "PoliceCar"
sport  = SportCar()
sport.name = "SportCar"

list_cars = [town, work, police, sport]
list_speed = [0, 30, 40, 50, 80]

while True:
    car = random.randint(0, 3)
    speed = random.randint(0, 4)
    print(f"Едет машина {list_cars[car].name}")
    list_cars[car].speed = list_speed[speed]
    print(f"Ее скорость {list_speed[speed]}")
    if list_speed[speed] == 0:
        print(list_cars[car].stop())
    else:
        print(list_cars[car].show_speed())
    time.sleep(2)
