# Battleship game
import random


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
        print("|")
        for j in range(len(grid[i])):
            print(grid[i][j], end="|")
        print("")
    print("----------------------")

def ask_position():
    while True:
        try:
            user_input = input("Enter a position in format row,column : ").strip()
            row, column = map(int, user_input.split(','))
            if row in [0, 2] and column in [0, 2]:
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
    return display_grid(grid, "Here is your game grid with your boats: ")

def turn(player, player_shots_grid, opponent_grid):
    display_grid(player_shots_grid, "Player history shots")

    if player == 0:
        pos = ask_position()
    else:
        pos = (random.randint(0, 2), random.randint(0, 2))

    if opponent_grid[pos[0]][pos[1]] == "B":
        player_shots_grid[pos[0]][pos[1]] = "x"
    else:
        player_shots_grid[pos[0]][pos[1]] = "."

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
    initialize()
    ai_grid = empty_grid()
    for i in range(2):
        pos = (random.randint(0, 2), random.randint(0, 2))
        ai_grid[pos[0]][pos[1]] = "B"

    player_shots_grid = empty_grid()
    ai_shots_grid = empty_grid()
    shots_grids = [player_shots_grid, ai_shots_grid]

    player = 0
    while not has_won(shots_grids[player]):
        turn(player, player_shots_grid, ai_shots_grid)
        if has_won(shots_grids[0]):
            print("The player won!")
            return True
        elif has_won(shots_grids[1]):
            print("The game master won. You lost...")
            return False
        else:
            next_player(player)
