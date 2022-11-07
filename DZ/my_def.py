file = 'Namebook.csv'

def writing_scv():
    id = input('Введите ID ученика: ')
    if not id.isdigit():
        print("Ошибка! ID вводить цифрами")
        return
    surname = input('Введите фамилию ученика: ')
    if not surname.isalpha():
        print("Ошибка! Фамилию вводить буквами")
        return
    name = input('Введите имя уеника: ')
    if not name.isalpha():
        print("Ошибка! Имя вводить буквами")
        return
    age = input('Введите дату рождения ученика в формате (dd/mm/yyyy): ')
    av_mark = input('Введите средний бал ученика: ')
    description = input('Введите описание: ')
    file = 'Namebook.csv'
    with open(file, 'a', encoding='utf-8') as my_f:
        my_f.write(f"{id} {surname} {name} {age} {av_mark} {description}\n")


def read_date():
    with open(file, 'r', encoding='utf-8') as my_f:
        print(my_f.read())



def find_date():
    sn = input("Ввeдите ID ученика, которого нужно найти :  ")
    file = 'Namebook.csv'
    with open(file, 'r', encoding='utf-8') as my_f:
        for line in my_f.readlines():
            if line.startswith(sn):
                print(line)

def del_date():
    sn = input("Ввeдите ID ученика, которого нужно удалить :  ")
    file = 'Namebook.csv'
    with open(file, 'r+', encoding='utf-8') as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if sn not in line:
                f.write(line)
        f.truncate()



