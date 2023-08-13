#!/usr/bin/env python3
from random import randint
import prompt


def random_quest():

    return (randint(1, 50))


def main():

    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no"')
    i = 0
    while i < 3:
        i += 1
        number = random_quest()
        print('Question:', number)
        answer = prompt.string("Your answer: ")
        if answer == 'yes' and number % 2 != 0:
            return f"'{answer}' is wrong answer :(. Correct answer was 'no'\nLet's try again, {name}"
        if answer == 'no' and number % 2 == 0:
            return f"'{answer}' is wrong answer :(. Correct answer was 'yes'\nLet's try again, {name}"
        if answer == 'yes' and number % 2 == 0:
            print('Correct!')
        if answer == 'no' and number % 2 != 0:
            print('Correct!')
    return f'Congratulations, {name}!'       


if __name__ == '__main__':

    main()
