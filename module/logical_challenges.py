# Battleship game
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
    for i in range(2):
        pos = ask_position()
        while grid[pos[0]][pos[1]] != " ":
            pos = ask_position()
        grid[pos[0]][pos[1]] = "B"
    return display_grid(grid, "Player grid")

def turn(player, player_shots_grid, opponent_grid):
    pass