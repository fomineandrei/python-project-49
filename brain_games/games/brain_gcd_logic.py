

import math
import random


# Условие игры Наибольший Общий Делителm
RULES = 'Find the greatest common divisor of given numbers.'


# Функция создания списка пар чисел для нахождения НОД
def question_answer_pair():
    multiplier = random.randint(1, 10)
    a = multiplier * random.randint(2, 10)
    b = multiplier * random.randint(2, 10)
    return (f'{a} {b}', str(math.gcd(a, b)))
