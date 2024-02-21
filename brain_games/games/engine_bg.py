

import prompt


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
def game_bg(question_check, condition):
    welcome_user()
    game_condition(condition)
    game_check(question_check)
