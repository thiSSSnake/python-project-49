import random
import operator


GAME_RULES = "What is the result of the expression?"


def operation():
    action = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.pow
    }
    return random.choice(list(action))


def quest():
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    oper = operation()
    question = str(num_1) + f' {oper} ' + str(num_2)
    correct_answer = str(eval(question))
    return question, correct_answer
