import random
import math

GAME_RULES = 'Find the greatest common divisor of given numbers.'


def quest():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)

    question = f'{number_1} {number_2}'
    correct_answer = str(math.gcd(number_1, number_2))
    return question, correct_answer
