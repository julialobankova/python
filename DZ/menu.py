from my_def import writing_scv, read_date, find_date,  del_date

def menu():
    flag = True
    while flag:
        print("\n:Эллектронный дневник 10А   \n Выберите пункт меню для продолжения")
        while True:
            print("1: Добавление нового ученика")
            print("2: Поиск ученика по фамилии")
            print("3: Удаление ученика")
            print("4: Показать всех учеников")
            print("5: Выход")
            ch = int(input())
            if ch not in [1,2,3,4,5]:
                print('\nВыбран неверный пункт меню, попробуйте еще раз: ')
                continue
            if ch == 1:
                writing_scv()
                break
            elif ch == 2:
                find_date()
                break
            elif ch == 3:
                del_date()
                break
            elif ch == 4:
                read_date()
            else:
                flag = False
                break
if __name__  == '__main__':
    menu() 