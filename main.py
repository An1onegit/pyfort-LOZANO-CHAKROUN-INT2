import final_challenge
import utility_functions
from chance_challenges import chance_challenge
from logical_challenges import logical_challenge
from math_challenges import math_challenge
from pere_fouras_challenge import pere_fouras_riddles

def game():
    key = 0
    utility_functions.introduction()
    team = utility_functions.compose_equipe()
    while key < 3:
        challenge = utility_functions.challenge_menu()
        player = utility_functions.choose_player(team)
        match challenge:
            case 1:
                if math_challenge():
                    player["key"] += 1
                    key += 1
            case 2:
                if logical_challenge():
                    player["key"] += 1
                    key += 1
            case 3:
                if chance_challenge():
                    player["key"] += 1
                    key += 1
            case 4:
                if pere_fouras_riddles():
                    player["key"] += 1
                    key += 1
    if final_challenge.treasure_room():
            print("Win")
            return True
    else:
        print("Lose")
        return False

game()