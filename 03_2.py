# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_params(**userparams):
    return userparams


print("Введите данные пользователя")
name = input("Введите имя пользователя: ")
surname = input("Введите фамилию пользователя: ")
town = input("Введите город проживания: ")
year_of_birth = input("Введите год рождения: ")
email = input("Введите адрес эл.почты: ")
phone = input("Введите номер телефона: ")
print(user_params(Name=name, Surname=surname, Town=town, Birth_year=year_of_birth, E_mail=email, Phone_number=phone))
