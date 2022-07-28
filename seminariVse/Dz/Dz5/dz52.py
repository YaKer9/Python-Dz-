# 2- Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Тот, кто берет последнюю конфету - проиграл.

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""


player_one = input('Enter you name player one: ')
player_two = input('Enter you name player two: ')
all_candy = input('Enter how many candys are on the table: ')
max_candy_step = input('Enter max candys by step: ')

whose_step = [1, -1]
first_step = input(f'определите кто будет ходить первым: \n1 - если {player_one}, \n2 - если {player_two}.\n')

if first_step == 1:
    print(f'ходит: {player_one}')
elif first_step==2:
    first_step = -1
    print(f'ходит: {player_two}')
step = 1
def who_step(first):
    if first_step == 1:
        print(f'ходит: {player_one}')
    elif first_step==2:
        first_step = -1
        print(f'ходит: {player_two}')

def how_much_candy():
    if all_candy > 1:
        first_step = first_step * (-1)


