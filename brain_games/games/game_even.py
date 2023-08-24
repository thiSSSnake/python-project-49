import random

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def even(number):
    correct_answer = ''
    if number % 2 == 0:
        correct_answer += 'yes'
    if number % 2 != 0:
        correct_answer += 'no'
    return correct_answer


def quest():
    number = random.randint(1, 50)

    question = number
    correct_answer = even(number)
    return question, correct_answer
