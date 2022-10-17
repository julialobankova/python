
#Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint
from fun import info
from fun import botinfo
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
    info(candy_player1, candy_player2,candies)
else:
    p2 = randint(1, 29)
    candies = candies - p2
    candy_player2 += p2 
    player = 1
    botinfo(p2)
    info(candy_player1, candy_player2,candies)

while candies >= 0:
    if player == 1:
        p1 = int(input('Первый игрок: '))
        candies = candies - p1
        candy_player1 += p1 
        info(candy_player1, candy_player2,candies)
        player = 2
        if candies <= 0:
            print('Победил первый игрок')
            break
    else:
        p2 = randint(1, 29)
        candies = candies - p2
        candy_player2 += p2
        botinfo(p2)
        info(candy_player1, candy_player2,candies)
        player = 1 
        if candies <= 0:
            print('Победил второй игрок!')
            break


