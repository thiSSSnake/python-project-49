#!/usr/bin/env python3
import random

game_rules = "What is the result of the expression?"

def quest():
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    list_operators = ['+', '-', '*']
    oper = random.choice(list_operators)

    
    question = str(num_1) + f' {oper} ' + str(num_2)
    correct_answer = str(eval(question))
    return question, correct_answer


if __name__ == '__quest__':

    quest()
