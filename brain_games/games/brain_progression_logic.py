

import random


# условие игры Арифметическая прогрессия
PROG = 'What number is missing in the progression?'
# Длина прогрессии
PROGRESSION_LENGTH = 10


# Функция заполнения листа вопросов
def question_check_prog():
    start = random.randint(1, 70)
    step = random.randint(1, 15)
    progression = []
    i = 0
    while i < PROGRESSION_LENGTH:
        progression.append(str(start))
        start = start + step
        i += 1
    index = random.randint(0, 9)
    check = progression[index]
    progression[index] = '..'
    return (" ".join(progression), check)
