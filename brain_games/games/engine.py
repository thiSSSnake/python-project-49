import prompt


def get_name():
    global user_name
    user_name = prompt.string("Welcome to the Brain Games!\nMay I have your name? ")
    return user_name


def greet(name):
    print(f"Hello, {name}!")


def start_game(game_name):
    user_name = get_name()
    greet(user_name)
    print(game_name.game_rules)
    i = 0
    while i < 3:
        question, correct_answer = game_name.quest()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if not (user_answer == correct_answer):
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {user_name}!")
            break
        print("Correct!")
        i += 1
    else:
        print(f"Congratiulations, {user_name}!")


if __name__ == '__start_game__':

    start_game()
