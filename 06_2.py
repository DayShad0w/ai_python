
# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
# Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    _road_length: float  # length зарезервировано системой
    _road_width: float

    def __init__(self, road_length, road_width):
        self._road_length = road_length
        self._road_width  = road_width

    def count_amount(self, mass, height):
        asf_amount = self._road_length*self._road_width*mass*height
        return asf_amount/1000

height   = float(input("Введите массу асфальта по нормам на 1 см полотна в кг: "))
mass     = float(input("Введите толщину покрытия в см: "))
r_length = float(input("Введите длину полотна в м: "))
r_width  = float(input("Введите ширину полотна в м: "))
asf_obj = Road(r_length, r_width)
total = asf_obj.count_amount(mass, height)
print(f"Для данных параметров требуется {total} тонн раствора")
