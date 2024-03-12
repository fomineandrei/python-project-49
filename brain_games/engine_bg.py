

import prompt


ROUNDS_NUM = 3


# Приветствие и ввод имени пользователя(универсальный)
def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


# Ввод и проверка ответов(универсальный)
def game_check(game):
    name = welcome_user()
    print(game.RULES)
    game_round = 1
    while game_round <= ROUNDS_NUM:
        question, check = game.question_check()
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
