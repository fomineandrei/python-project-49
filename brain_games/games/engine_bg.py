

import prompt
from brain_games.games.brain_even_logic import EVEN_CONDITION, question_check_even
from brain_games.games.brain_calc_logic import CALC_CONDITION, question_check_calc
from brain_games.games.brain_gcd_logic import GCD_CONDITION, question_check_gcd
from brain_games.games.brain_progression_logic import PROG_CONDITION, question_check_prog
from brain_games.games.brain_prime_logic import PRIM_CONDITION, question_check_prim


# Приветствие и ввод имени пользователя(универсальный)
def welcome_user():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


# Ввод и проверка ответов(универсальный)
def game_check(question_check_list):
    for question, check in question_check_list:
        print(f'Question: {question}')
        answer = input('Your answer: ')
        if str(answer) == check:
            print('Correct!')
            continue
        elif str(answer) != check:
            print(f"'{answer}' is wrong answer;(. Correct answer is '{check}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')


# Функция печати условия игры
def game_condition(game_type):
    print(game_type)


# Функции логики игр
def game_even():
    welcome_user()
    game_condition(EVEN_CONDITION)
    game_check(question_check_even())


def game_calc():
    welcome_user()
    game_condition(CALC_CONDITION)
    game_check(question_check_calc())


def game_gcd():
    welcome_user()
    game_condition(GCD_CONDITION)
    game_check(question_check_gcd())


def game_prog():
    welcome_user()
    game_condition(PROG_CONDITION)
    game_check(question_check_prog())


def game_prim():
    welcome_user()
    game_condition(PRIM_CONDITION)
    game_check(question_check_prim())
