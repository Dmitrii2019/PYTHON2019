#__author__ = 'Гродзинский Дмитрий Александрович'# Задача-1:
import random
# == Лото ==
# Правила игры в лото.
# Игра ведется с помощью специальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
def card(player): # красиво показывает карточку
    if player == 'player1':
        print('--- Моя карточка ---')
        for itm in player1:
            print(itm)
        print('--------------------')
    elif player == 'player_com':
        print('Карточка компьютера-')
        for itm in player_com:
            print(itm)
        print('--------------------')
def generator(player):
    if player == 'player1':
        player1 = [[random.randint(1, 90) for j in range(5) ] for i in range(3)]
        return player1
    elif player == 'player_com':
        player_com = [[random.randint(1, 90) for j in range(5)] for i in range(3)]
        return player_com
number = [0,]
def barrel():
    num = random.randint(1, 90)
    if not num in number:
        number.append(num)
        return num
    else:
        barrel()
def com():
    for i, e in enumerate(player_com):
        if e != ['-', '-', '-', '-', '-']:
            for it, en in enumerate(e):
                if num == en:
                    player_com[i][it] = '-'
        else:
            return a
def player(action):
        if action == 'y':
            a = 0
            for i, e in enumerate(player1):
                if e != ['-','-','-','-','-']:
                    for it, en in enumerate(e):
                        if num == en:
                            player1[i][it] = '-'
                            a = 1
                else:
                    return 'Вы выграли!!!'
            return a
        elif action == 'n':
            a = 1
            for i, e in enumerate(player1):
                for it, en in enumerate(e):
                    if num == en:
                        a = 0
            return a
player1 = generator('player1')
player_com = generator('player_com')
turn = 89
while turn > 0:
    num = barrel()
    print(f'Новый бочонок: {num} (осталось {turn}) ')
    card('player1')
    card('player_com')
    turn -= 1
    action = input('Зачеркнуть цифру? (y/n):')
    if action != 'y' and action != 'n' or action == '' :
        print('Нужно ввести только y and n')
        turn +=1
        continue
    com()
    if player(action) == 0:
        break
print('Вы проиграли')

# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка.
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
# 	Если цифра есть на карточке - она зачеркивается и игра продолжается.
# 	Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
# 	Если цифра есть на карточке - игрок проигрывает и игра завершается.
# 	Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый закроет все числа на своей карточке.
# Пример одного хода:
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 11     - 14    87
#       16 49    55 77    88
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)
# Подсказка: каждый следующий случайный бочонок из мешка удобно получать
# с помощью функции-генератора.
# Подсказка: для работы с псевдослучайными числами удобно использовать
# модуль random: http://docs.python.org/3/library/random.html
