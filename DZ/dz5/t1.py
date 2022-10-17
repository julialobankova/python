# Создайте программу для игры с конфетами человек против человека.
# Условие задачи:
# На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

candies = 2021
candy_player1 = 0
candy_player2 = 0
player = randint(1, 2)
print('Начнем игру, первый ход определяется жеребьёвкой, за раз можно взять не более 28 конфет, погнали')

if player == 1:
    p1 = int(input('Первый игрок: '))
    candies = candies - p1
    candy_player1 += p1 
    player = 2
    print('1й игрок {} конфет, 2й игрок {} конфет, {} осталось конфет'.format(candy_player1, candy_player2, candies))
else:
    p2 = int(input('Второй игрок: '))
    candies = candies - p2
    candy_player2 += p2 
    player = 1
    print('1й игрок {} конфет, 2й игрок {} конфет, {} осталось конфет'.format(candy_player1, candy_player2, candies))

while candies >= 0:
    if player == 1:
        p1 = int(input('Первый игрок: '))
        candies = candies - p1
        candy_player1 += p1 
        print('1й игрок {} конфет, 2й игрок {} конфет, {} осталось конфет'.format(candy_player1, candy_player2, candies))
        player = 2
        if candies <= 0:
            print('Вы победили')
            break
    else:
        p2 = int(input('Второй игрок: '))
        candies = candies - p2
        candy_player2 += p2 
        print('1й игрок {} конфет, 2й игрок {} конфет, {} осталось конфет'.format(candy_player1, candy_player2, candies))
        player = 1 
        if candies <= 0:
            print('Вы победили!')
            break
