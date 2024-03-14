

import random


# Условия игры brain_even
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


# Функция проверки случайных чисел на четность
def even_check(num: int) -> bool:
    reminder = num % 2
    return reminder == 0


# Функция формирования кортежа "вопрос - правильный ответ"
def question_answer_pair():
    num = random.randint(1, 999)
    if even_check(num) is True:
        return (num, 'yes')
    else:
        return (num, 'no')
