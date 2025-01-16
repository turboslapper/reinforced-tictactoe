# Tic Tac Toe with Reinforcement Learning

## Description
This project implements a Tic Tac Toe game with reinforcement learning. The program trains an AI agent to play Tic Tac Toe by learning optimal strategies through self-play and exploration. The agent uses Q-learning to update its state-action values based on rewards received during gameplay.

The game also includes:
- A graphical interface built with Pygame.
- A training mode where the agent learns by playing games.
- The option to play against the trained agent.

---

## Features
1. **Reinforcement Learning**
   - Implements Q-learning to train the AI agent.
   - Adjustable learning rate and discount factor.
   - Exploration and exploitation using epsilon-greedy strategy.

2. **Graphical Interface**
   - Built using Pygame.
   - Displays the game board and player moves in real time.
   - Highlights winning moves visually.
   - Taken from https://www.youtube.com/watch?v=IL_PMGVxEUY&t=769s (Thank you BaralTech)

4. **Training Mode**
   - Allows the agent to train by playing games against itself or a random opponent.
   - Tracks win rates and adjusts strategies over time.

5. **Interactive Gameplay**
   - Enables human players to play against the AI agent.
   - Configurable difficulty through adjustable epsilon-greedy settings.

---

## Installation
### Prerequisites
- Python 3.8+
- Required libraries:
  - `pygame`
  - `tqdm`
  - `matplotlib`
  - `tkinter`

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/turboslapper/reinforced-tictactoe.git
   cd reinforced-tictactoe
   ```
2. Install dependencies:
   ```bash
   pip install pygame tqdm matplotlib
   ```
3. Run the program:
   ```bash
   python opp_random.py
   ```

---

## How to Use
### Training Mode
1. Upon starting, you'll be prompted to set:
   - **Max Episodes**: Number of games to train the agent.
   - **Learning Rate (Alpha)**: Speed of learning.
   - **Discount Factor (Gamma)**: Importance of future rewards.
2. The agent trains against a random opponent (`opp_random.py`) or through self-play (`opp_self-play.py`).
3. Outputs training stats to the console and optionally logs progress.

### Playing Against the Agent
1. After training, you can run the program to play against the agent.
2. Click on the graphical board to make your moves.
3. Watch the AI adapt and respond to your playstyle!

---

## File Structure
```
├── assets/
│   └── .gitignore
├── README.md
├── learning_example.txt
├── opp_random.py
├── opp_self-play.py
```
- `assets/`: Folder containing images for the board and player symbols (X and O).
- `README.md`: Project documentation.
- `learning_example.txt`: Example of the agent learning, observe the Q values!
- `opp_random.py`: Training and playing with a random opponent.
- `opp_self-play.py`: Training through self-play.

---

## Customization
- Modify learning parameters (learning rate, discount factor, epsilon) for experimentation.
- Add more advanced opponent strategies for a more challenging training environment.
- Customize the graphical interface by editing assets in the `assets/` folder.

---

## Troubleshooting
- If you encounter errors with Pygame, ensure all dependencies are installed.
- Use `print_q_value(q_values)` to debug the Q-values during training.

---

## Acknowledgments
- Reinforcement learning concepts (heavily) inspired by Sutton and Barto's "Reinforcement Learning: An Introduction."
- Graphics powered by Pygame.
- Progress tracking with TQDM.
