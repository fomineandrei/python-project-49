

import random
import itertools


# Условие игры Калькулятор
RULES = 'What is the result of the expression?'
# Циклический итератор вариантов математических операций
OPERATION_VARIANTS = itertools.cycle(['summ', 'diff', 'mult'])


# Функция создания кортежа "вопрос - правильный ответ"
def question_check():
    a = random.randint(20, 200)
    b = random.randint(20, 200)
    c = random.randint(300, 500)
    d = random.randint(50, 299)
    u = random.randint(10, 99)
    v = random.randint(2, 10)
    operation = next(OPERATION_VARIANTS)
    if operation == 'summ':
        summ = f'{a} + {b}'
        return (summ, str(a + b))
    elif operation == 'diff':
        diff = f'{c} - {d}'
        return (diff, str(c - d))
    elif operation == 'mult':
        mult = f'{u} * {v}'
        return (mult, str(u * v))
