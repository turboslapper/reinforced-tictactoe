import pygame, sys
from tqdm import tqdm
from collections import defaultdict
import matplotlib.pyplot as plt
import random
import tkinter as tk
from tkinter import simpledialog

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
graphical_board = [[[None, None], [None, None], [None, None]], 
                    [[None, None], [None, None], [None, None]], 
                    [[None, None], [None, None], [None, None]]]
logical_board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

to_move = 'X'

def render_board(board, ximg, oimg):
    global graphical_board
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                # Create an X image and rect
                graphical_board[i][j][0] = ximg
                graphical_board[i][j][1] = ximg.get_rect(center=(j*300+150, i*300+150))
            elif board[i][j] == 'O':
                graphical_board[i][j][0] = oimg
                graphical_board[i][j][1] = oimg.get_rect(center=(j*300+150, i*300+150))

def add_XO(board, graphical_board, to_move, logical_board):
    current_pos = pygame.mouse.get_pos()
    converted_x = (current_pos[0] - 65) / 835 * 2
    converted_y = current_pos[1] / 835 * 2

    row = round(converted_y)
    col = round(converted_x)

    if board[row][col] != 'O' and board[row][col] != 'X':
        board[row][col] = to_move

        # Update logical_board
        if to_move == 'X':
            logical_board[row][col] = 1  # 1 = X
            to_move = 'O'
        else:
            logical_board[row][col] = 2  # 2 = O
            to_move = 'X'
    
    render_board(board, X_IMG, O_IMG)

    for i in range(3):
        for j in range(3):
            if graphical_board[i][j][0] is not None:
                SCREEN.blit(graphical_board[i][j][0], graphical_board[i][j][1])

    return board, to_move, logical_board

def place_O(board, logical_board, position):
    row, col = position

    # Update the main board with 'O'
    board[row][col] = 'O'

    # Update the logical board with integer 2 (representing O)
    logical_board[row][col] = 2

    return board, logical_board

def place_X(board, logical_board, position):
    row, col = position

    # Update the main board with 'X'
    board[row][col] = 'X'

    # Update the logical board with integer 1 (representing X)
    logical_board[row][col] = 1

    return board, logical_board

def check_win(board):
    winner = None
    for row in range(0, 3):
        if((board[row][0] == board[row][1] == board[row][2]) and (board [row][0] is not None)):
            winner = board[row][0]
            return winner

    for col in range(0, 3):
        if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
            winner =  board[0][col]
            return winner
   
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
        winner =  board[0][0]
        return winner
          
    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
        winner =  board[0][2]
        return winner
    
    if winner is None:
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != 'X' and board[i][j] != 'O':
                    return None
        return "DRAW"

def check_win_update(board):
    winner = None
    for row in range(0, 3):
        if((board[row][0] == board[row][1] == board[row][2]) and (board [row][0] is not None)):
            winner = board[row][0]
            for i in range(0, 3):
                graphical_board[row][i][0] = pygame.image.load(f"/home/codedemon/RLearning/Tic-Tac-Toe/assets/Winning {winner}.png")
                SCREEN.blit(graphical_board[row][i][0], graphical_board[row][i][1])
            pygame.display.update()
            return winner

    for col in range(0, 3):
        if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
            winner =  board[0][col]
            for i in range(0, 3):
                graphical_board[i][col][0] = pygame.image.load(f"/home/codedemon/RLearning/Tic-Tac-Toe/assets/Winning {winner}.png")
                SCREEN.blit(graphical_board[i][col][0], graphical_board[i][col][1])
            pygame.display.update()
            return winner
   
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
        winner =  board[0][0]
        graphical_board[0][0][0] = pygame.image.load(f"/home/codedemon/RLearning/Tic-Tac-Toe/assets/Winning {winner}.png")
        SCREEN.blit(graphical_board[0][0][0], graphical_board[0][0][1])
        graphical_board[1][1][0] = pygame.image.load(f"/home/codedemon/RLearning/Tic-Tac-Toe/assets/Winning {winner}.png")
        SCREEN.blit(graphical_board[1][1][0], graphical_board[1][1][1])
        graphical_board[2][2][0] = pygame.image.load(f"/home/codedemon/RLearning/Tic-Tac-Toe/assets/Winning {winner}.png")
        SCREEN.blit(graphical_board[2][2][0], graphical_board[2][2][1])
        pygame.display.update()
        return winner
          
    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
        winner =  board[0][2]
        graphical_board[0][2][0] = pygame.image.load(f"/home/codedemon/RLearning/Tic-Tac-Toe/assets/Winning {winner}.png")
        SCREEN.blit(graphical_board[0][2][0], graphical_board[0][2][1])
        graphical_board[1][1][0] = pygame.image.load(f"/home/codedemon/RLearning/Tic-Tac-Toe/assets/Winning {winner}.png")
        SCREEN.blit(graphical_board[1][1][0], graphical_board[1][1][1])
        graphical_board[2][0][0] = pygame.image.load(f"/home/codedemon/RLearning/Tic-Tac-Toe/assets/Winning {winner}.png")
        SCREEN.blit(graphical_board[2][0][0], graphical_board[2][0][1])
        pygame.display.update()
        return winner
    
    if winner is None:
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != 'X' and board[i][j] != 'O':
                    return None
        return "DRAW"

def get_empty_spots(logical_board):
    empty_spots = []
    for i in range(3):
        for j in range(3):
            if logical_board[i][j] == 0:
                empty_spots.append((i, j))
    return empty_spots

def print_q_value(q_values):
    print("=== Q-Values Table ===")
    for state, actions in q_values.items():
        print("State:")
        # Convert the state (a tuple of tuples) to a readable grid format
        for row in state:
            print("  " + " ".join(str(cell) for cell in row))
        
        print("Actions and Q-values:")
        for action, q_value in actions.items():
            print(f"  Action {action}: Q-value = {q_value:.2f}")
        print("------------------------")
    print("========================\n")

def print_state_q_values(q_values, state):
    print("=== Q-Values for the Given State ===")
    print("State:")
    for row in state:
        print("  " + " ".join(str(cell) for cell in row))
    print("\nActions and Q-values:")
    if state in q_values:
        actions = q_values[state]
        for action, q_value in actions.items():
            print(f"  Action {action}: Q-value = {q_value:.2f}")
    else:
        print("  No actions available for this state.")
    print("====================================\n")

def prompt_for_rl_params():
    """
    Open a Tkinter dialog to ask the user for three RL parameters:
    1) Max Episodes (integer)
    2) Learning Rate (float)
    3) Discount Factor (float)

    Returns (max_episodes, learning_rate, discount_factor) as a tuple.
    If the user cancels or closes any dialog, defaults are used.
    """

    root = tk.Tk()
    root.withdraw()  # Hide the empty main Tkinter window

    # Prompt for Max Episodes (integer)
    max_episodes = simpledialog.askinteger(
        title="Max Episodes",
        prompt="Enter the number of episodes you want to train for:",
        minvalue=1,
        maxvalue=10_000_000
    )
    if max_episodes is None:
        print("No input provided for max_episodes. Using default = 20000.")
        max_episodes = 20000

    # Prompt for Learning Rate (float)
    learning_rate = simpledialog.askfloat(
        title="Learning Rate",
        prompt="Enter the learning rate (alpha):\n(e.g., 0.1, 0.3, etc.)",
        minvalue=0.000001,
        maxvalue=1.0
    )
    if learning_rate is None:
        print("No input provided for alpha. Using default = 0.3.")
        learning_rate = 0.3

    # Prompt for Discount Factor (float)
    discount_factor = simpledialog.askfloat(
        title="Discount Factor",
        prompt="Enter the discount factor (gamma):\n(e.g., 0.9, 0.99, etc.)",
        minvalue=0.0,
        maxvalue=1.0
    )
    if discount_factor is None:
        print("No input provided for gamma. Using default = 0.9.")
        discount_factor = 0.9

    root.destroy()  # Close the Tkinter root once done

    return max_episodes, learning_rate, discount_factor

game_finished = False

count = 0
win_count = 0
loss_count = 0
stalemate_count = 0
q_values = defaultdict(lambda: defaultdict(float))
epsilon_greedy = 1.0

# Initialize variables
win_rate_history = []
game_intervals = []

max_episodes, learning_rate, discount_factor = prompt_for_rl_params()

pbar = tqdm(total=max_episodes, desc="Training", ncols=80)

while count < max_episodes:
    # (1) The user is about to place X if it's X's turn
    # If game is finished, do resets
    if game_finished:
        board = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]
        graphical_board = [
            [[None, None], [None, None], [None, None]],
            [[None, None], [None, None], [None, None]],
            [[None, None], [None, None], [None, None]]
        ]
        logical_board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        to_move = 'O'
        
        game_finished = False

    if to_move == "X":
        empty_spots = get_empty_spots(logical_board)
        row, col = random.choice(empty_spots)
    
        # Take the chosen action
        place_X(board, logical_board, (row, col))
        
        to_move = 'O'

    else:
        last_state = tuple(tuple(row) for row in logical_board)
        for i in range(3):
            for j in range(3):
                if logical_board[i][j] == 0:  # Check if the cell is empty
                    if (i,j) not in q_values[last_state]:
                        q_values[last_state][(i,j)] = 0.0

        if random.random() <  epsilon_greedy:
            row, col = random.choice(get_empty_spots(logical_board))
        else:
            max_action = max(q_values.get(last_state, {}).items(), key=lambda x: x[1])  # Returns (action, Q-value)
            action, max_value = max_action
            row, col = action

        place_O(board, logical_board, (row,col))

        new_state = tuple(tuple(row) for row in logical_board)
        for i in range(3):
            for j in range(3):
                if logical_board[i][j] == 0:  # Check if the cell is empty
                    if (i,j) not in q_values[new_state]:
                        q_values[new_state][(i,j)] = 0.0

        reward = -0.005
        actions_dict = q_values.get(new_state, {})
        if len(actions_dict) == 0:
            max_value = 0.0
        else:
            action, max_value = max(actions_dict.items(), key=lambda x: x[1])
        q_values[last_state][(row, col)] = q_values[last_state][(row, col)] + learning_rate*(reward + discount_factor*(max_value) - q_values[last_state][(row, col)])

        to_move = 'X'
    
    winner = check_win(board)
    if winner is not None:
        if winner == "X":
            reward = -1
            q_values[last_state][(row, col)] = q_values[last_state][(row, col)] + learning_rate*(reward - q_values[last_state][(row, col)])
            loss_count += 1
        elif winner == "O":
            reward = 1
            q_values[last_state][(row, col)] = q_values[last_state][(row, col)] + learning_rate*(reward - q_values[last_state][(row, col)])
            win_count += 1
        else:
            reward = 0
            q_values[last_state][(row, col)] = q_values[last_state][(row, col)] + learning_rate*(reward - q_values[last_state][(row, col)])
            stalemate_count += 1

        game_finished = True
        # 0.9999 Seems to yield the best results
        epsilon_greedy = max(epsilon_greedy * 0.99, 0.05)
        count += 1
        pbar.update(1)  # Update the progress bar
        if count % 1000 == 0:  # Check if 'count' is a multiple of 500
            current_win_rate = win_count / count  # Calculate the win rate
            win_rate_history.append(current_win_rate)  # Store the win rate
            game_intervals.append(count)  # Store the game interval for x-axis

            # print_q_value(q_values)

            # print(f'At {count} games, the current stats are:')
            # print(f'Wins: {win_count}')
            # print(f'Losses: {loss_count}')
            # print(f'Stalemate: {stalemate_count}')
            # print(f'Current epsilon value: {epsilon_greedy}')
            # print(f'Win rate is {current_win_rate * 100}%')

pbar.close()

print(f'=========== Training Results ===========')
print(f'At {count} games, the current stats are:')
print(f'Wins: {win_count}')
print(f'Losses: {loss_count}')
print(f'Stalemate: {stalemate_count}')
print(f'Current epsilon value: {epsilon_greedy}')
print(f'Win rate is {current_win_rate * 100}%')
# print_q_value(q_values)

play_count = 0
play_win_count = 0
play_loss_count = 0
play_stalemate_count = 0
epsilon_greedy = 0.5

win_rate_history = []
game_intervals = []

game_finished = True

pygame.init()
 
WIDTH, HEIGHT = 900, 900
 
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe!")

BOARD = pygame.image.load("assets/Board.png")
X_IMG = pygame.image.load("assets/X.png")
O_IMG = pygame.image.load("assets/O.png")

BG_COLOR = (214, 201, 227)
SCREEN.fill(BG_COLOR)
SCREEN.blit(BOARD, (64, 64))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if play_count != 0:
                print(f'At {play_count} games, the current stats are:')
                print(f'Wins: {play_win_count}')
                print(f'Losses: {play_loss_count}')
                print(f'Stalemate: {play_stalemate_count}')
                print(f'Current epsilon value: {epsilon_greedy}')
                print(f'Win rate is {(play_win_count/play_count) * 100}%')
                # print_q_value(q_values)

                # After the loop ends, plot the win rate history
                plt.figure(figsize=(10, 6))
                plt.plot(game_intervals, win_rate_history, label="Win Rate", color='blue')
                plt.title("Win Rate Over Time")
                plt.xlabel("Number of Games")
                plt.ylabel("Win Rate")
                plt.grid(True)
                plt.legend()
                plt.show()
            else:
                print("You have not played yet!")
            pygame.quit()
            sys.exit()    
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            # (1) The user is about to place X if it's X's turn
            # If game is finished, do resets
            if game_finished:
                board = [[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9]]
                graphical_board = [
                    [[None, None], [None, None], [None, None]],
                    [[None, None], [None, None], [None, None]],
                    [[None, None], [None, None], [None, None]]
                ]
                logical_board = [
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]
                ]
                to_move = 'O'
                
                SCREEN.fill(BG_COLOR)
                SCREEN.blit(BOARD, (64, 64))
                game_finished = False
                pygame.display.update()

            if to_move == "X":

                add_XO(board, graphical_board, "X", logical_board)

                render_board(board, X_IMG, O_IMG)
                for i in range(3):
                    for j in range(3):
                        if graphical_board[i][j][0] is not None:
                            SCREEN.blit(graphical_board[i][j][0], graphical_board[i][j][1])
                pygame.display.update()

                to_move = "O"
            # The reason there has to be an else is that it should check after every move if there is a winner
            # For example, if X (you) moves last and you win, O will still go despite the game being over and then O will win 
            # Since the terminal states are checked after O in the code, even though your move (X) should've ended the game
            else:
                last_state = tuple(tuple(row) for row in logical_board)
                for i in range(3):
                    for j in range(3):
                        if logical_board[i][j] == 0:  # Check if the cell is empty
                            if (i,j) not in q_values[last_state]:
                                q_values[last_state][(i,j)] = 0.0

                if random.random() <  epsilon_greedy:
                    row, col = random.choice(get_empty_spots(logical_board))
                    print(f"We chose to explore: ({row, col})")
                else:
                    # print_state_q_values(q_values, last_state)
                    max_action = max(q_values.get(last_state, {}).items(), key=lambda x: x[1])  # Returns (action, Q-value)
                    action, max_value = max_action
                    print_state_q_values(q_values, last_state)
                    print(f'We chose {action} with value: {max_value}')
                    row, col = action

                place_O(board, logical_board, (row,col))

                render_board(board, X_IMG, O_IMG)
                for i in range(3):
                    for j in range(3):
                        if graphical_board[i][j][0] is not None:
                            SCREEN.blit(graphical_board[i][j][0], graphical_board[i][j][1])
                pygame.display.update()

                new_state = tuple(tuple(row) for row in logical_board)
                for i in range(3):
                    for j in range(3):
                        if logical_board[i][j] == 0:  # Check if the cell is empty
                            if (i,j) not in q_values[new_state]:
                                q_values[new_state][(i,j)] = 0.0

                reward = 0.0
                actions_dict = q_values.get(new_state, {})
                if len(actions_dict) == 0:
                    max_value = 0.0
                else:
                    action, max_value = max(actions_dict.items(), key=lambda x: x[1])
                q_values[last_state][(row, col)] = q_values[last_state][(row, col)] + learning_rate*(reward + discount_factor*(max_value) - q_values[last_state][(row, col)])

                to_move = 'X'

            winner = check_win_update(board)
            if winner is not None:
                if winner == "X":
                    reward = -1
                    q_values[last_state][(row, col)] = q_values[last_state][(row, col)] + learning_rate*(reward - q_values[last_state][(row, col)])
                    play_loss_count += 1
                elif winner == "O":
                    reward = 1
                    q_values[last_state][(row, col)] = q_values[last_state][(row, col)] + learning_rate*(reward - q_values[last_state][(row, col)])
                    play_win_count += 1
                else:
                    reward = 0
                    q_values[last_state][(row, col)] = q_values[last_state][(row, col)] + learning_rate*(reward - q_values[last_state][(row, col)])
                    play_stalemate_count += 1

                game_finished = True
                # 0.9999 Seems to yield the best results
                epsilon_greedy = max(epsilon_greedy * 0.99, 0.05)
                play_count += 1
                if play_count % 3 == 0:  # Check if 'play_count' is a multiple of 500
                    current_win_rate = play_win_count / play_count  # Calculate the win rate
                    win_rate_history.append(current_win_rate)  # Store the win rate
                    game_intervals.append(play_count)  # Store the game interval for x-axis

                    print(f'At {play_count} games, the current stats are:')
                    print(f'Wins: {play_win_count}')
                    print(f'Losses: {play_loss_count}')
                    print(f'Stalemate: {play_stalemate_count}')
                    print(f'Current epsilon value: {epsilon_greedy}')
                    print(f'Win rate is {current_win_rate * 100}%')
