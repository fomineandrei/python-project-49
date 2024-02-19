

import math
import random


# Услловие игры Наибольший Общий Делителm
GCD_CONDITION = 'Find the greatest common divisor of given numbers.'


# Функция создания списка пар чисел для нахождения НОД
def random_numbers_pairs():
    for_sample = [(24, 64), (18, 99), (26, 65), (15, 70), (32, 78), (17, 85)]
    pairs_list = random.sample(for_sample, 2)
    # Добавим случайную  пару
    pairs_list.append((random.randint(2, 50), random.randint(51, 100)))
    questions_list = []
    for pair in pairs_list:
        a, b = pair
        questions_list.append(f'{a} {b}')
    return (questions_list, pairs_list)


# Функция создания списка вопрос - ответ
def question_check_gcd():
    questions_list, pairs_list = random_numbers_pairs()
    gcd_list = []
    for pair in pairs_list:
        a, b = pair
        gcd = math.gcd(a, b)
        gcd_list.append(str(gcd))
    questions_check_list = list(zip(questions_list, gcd_list))
    return questions_check_list
