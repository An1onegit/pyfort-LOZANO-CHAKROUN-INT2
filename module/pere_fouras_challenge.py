import json
import random

from pygame.examples.video import answer


def load_riddles(file):
    l = []
    with open(file, 'r') as file:
        data = json.load(file)
    for i in range(len(data)):
        riddle = {data[i]["question"]: data[i]["answer"]}
        l.append(riddle)
    return l

def pere_fouras_riddles():
    riddles = load_riddles('PFRiddles.json')
    d = riddles[random.randint(0, len(riddles))]
    attempts = 3
    for key,value in d.items():
        riddle = key
        correct_answer = value
    print(riddle)
    while attempts > 0:
        answer = str(input("Your answer : "))
        answer.lower()
        if answer == correct_answer:
            print("The answer is correct ! You won a key.")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print("Incorrect answer")
                print(f"You have {attempts} attempts left.")
            else:
                print(f"You lost... The correct answer was : {correct_answer}")
                return False

pere_fouras_riddles()