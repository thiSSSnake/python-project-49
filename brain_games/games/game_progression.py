import random 

game_rules = 'What number is missing in the progression?'

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
    string = " ".join(map(str, sequence))
    choice = random.choice(sequence)
    correct_answer = str(choice)
    string = string.replace(str(choice), ' .. ')
    question = string
    return question, correct_answer


if __name__ == '__quest__':

    quest()
