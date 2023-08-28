import random

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return True
    if number % 2 != 0:
        return False


def quest():
    number = random.randint(1, 50)
    correct_answer = ''
    question = number
    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
