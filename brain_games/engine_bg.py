

import prompt
from brain_games.games.brain_calc_logic import CALC, question_check_calc
from brain_games.games.brain_even_logic import EVEN, question_check_even
from brain_games.games.brain_gcd_logic import GCD, question_check_gcd
from brain_games.games.brain_prime_logic import PRIM, question_check_prim
from brain_games.games.brain_progression_logic import PROG, question_check_prog


ROUNDS_NUM = 3


# Приветствие и ввод имени пользователя(универсальный)
def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


# Функция подбора генератора для каждой игры
def generators(game_type):
    if game_type == CALC:
        return question_check_calc()
    elif game_type == EVEN:
        return question_check_even()
    elif game_type == GCD:
        return question_check_gcd()
    elif game_type == PRIM:
        return question_check_prim()
    elif game_type == PROG:
        return question_check_prog()


# Ввод и проверка ответов(универсальный)
def game_check(condition):
    name = welcome_user()
    print(condition)
    game_round = 1
    while game_round <= ROUNDS_NUM:
        question, check = generators(condition)
        print(f'Question: {question}')
        answer = input('Your answer: ')
        if str(answer) == check:
            print('Correct!')
            game_round += 1
            continue
        elif str(answer) != check:
            print(f"'{answer}' is wrong answer;(. Correct answer is '{check}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
