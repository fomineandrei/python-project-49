#!/usr/bin/env python3


import random
from brain_games.games.functions import welcome_user
from brain_games.games.functions import game_check


# Функция заполнения листа вопросов
def random_progressions():
    start = random.randint(1, 70)
    step = random.randint(1, 15)
    progression_list = []
    i = 0
    while i < 3:
        start = random.randint(1, 70)
        step = random.randint(1, 15)
        progression = []
        u = 0
        while u < 10:
            progression.append(str(start))
            start = start + step
            u += 1
        progression_list.append(progression)
        i += 1
    return progression_list


# Функция заполнения листа вопрос - ответ
def question_check_func(random_progressions):
    check_list = []
    progressions_list = random_progressions
    for progression in progressions_list:
        index = random.randint(0, 9)
        check_list.append(progression[index])
        progression[index] = '..'
    question_list = []
    for progression in progressions_list:
        question_list.append(" ".join(progression))
    question_check_list = list(zip(question_list, check_list))
    return question_check_list


# Функция условий игры Арифметическая прогрессия
def condition_progression():
    print('What number is missing in the progression?')


def main():
    welcome_user()
    condition_progression()
    game_check(question_check_func(random_progressions()))


if __name__ == '__main__':
    main()
