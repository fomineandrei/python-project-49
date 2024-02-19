

import random


# условие игры Простое число
PRIM_CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# Функция создания списка вопросов Простое это число?
# Каждое значение списка заполняется из интервала от 2 до 100 случайным числом
# или значением из списка простых чисел с вероятностью 0.5 для каждого случая
def random_numbers_prime():
    prime_numbers = [2, 3, 5, 7, 11,
                     13, 17, 19, 23, 29, 31,
                     37, 41, 43, 47, 53, 59,
                     61, 67, 71, 73, 79, 83,
                     89, 97]
    prime_list = []
    i = 0
    while i < 3:
        a = random.randint(2, 100)
        b = random.sample(prime_numbers, 1)[0]
        element = random.sample([a, b], 1)
        prime_list.append(element[0])
        i += 1
    return prime_list


# Функция создания списка вопрос - ответ Простое число?
def question_check_prim():
    questions_list = random_numbers_prime()
    check_list = []
    for number in questions_list:
        # Начинаем делить с двойки, так как все натуральные числа
        # делятся на 1 без остатка
        i = 2
        while i < number // 2:
            if number % i != 0:
                i += 1
                continue
            elif number % i == 0:
                check_list.append('no')
                break
        else:
            check_list.append('yes')
    question_check_list = list(zip(questions_list, check_list))
    return question_check_list
