# Fort Boyard - Math Challenges in Console

---

## 1. General Presentation

### Project Title  
**Fort Boyard - Math Challenges in Console**

### Contributors  
- **Lino Lozano** 
- **Giordano Chakroun** 

### Description  
In this project, you are immersed in the world of *Fort Boyard*! Each player must solve puzzles and math challenges to collect keys and progress toward the treasure room.

### Key Features  
- **Varied Math Challenges**: Challenges range from mental arithmetic to logic puzzles, solving equations, and numeric sequences.
- **Key Collection**: Players need to complete challenges to earn keys, each unlocking progress toward the treasure room.
- **Console Interface**: The game is played directly in your terminal or console.

## 2. Installation

1. **Clone the repository**:  
   ```bash
   git clone https://github.com/An1onegit/pyfort-LOZANO-CHAKROUN-INT2.git
   ```
---

## 3. How to Use

To start the game, run the following command in your terminal:  
```bash
python main.py
```

## 4. Technical Documentation

### Game Algorithm  
The game is structured as follows:

1. The player starts the game.
2. The player creates a team.
3. The system shows a menu of challenges.
4. One player can choose to play one of thoses challenges
5. The player submits their answer:
   - If the answer is correct, the player earns a key.
   - If the answer is incorrect, they lose a chance.
6. The player continues solving challenges until they have enough keys.
7. If the player collects enough keys, they unlock the treasure room and face a final puzzle.

### Functions

| **Function**              | **Description**                                                                                          | **Parameters**              |
|---------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------|
| `game()`                  | Starts the game and initializes the necessary variables.                                                  | None                        |
| `nim_game()`              | Handle the nim game.                                                                                     | None
| `check_victory()`         | Checks if the player won.                                                                               | `grid`: game's grid, `symbol`: player's symbol |
| `load_riddles()`          | Load the riddles frome a JSON file.                                                                    | `file`: file with all the riddles  |
| `compose_equipe()`        | Compose the team.                                                                                       | None                        |

### Input and Error Management  
- **Input Validation**: The game ensures that user input is in the correct format (numbers, expressions).  
  
**Known Bugs**:
- If the player enters a non-numeric input during a math challenge, the game may not handle it gracefully (we're working on fixing this).
  
---

## 5. Logbook

### Project Chronology  
- **05/12**: Project setup and initial planning.  
- **05/12**: First round of development completed: math challenges implemented.  
- **12/12**: Implemented key collection system and final treasure room.  
- **05/01**: Final testing and bug fixing.

### Task Distribution  
- **Lino LOZANO**: Main, math challenge roulette, math challenge prime, chance challenge roll dice, logical challenge battleship game, logical challenge nim game, pere fouras challenge, readme
- **Giordano CHAKROUN**: Utility functions, tic-tac-toe game, math challenge equation, math challenge factorial, chance challenge shell game, readme

---

## 6. Testing and Validation

### Test Strategies  
- **Test Case 1**: Player enters a valid answer to a challenge.  
  - **Expected Result**: Player earns a key and the next challenge appears.
- **Test Case 2**: Player enters a non valid answer to a challenge.
  - **Expected Result**: The console remind the player to enter a valid input.
  
**Screenshots**:  
![image](https://github.com/user-attachments/assets/a53ddc44-e61f-4d42-ae7d-46eab5d5bf1d)
![image](https://github.com/user-attachments/assets/81e4db2c-43d8-42dc-89d5-098c4780a5f4)
