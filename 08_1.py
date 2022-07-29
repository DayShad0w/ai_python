
# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать
# их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Data:

    @classmethod
    def extract_dmy(cls, data):
        my_list = data.split(sep='-')
        try:
            result_list = [int(item) for item in my_list]
        except Exception as e:
            print(f'Ошибка данных {e}')
        return result_list

    @staticmethod
    def check_dmy(data):
        my_list = Data.extract_dmy(data)
        my_dict = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        day = my_dict.get(int(my_list[1]))
        if day >= int(my_list[0]):
            print("Такая дата есть")
        else:
            print('Дата не верна')
data = input("Введите дату в формате dd-mm-yyyy: ")

Data.check_dmy(data)
Data.extract_dmy(data)
