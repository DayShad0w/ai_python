
# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.
class Warehouse():
    name: str
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Items():
    colour: str
    name: str
    num_items: int
    place: Warehouse

    def __init__(self):
        name, colour = input('Введите наименование и цвет оборудования ').split()
        self.name = name;
        self.colour = colour
        num = ''
        while not (num.isdigit()):
            num = input('Укажите количество размещаемого оборудования: ')
        self.num_items = num

    def __str__(self):
        return f'Dev: {self.name}, color {self.colour} \n' \
               f'warehouse: {self.place} ---> amount {self.num_items}'

    def set_place(self, place):
        self.place = place

class Printer(Items):
    brand: str
    color_type: str

class Scanner(Items):
    dual: bool

warehouse = Warehouse("Main")
ware_list = []
dev_name = input('Введите данные для размещения: тип оборудования ')
if dev_name == 'Scanner':
    new_dev = Scanner()
    #по типу добавить заполнение доп атрибутов класса, присущих только этому классу
elif dev_name == 'Printer':
    new_dev = Printer()
else:
    print('Тип оборудования не найден. Проверьте вводимые данные и попробуйте снова')

new_dev.set_place(warehouse)

ware_list.append(new_dev)

for items in ware_list:
    print(items)
