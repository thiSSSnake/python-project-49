import random

GAME_RULES = 'What number is missing in the progression?'


def making_a_sequence():
    start = random.randint(1, 40)
    step = random.randint(1, 10)
    end = start + step * 10
    progression = list(range(start, end, step))
    return progression


def quest():
    sequence = making_a_sequence()
    random_index = random.randint(0, len(sequence) - 1)
    correct_answer = sequence[random_index]
    sequence[random_index] = '..'
    question = " ".join(map(str, sequence))
    return question, str(correct_answer)
