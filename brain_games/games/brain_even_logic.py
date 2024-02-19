

import random


# Условия игры brain_even
EVEN = 'Answer "yes" if the number is even, otherwise answer "no".'


# Функция заполнения списка случайными целыми числами
def random_numbers():
    five_numbers = []
    iteration = 0
    while iteration < 3:
        number = random.randint(1, 99)
        five_numbers.append(number)
        iteration += 1
    return five_numbers


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
def question_check_even():
    question = random_numbers()
    check = check_func_even(question)
    question_check_list = list(zip(question, check))
    return question_check_list
