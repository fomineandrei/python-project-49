

import math
import random


# Условие игры Наибольший Общий Делителm
RULES = 'Find the greatest common divisor of given numbers.'
# Диапазоны для множителя и чисел
RANGE_MULT = (1, 10)
RANGE_NUM1 = (2, 10)
RANGE_NUM2 = (2, 10)


# Функция создания списка пар чисел для нахождения НОД
def question_answer_pair():
    multiplier = random.randint(*RANGE_MULT)
    a = multiplier * random.randint(*RANGE_NUM1)
    b = multiplier * random.randint(*RANGE_NUM2)
    return (f'{a} {b}', str(math.gcd(a, b)))
