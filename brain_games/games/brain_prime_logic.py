

import random


# условие игры Простое число
PRIM = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# Функция,которая проверяет простое ли число.
def is_prime(num):
    """Начинаем с 2, потомо что все числа деляться на 1 без остатка"""
    i = 2
    while i < num // 2:
        check = (num % i != 0)
        if check is False:
            break
        i += 1
    return check


def question_check_prim():
    prime_numbers = [
        2, 3, 5, 7, 11, 13, 17,
        19, 23, 29, 31, 37, 41,
        43, 47, 53, 59, 61, 67,
        71, 73, 79, 83, 89, 97
    ]
    prime_num = random.choice(prime_numbers)
    """Вероятность выбора простого числа к случайному числу сделаем 1 к 3"""
    random1 = random.randint(1, 99)
    random2 = random.randint(1, 99)
    num_for_game = random.choice((prime_num, random1, random2))
    if is_prime(num_for_game) is True:
        return (num_for_game, 'yes')
    else:
        return (num_for_game, 'no')
