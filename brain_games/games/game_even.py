import random

game_rules = 'Answer "yes" if the number is even, otherwise answer "no"'

def quest():
    number = random.randint(1, 50)

    question = number
    correct_answer = ''
    if number % 2 == 0:
        correct_answer += 'yes'
    if number % 2 != 0:
        correct_answer += 'no'
    return question, correct_answer


if __name__ == '__quest__':

    quest()