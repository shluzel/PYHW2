#На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
#Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
#Выведите минимальное количество монет, которые нужно перевернуть
from random import randint
N = int(input('Укажите количество монеток на столе '))
coins = [randint(0, 1) for _ in range(N)]
eagle = 0
tails = 0
for i in coins:
    print(coins[i])
for i in coins:
    if coins[i]==0:
        eagle+=1
    else:
        tails+=1
    i+=1
if eagle==tails:
    print('Нужно перевернуть', tails, 'монеток' )
else:
    if eagle>tails:
        print('Нужно перевернуть', tails, 'монеток' )
    else:
        print('Нужно перевернуть', eagle, 'монеток' )