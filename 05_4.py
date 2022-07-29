
# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
my_dict = {'One': 'Один',
           'Two': 'Два',
           'Three': 'Три',
           'Four': 'Четыре'
           }
new_file = open('04_1.txt', 'a')
with open('04.txt', encoding='utf-8') as file:
    for lines in file.readlines():
        line = lines[0:lines.find(' ')]
        print(lines.replace(line, my_dict.get(line)), file=new_file)
new_file.close()
print('Файл 04_1.txt сформирован')
