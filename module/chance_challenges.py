import random

def chance_challenge():
    x = random.randint(1,2)
    match x:
        case 1:
            shell_game()
        case 2:
            roll_dice_game()

def shell_game():
    l = ["A","B","C"]
    print("The rules of this challenge are quite simple. You can chose between those three shells, if you find the key you win ! You have two tries quick!")
    print(l)
    attempts = 0
    n = 0
    for i in range(2) :
        n = random.randint(0,len(l)-1)
        attempts += 1
        shell = l[n]
        guess = input("Enter your guess : ")
        if guess == shell :
            print("Congrats ! you found the key. Seems like you are good at these.")
            return True
        else :
            print("Wrong ! You have one more try.")
    if attempts == 2 :
        print(f"You lose, the key was under the shell {l[n]}.")
        return False

def roll_dice_game():
    attempts = 3
    for i in range(attempts):
        player_dice = (random.randint(1, 6), random.randint(1, 6))
        master_dice = (random.randint(1, 6), random.randint(1, 6))
        print(f"You have {attempts} tries left.")
        x = str(input("Roll the dice by pressing Enter"))
        if x == "":
            print("Yours dices : ", player_dice)
            if 6 in player_dice:
                print("Congrats ! You won a key.")
                return True
            print("Game master dices : ", master_dice)
            if 6 in master_dice:
                print("Oh no... Game master has won.")
                return False
            else:
                print("Next attempt")
    print("None of the players won... It's a draw.")
    return False

chance_challenge()