import prompt

MAX_ROUNDS = 3


def get_name():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    return user_name


def greet(name):
    print(f"Hello, {name}!")


def start_game(game_name):
    user_name = get_name()
    greet(user_name)
    print(game_name.GAME_RULES)
    i = 0
    while i < MAX_ROUNDS:
        question, correct_answer = game_name.quest()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {user_name}!")
            break
        print("Correct!")
        i += 1
    else:
        print(f"Congratulations, {user_name}!")
