

import random


# условие игры Арифметическая прогрессия
RULES = 'What number is missing in the progression?'
# Длина прогрессии
PROG_LENGTH = 10
# Начало прогрессии
START_RANGE = [1, 70]
# Шаг прогрессии
STEP_RANGE = [1, 15]
# Индекс скрываемого числа прогрессии
INDEX_RANGE = [1, PROG_LENGTH - 1]


# Функция создания арифметической прогрессии
def random_progression(start, step, length):
    progression = []
    i = 0
    while i < length:
        progression.append(str(start))
        start = start + step
        i += 1
    return progression


# Функция создания строки вопроса
def progression_string(progression, index):
    check = progression[index]
    progression[index] = '..'
    return " ".join(progression), check


# Функция заполнения листа вопросов
def question_check():
    start_rand = random.randint(*START_RANGE)
    step_rand = random.randint(*STEP_RANGE)
    index_rand = random.randint(*INDEX_RANGE)
    progression = random_progression(start_rand, step_rand, PROG_LENGTH)
    question, check = progression_string(progression, index_rand)
    return (question, check)
