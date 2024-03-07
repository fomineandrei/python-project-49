

import random


# условие игры Арифметическая прогрессия
RULES = 'What number is missing in the progression?'
# Длина прогрессии
PROGRESSION_LENGTH = 10
# Имя модуля
MODULE = 'brain_games.games.brain_progression_logic'


# Функция создания арифметической прогрессии
def random_progression():
    start = random.randint(1, 70)
    step = random.randint(1, 15)
    progression = []
    i = 0
    while i < PROGRESSION_LENGTH:
        progression.append(str(start))
        start = start + step
        i += 1
    return progression


# Функция создания строки вопроса
def progression_string(progression):
    index = random.randint(0, 9)
    check = progression[index]
    progression[index] = '..'
    return " ".join(progression), check


# Функция заполнения листа вопросов
def question_check():
    progression = random_progression()
    question, check = progression_string(progression)
    return (question, check)
