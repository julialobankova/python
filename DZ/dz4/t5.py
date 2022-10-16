# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

str_line = ''

file_1 = open('new1.txt', 'r')
file_2 = open('new2.txt', 'r')

while True:
    line1 = file_1.readline()
    line2 = file_2.readline()
    if not line2 or not line1:
        break

    str_line = line1[:-1] + '+ ' + line2
    with open('new3.txt', 'a', encoding='utf-8') as file_my:
        file_my.write(f'{str_line}\n')