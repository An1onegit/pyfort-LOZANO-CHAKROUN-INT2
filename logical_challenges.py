# Battleship game
import random

def logical_challenge():
    x = random.randint(1, 4)
    match x:
        case 1:
            nim_game()
        case 2:
            tictactoe_game()
        case 3:
            battleship_game()


def next_player(actual_player):
    return (actual_player + 1) % 2

def empty_grid():
    l = [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
    ]
    return l

def display_grid(grid, message):
    print(message)
    for i in range(len(grid)):
        print("|", end="")
        for j in range(len(grid[i])):
            print(grid[i][j], end="|")
        print("")
    print("----------------------")

def ask_position():
    while True:
        try:
            user_input = input("Enter a position in format row,column : ").strip()
            row, column = map(int, user_input.split(','))
            if 0 <= row <= 2 and 0 <= column <= 2:
                return row, column
            else:
                print("Position out of bounds. Please enter values between 0 and 2.")
        except ValueError:
            print("Invalid input format. Please enter the position as row,column (e.g., 1,2).")

def initialize():
    grid = empty_grid()
    print("Place your boats: ")
    for i in range(2):
        print(f"Boat {i+1}")
        pos = ask_position()
        while grid[pos[0]][pos[1]] != " ":
            pos = ask_position()
        grid[pos[0]][pos[1]] = "B"
    display_grid(grid, "Here is your game grid with your boats: ")
    return grid

def turn(player, player_shots_grid, opponent_grid):
    if player == 0:
        display_grid(player_shots_grid, "History of your previous shots: ")
        pos = ask_position()
        while player_shots_grid[pos[0]][pos[1]] == "." or player_shots_grid[pos[0]][pos[1]] == "x":
            pos = ask_position()
    else:
        pos = (random.randint(0, 2), random.randint(0, 2))
        while player_shots_grid[pos[0]][pos[1]] == "." or player_shots_grid[pos[0]][pos[1]] == "x":
            pos = (random.randint(0, 2), random.randint(0, 2))
        print(f"The game master shoots at position {pos}")

    if opponent_grid[pos[0]][pos[1]] == "B":
        player_shots_grid[pos[0]][pos[1]] = "x"
        print("Hit, sunk!")
    else:
        player_shots_grid[pos[0]][pos[1]] = "."
        print("Splash...")

def has_won(player_shots_grid):
    count = 0
    for i in range(len(player_shots_grid)):
        for j in range(len(player_shots_grid[i])):
            if player_shots_grid[i][j] == "x":
                count += 1
    if count == 2:
        return True
    else:
        return False

def battleship_game():
    print("Each player must place 2 boats on a 3x3 grid.")
    print("Boats are represented by 'B' and missed shots by '.'. Sunk boats are marked by 'x'.'")
    player_grid = initialize()
    ai_grid = empty_grid()
    for i in range(2):
        pos = (random.randint(0, 2), random.randint(0, 2))
        ai_grid[pos[0]][pos[1]] = "B"

    player_shots_grid = empty_grid()
    ai_shots_grid = empty_grid()

    player = 0
    while True:
        if player == 0:
            print("It's your turn to shoot!")
            turn(player, player_shots_grid, ai_grid)
            if has_won(player_shots_grid):
                print("The player won!")
                return True
            else:
                player = next_player(player)
        elif player == 1:
            print("It's the game master's turn:")
            turn(player, ai_shots_grid, player_grid)
            if has_won(ai_shots_grid):
                print("The game master won. You lost...")
                return False
            else:
                player = next_player(player)

#battleship_game()

# The Game of Nim
def display_sticks(n):
    for i in range(n):
        print("|", end=" ")
    print("")

def player_removal(n):
    x = int(input("Choose how many you want to remove (1,2 or 3) : "))
    while x not in [1,2,3] and x > n:
        x = int(input("Choose a valid amount of stick you want to remove (1,2 or 3) : "))
    return x

def master_removal(n):
    print("It's the game master's turn")
    rem = n % 4
    match rem:
        case 0:
            print("He choose to remove 3 sticks")
            return 3
        case 1:
            sticks = random.randint(1,3)
            print(f"He choose to remove {sticks} sticks")
            return sticks
        case 2:
            print("He choose to remove 1 sticks")
            return 1
        case 3:
            print("He choose to remove 2 sticks")
            return 2

def nim_game():
    sticks = 20
    turn = True
    while sticks > 0:
        display_sticks(sticks)
        if turn:
            sticks -= player_removal(sticks)
        else:
            sticks -= master_removal(sticks)
        turn = not turn
        if sticks == 1:
            display_sticks(sticks)
            if turn:
                print("There is only one stick left, you lost...")
                return False
            else:
                print("You won !")
                return True

#nim_game()

#The tic tac toe game

def display_grid2(grid):
    for i in range(3):
        print("|")
        for j in range(3):
            print(grid[i][j],"|")
    print("---------")

    return grid

def check_victory(grid, symbol):
    #check rows
    for i in range(3):
        s = 0
        for j in range(3):
            if grid[i][j] == symbol:
                s += 1
        if s == 3:
            return True
    #check columns
    for i in range(3):
        s=0
        for j in range(3):
            if grid[j][i]==symbol:
                s+=1
        if s==3:
            return True 

    #check diagonal
    for i in range(3):
        s=0
        if grid[i][i]==symbol:
            s+=1
    if s==3 :
        return True

    #check anti diagonal
    for i in range(3):
        s=0
        if grid[i][2-i]==symbol:
            s+=1
    if s==3 :
        return True

def master_move(grid, symbol):
    if symbol=="O":
        opps_symbol="X"
    else:
        opps_symbol ="O"


#check for win
    for i in range(3):
       for j in range(3):
           if grid[i][j]==" ":
               grid[i][j]=symbol
               if check_victory(grid, symbol):
                   grid[i][j]=" "
                   return (i,j)
               grid[i][j]=" "


#defence
    for i in range(3):
        for j in range(3):
            if grid[i][j]==" ":
                grid[i][j]=opps_symbol
                if check_victory(grid, opps_symbol):
                    grid[i][j]=" "
                    return (i,j)
                grid[i][j]=" "


#random






















