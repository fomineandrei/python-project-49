#!/usr/bin/env python3


import random
import prompt


# Функция заполнения списка случайными целыми числами
def random_numbers():
    five_numbers = []
    iteration = 0
    while iteration < 3:
        number = random.randint(1, 99)
        five_numbers.append(number)
        iteration += 1
    return five_numbers


# Приветствие и ввод имени пользователя(универсальный)
def welcome_user():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


# Проверка на четность, создание списка правильных ответов
def check_func_even(question_list):
    check_list = []
    for number in question_list:
        reminder = number % 2
        if reminder == 0:
            check_list.append('yes')
        else:
            check_list.append('no')
    return check_list


# Создание списка вопрос-ответ
def question_check_list():
    question = random_numbers()
    check = check_func_even(question)
    question_check_list = list(zip(question, check))
    return question_check_list


# Условие игры четное-нечетное
def condition_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')


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


def main():
    welcome_user()
    condition_even()
    game_check(question_check_list())


if __name__ == '__main__':
    main()
