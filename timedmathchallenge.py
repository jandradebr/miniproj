'''
This is a time math challenge script.
'''

from datetime import datetime
from random import randint

num1 = randint(1,10)
num2 = randint(1,10)

operator = randint(0,3)


match operator:
    case 0:#+
        result = num1 + num2
        t1 = datetime.now()
        test = int(input(f'Calculate {num1} + {num2}: '))
        t2 = datetime.now()
        time = t2-t1
        if test == result:
            print(f'Congratulations! You guessed in {time}')
        else:
            print('Bad luck! :(')

    case 1:#-
        result = num1 - num2
        t1 = datetime.now()
        test = int(input(f'Calculate {num1} - {num2}: '))
        t2 = datetime.now()
        time = t2-t1
        if test == result:
            print(f'Congratulations! You guessed in {time}')
        else:
            print('Bad luck! :(')

    case 2:#*
        result = num1 * num2
        t1 = datetime.now()
        test = int(input(f'Calculate {num1} * {num2}: '))
        t2 = datetime.now()
        time = t2-t1
        if test == result:
            print(f'Congratulations! You guessed in {time}')
        else:
            print('Bad luck! :(')

    case 3:#/
        result = num1 / num2
        t1 = datetime.now()
        test = int(input(f'Calculate {num1} / {num2}: '))
        t2 = datetime.now()
        time = t2-t1
        if test == result:
            print(f'Congratulations! You guessed in {time}')
        else:
            print('Bad luck! :(')
