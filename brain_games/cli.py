import prompt


def welcome_user():
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    return 'Hello, ' + name + '!'
