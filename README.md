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

### Technologies Used  
- **Programming Language**: Python 3.
- **Python Libraries**:  
  - `random`: For random generation of challenges.  
  - `json`: For saving and loading player scores.

---

## 2. Installation

1. **Clone the repository**:  
   ```bash
   git clone https://github.com/your-username/fort-boyard-maths.git
   cd fort-boyard-maths
   ```
---

## 3. How to Use

To start the game, run the following command in your terminal:  
```bash
python main.py
```

Follow the on-screen instructions to play through various challenges. You will be given a set of math tasks, and you must solve them within the given time (for timed challenges). Once you collect enough keys, you will access the treasure room for the final challenge!

---

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
- **[Date1]**: Project setup and initial planning.  
- **[Date2]**: First round of development completed: math challenges implemented.  
- **[Date3]**: Implemented key collection system and final treasure room.  
- **[Date4]**: Final testing and bug fixing.

### Task Distribution  
- **[Name1]**: Worked on developing math challenges and implementing the logic for generating random problems.  
- **[Name2]**: Focused on developing the key system, managing the game flow, and saving scores.  
- **[Name3]**: Handled documentation, testing the game, and fixing minor bugs.

---

## 6. Testing and Validation

### Test Strategies  
- **Test Case 1**: Player enters a valid answer to a math challenge.  
  - **Expected Result**: Player earns a key and the next challenge appears.
- **Test Case 2**: Player runs out of time in a timed challenge.  
  - **Expected Result**: Player loses a chance, and the next challenge is presented.
  
**Screenshots**:  
(Include screenshots of the game running in the console, showing test cases in action.)

---

## 7. License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
