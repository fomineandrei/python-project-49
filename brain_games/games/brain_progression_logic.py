

import random


# условие игры Арифметическая прогрессия
RULES = 'What number is missing in the progression?'
# Длина прогрессии
PROG_LENGTH = 10
# Начало прогрессии
START_RANGE = 70
# Шаг прогрессии
STEP_RANGE = 15
# Индекс скрываемого числа прогрессии
INDEX_RANGE = PROG_LENGTH - 1


# Функция создания арифметической прогрессии
def random_progression(start, step, length):
    start_prog = random.randint(1, start)
    step_prog = random.randint(1, step)
    progression = []
    i = 0
    while i < length:
        progression.append(str(start_prog))
        start_prog = start_prog + step_prog
        i += 1
    return progression


# Функция создания строки вопроса
def progression_string(progression, index):
    random_index = random.randint(1, index)
    check = progression[random_index]
    progression[random_index] = '..'
    return " ".join(progression), check


# Функция заполнения листа вопросов
def question_check():
    progression = random_progression(START_RANGE, STEP_RANGE, PROG_LENGTH)
    question, check = progression_string(progression, INDEX_RANGE)
    return (question, check)
