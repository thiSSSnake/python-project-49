#!/usr/bin/env python3
import random
import math

game_rules = 'Find the greatest common divisor of given numbers.'

def quest():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)

    question = str(number_1) + ' ' + str(number_2)
    correct_answer = str(math.gcd(number_1, number_2))
    return question, correct_answer


if __name__ == '__quest__':

    quest()
