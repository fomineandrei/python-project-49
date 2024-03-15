

import random
import itertools


# Условие игры Калькулятор
RULES = 'What is the result of the expression?'
# Интервалы чисел для различных опреаций
RANGE_SUMM = [(20, 200), (20, 200)]
RANGE_DIFF = [(300, 500), (50, 299)]
RANGE_MULT = [(10, 99), (2, 10)]
# Циклический итератор вариантов математических операций и числовых интервалов
OPERATION_VARIANTS = itertools.cycle(
    [('summ', RANGE_SUMM), ('diff', RANGE_DIFF), ('mult', RANGE_MULT)])


# Вычисление правильного ответа и запись вопроса
def ariph_calculate(arg1, arg2, ariph_operation):
    if ariph_operation == 'summ':
        summ = f'{arg1} + {arg2}'
        return (summ, str(arg1 + arg2))
    elif ariph_operation == 'diff':
        diff = f'{arg1} - {arg2}'
        return (diff, str(arg1 - arg2))
    elif ariph_operation == 'mult':
        mult = f'{arg1} * {arg2}'
        return (mult, str(arg1 * arg2))


# Функция создания кортежа "вопрос - правильный ответ"
def question_answer_pair():
    operation_and_ranges = next(OPERATION_VARIANTS)
    operation = operation_and_ranges[0]
    ranges = operation_and_ranges[1]
    a = random.randint(*ranges[0])
    b = random.randint(*ranges[1])
    question, check = ariph_calculate(a, b, operation)
    return (question, check)
