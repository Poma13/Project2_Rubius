from random import randint as ri
import os


# генерация чисел для разных режимов


def get_num_4_1():
    a = ri(1, 100)
    b = ri(1, 100)
    return [a, b]


def get_num_4_2():
    while 1:
        a = ri(1, 100)
        b = ri(1, 100)
        if a > b:
            break
    return [a, b]


def get_num_4_3():
    while 1:
        a = ri(2, 100)
        b = ri(2, 100)
        if a * b < 201:
            break
    return [a, b]


def get_num_4_4():
    while 1:
        a = ri(2, 100)
        b = ri(2, 100)
        if a != b and a % b == 0:
            break
    return [a, b]


# сложение
def one(n=10):
    ex = 0
    score = 0
    for i in range(n):
        l = get_num_4_1()
        a = input(f"{l[0]} + {l[1]} = ")
        if a == 'menu':
            ex = 1
            break
        if a.isdigit() and int(a) == l[0] + l[1]:
            score += 1
    if ex == 1:
        return -1
    else:
        return score


# вычитание
def two(n=10):
    ex = 0
    score = 0
    for i in range(n):
        l = get_num_4_2()
        a = input(f"{l[0]} - {l[1]} = ")
        if a == 'menu':
            ex = 1
            break
        if a.isdigit() and int(a) == l[0] - l[1]:
            score += 1
    if ex == 1:
        return -1
    else:
        return score


# умножение
def three(n=10):
    ex = 0
    score = 0
    for i in range(n):
        l = get_num_4_3()
        a = input(f"{l[0]} * {l[1]} = ")
        if a == 'menu':
            ex = 1
            break
        if a.isdigit() and int(a) == l[0] * l[1]:
            score += 1
    if ex == 1:
        return -1
    else:
        return score


# деление
def four(n=10):
    score = 0
    ex = 0
    for i in range(n):
        l = get_num_4_4()
        a = input(f"{l[0]} / {l[1]} = ")
        if a == 'menu':
            ex = 1
            break
        if a.isdigit() and int(a) == l[0] / l[1]:
            score += 1
    if ex == 1:
        return -1
    else:
        return score


# всё вместе
def five():
    score = 0
    ex = 0
    o = one(2)
    if o == -1:
        ex = 1
    else:
        score = + o
        tw = two(3)
        if tw == -1:
            ex = 1
        else:
            score += tw
            th = three(2)
            if th == -1:
                ex = 1
            else:
                score += th
                f = four(3)
                if f == -1:
                    ex = 1
                else:
                    score += f
    if ex == 1:
        return -1
    else:
        return score

# определение оценки
def rate(sc):
    if sc >= 9:
        return 5
    else:
        if sc >= 8:
            return 4
        else:
            if sc >= 6:
                return 3
            else:
                if sc >= 5:
                    return 2
                else:
                    return 1

str = '-'
# главный цикл
while True:
    print(f'\nТест по арифметике\n')
    print('1 - сложение')
    print('2 - вычитание ')
    print('3 - умножение')
    print('4 - деление')
    print('5 - всё вместе')
    print('menu - очистить экран и вернуться в гл. меню')
    print('end - выход из программы')
    mode = input('Выберите режим (введите цифру):')
    if mode == '1':
        One = one()
        os.system('CLS')
        if One != -1:
            print(f'{str*13}\nВаша оценка {rate(One)}\n{str*13}')
    elif mode == '2':
        Two = two()
        os.system('CLS')
        if Two != -1:
            print(f'{str*13}\nВаша оценка {rate(Two)}\n{str*13}')
    elif mode == '3':
        Three = three()
        os.system('CLS')
        if Three != -1:
            print(f'{str*13}\nВаша оценка {rate(Three)}\n{str*13}')
    elif mode == '4':
        Four = four()
        os.system('CLS')
        if Four != -1:
            print(f'{str*13}\nВаша оценка {rate(Four)}\n{str*13}')
    elif mode == '5':
        Five = five()
        os.system('CLS')
        if Five != -1:
            print(f'{str*13}\nВаша оценка {rate(Five)}\n{str*13}')
    elif mode == "end":
        break
    else:
        os.system('CLS')
        print(f'{str*17}\nНекорректный ввод\n{str*17}')
