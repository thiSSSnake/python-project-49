import random

GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'

PRIME_NUMBERS = [
        2, 3, 5, 7,
        11, 13, 17, 19,
        23, 29, 31, 37,
        41, 43, 47, 53,
        59, 61, 67, 71,
        73, 79, 83, 89,
        97
    ]


def is_prime(num):
    correct_answer = ''
    if num in PRIME_NUMBERS:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer


def quest():
    num = random.randint(1, 97)
    question = str(num)
    correct_answer = is_prime(num)
    return question, correct_answer
