import random

GAME_RULES = 'What number is missing in the progression?'


def seq():
    number = random.randint(1, 20)
    list = []
    list.append(number)
    count_seq = 0
    while count_seq < 9:
        number += 3
        list.append(number)
        count_seq += 1
    return list


def quest():
    sequence = seq()
    random_index = random.randint(0, len(sequence) - 1)
    correct_answer = sequence[random_index]
    sequence[random_index] = '..'
    question = " ".join(map(str, sequence))
    return question, str(correct_answer)
