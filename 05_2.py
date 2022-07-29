
# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

my_file = open('01.txt')
list = my_file.readlines()
print(f'В файле {len(list)} строк(и)')
for lines in list:
    line = lines.replace("\n", "")
    print(f"Строка {line} содержит {len(line.split())} слов(а) и {len(line)} символа(ов)")
my_file.close()
