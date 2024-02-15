

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
        answer = prompt.string('Your answer: ')
        if answer == check:
            print('Correct!')
            continue
        elif answer != check:
            print(f"'{answer}' is wrong answer;(. Correct answer is '{check}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
