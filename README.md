# Fort Boyard - Math Challenges in Console

---

## 1. General Presentation

### Project Title  
**Fort Boyard - Math Challenges in Console**

### Contributors  
- **Lino Lozano** 
- **Giordano Chakroun** 

### Description  
In this project, you are immersed in the world of *Fort Boyard*, but this time, everything happens in the console and revolves around math challenges! Each player must solve puzzles and math challenges to collect keys and progress toward the treasure room.

### Key Features  
- **Varied Math Challenges**: Challenges range from mental arithmetic to logic puzzles, solving equations, and numeric sequences.
- **Key Collection**: Players need to complete challenges to earn keys, each unlocking progress toward the treasure room.
- **Score System**: Scores are saved and can be compared among players.
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
2. The player chooses a challenge.
3. The system generates random parameters for the selected challenge.
4. The player submits their answer:
   - If the answer is correct, the player earns a key.
   - If the answer is incorrect, they lose a chance.
5. The player continues solving challenges until they have enough keys or fail too many times.
6. If the player collects enough keys, they unlock the treasure room and face a final puzzle.

### Functions

| **Function**              | **Description**                                                                                          | **Parameters**              |
|---------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------|
| `start_game()`            | Starts the game and initializes the necessary variables.                                                  | None                        |
| `generate_challenge()`    | Generates a challenge based on the selected type (math, logic, etc.).                                      | `type`: Type of challenge.  |
| `check_answer()`          | Checks if the player's answer is correct.                                                                | `answer`: Player's answer.  |
| `save_score()`            | Saves the player's score to a JSON file.                                                                  | `score`: Player's score.    |
| `load_scores()`           | Loads previous scores from the JSON file.                                                                | None                        |

### Input and Error Management  
- **Input Validation**: The game ensures that user input is in the correct format (numbers, expressions).  
- **Error Management**: If the user provides invalid input or a timeout occurs, the game will prompt them again.
  
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
- **Lino LOZANO**: Worked on developing math challenges and implementing the logic for generating random problems.  
- **Giordano CHAKROUN**: Focused on developing the key system and help with the logical challenges

---

## 6. Testing and Validation

### Test Strategies  
- **Test Case 1**: Player enters a valid answer to a challenge.  
  - **Expected Result**: Player earns a key and the next challenge appears.
- **Test Case 2**: Player enters a non valid answer to a challenge.
  - - **Expected Result**: The console remind the player to enter a valid input.
  
**Screenshots**:  
![image](https://github.com/user-attachments/assets/a53ddc44-e61f-4d42-ae7d-46eab5d5bf1d)
![image](https://github.com/user-attachments/assets/81e4db2c-43d8-42dc-89d5-098c4780a5f4)
