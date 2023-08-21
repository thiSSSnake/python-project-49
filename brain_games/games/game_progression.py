import random

GAME_RULES = 'What number is missing in the progression?'


def seq():
    a = random.randint(1, 20)
    list = []
    list.append(a)
    i = 0
    while i < 9:
        a += 3
        list.append(a)
        i += 1
    return list


def quest():
    sequence = seq()
    random_index = random.randint(0, len(sequence) - 1)
    correct_answer = sequence[random_index]
    sequence[random_index] = '..'
    question = " ".join(map(str, sequence))
    return question, str(correct_answer)


if __name__ == '__quest__':

    quest()
