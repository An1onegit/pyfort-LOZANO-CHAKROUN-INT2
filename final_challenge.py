import json
import random


def treasure_room():
    file = 'data/TRClues.json'
    with open(file, 'r') as file:
        tv_game = json.load(file)

    years = []
    for i in tv_game["Fort Boyard"]:
        years.append(i)
    year = years[random.randint(0, len(years)-1)]
    print(year)

    shows = []
    for i in tv_game["Fort Boyard"][year]:
        shows.append(i)
    show = shows[random.randint(0,len(shows)-1)]
    print(show)
    clues = tv_game["Fort Boyard"][year][show]["Clues"]
    code_word = tv_game["Fort Boyard"][year][show]["CODE-WORD"]
    numbers_of_clue = 3
    print(clues[:numbers_of_clue])
    attempts = 3
    answer_correct = False
    while attempts > 0:
        answer = str(input("Your answer (format : ANSWER) : "))
        if answer == code_word:
            answer_correct = True
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"You have {attempts} attempts left")
                numbers_of_clue +=1
                print(clues[:numbers_of_clue])
            else:
                print("The word was : ", code_word)
    if answer_correct:
        print("You won !")
    else:
        print("You lost... too bad...")
