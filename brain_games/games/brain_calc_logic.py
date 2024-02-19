

import random


# Условие игры Калькулятор
CALC_CONDITION = 'What is the result of the expression?'


# Функция создания списка арифметических выражений
def random_calc():
    questions = []
    global a, b, c, d, u, v
    a = random.randint(20, 200)
    b = random.randint(20, 200)
    c = random.randint(300, 500)
    d = random.randint(50, 299)
    u = random.randint(10, 99)
    v = random.randint(2, 10)
    summ = f'{a} + {b}'
    questions.append(summ)
    diff = f'{c} - {d}'
    questions.append(diff)
    mult = f'{u} * {v}'
    questions.append(mult)
    return questions


# Функция расчета правильных ответов
def check_calc(questions_list):
    check_list = []
    for element in questions_list:
        if element == f'{a} + {b}':
            check_list.append(str(a + b))
        elif element == f'{c} - {d}':
            check_list.append(str(c - d))
        elif element == f'{u} * {v}':
            check_list.append(str(u * v))
    return check_list


# Функция создвния списка пар вопрос-правильный ответ
def question_check_calc():
    question = random_calc()
    check = check_calc(question)
    check_list = list(zip(question, check))
    return check_list
