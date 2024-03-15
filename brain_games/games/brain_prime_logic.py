

import random


# условие игры Простое число
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
# Набор простых чисел для случайного выбора
PRIME_NUMBERS = [
    2, 3, 5, 7, 11, 13, 17,
    19, 23, 29, 31, 37, 41,
    43, 47, 53, 59, 61, 67,
    71, 73, 79, 83, 89, 97
]
# Диапазон случайных чисел для выбора
RANGE_NUM = (1, 99)


# Функция,которая проверяет простое ли число.
def is_prime(num):
    if num == 1:
        return False
    """Начинаем с 2, потомо что все числа деляться на 1 без остатка"""
    i = 2
    while i <= num // 2:
        if (num % i != 0) is False:
            return False
            break
        i += 1
    else:
        return True


# Функция формирования кортежа "вопрос - правильный ответ"
def question_answer_pair():
    prime_num = random.choice(PRIME_NUMBERS)
    """Вероятность выбора простого числа к случайному числу сделаем 1 к 3"""
    random1 = random.randint(*RANGE_NUM)
    random2 = random.randint(*RANGE_NUM)
    num_for_game = random.choice((prime_num, random1, random2))
    if is_prime(num_for_game) is True:
        return (num_for_game, 'yes')
    else:
        return (num_for_game, 'no')
