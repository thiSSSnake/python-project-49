#!/usr/bin/env python3
import prompt
import random

def greet():
    global name
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ') 
    print('Hello, ' + name + '!')
    print('What is the result of the expression?')


def calc_quest():
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    list_operators = ['+', '-', '*']
    oper = random.choice(list_operators)

    return str(num_1) + f' {oper} ' + str(num_2)

    
def main():
    greet()
    i = 0
    while i < 3:
        i += 1
        question = calc_quest()
        correct_answer = str(eval(question))
        print("Question:", question)
        user_answer = prompt.string("Your answer: ")
        if user_answer == correct_answer:
            print("Correct!")
        if user_answer != correct_answer:  
            return f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!"
    return f'Congratiulations, {name}!'


if __name__ == '__main__':

    main()