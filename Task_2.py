# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint


human = "человек"
bot = "бот"
total = 50

isFirstUserStep = True

game_mode = int(input(f"Выберите режим игры: \n 1) {human} - {human} \n 2) {human} - {bot} \n"))

if game_mode == 1:
    while(total>0):
        user = 'первого' if isFirstUserStep else 'второго'
        takedCandies = int(input(f"Кол-во конф {user} игрока: "))
        if 0 < takedCandies <= 28:
            total = total - takedCandies
            print(f"Осталось {total} конфет.")
            isFirstUserStep = not isFirstUserStep
        else:
            print(f"Нельзя брать {takedCandies} конфет. Повторите ещё раз!")
        if (total <= 0):
            print(f"Теперь все конфеты {user} игрока")

elif game_mode == 2:
    while(total>0):
        isUserReady = False  # если игрок ввел больше 28 конф или меньше 0, то бот не будет ходить
        takedCandies = int(input(f"Кол-во конф игрока: "))
        if 0 < takedCandies <= 28:
            total = total - takedCandies
            print(f"Осталось {total} конфет.")
            isUserReady = True
            if (total <= 0):
                print(f"Теперь все конфеты игрока")
                break
        else:
            print(f"Нельзя брать {takedCandies} конфет. Повторите ещё раз!")

        if isUserReady:
            limit = 28
            if(total <= limit):
                botCandies = total
            elif(total <= 57):
                botCandies = total-(limit + 1)
            else:
                botCandies = randint(1,limit) 
            print(f"Бот забирает {botCandies}")
            total = total - botCandies
            print(f"Осталось {total} конфет.")
            if (total <= 0):
                print(f"Теперь все конфеты бота")





                




