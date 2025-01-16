import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
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

    board[row][col] = 'O'

    logical_board[row][col] = 2

    return board, logical_board

def place_X(board, logical_board, position):
    row, col = position

    board[row][col] = 'X'

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
                graphical_board[row][i][0] = pygame.image.load(f"assets/Winning {winner}.png")
                SCREEN.blit(graphical_board[row][i][0], graphical_board[row][i][1])
            pygame.display.update()
            return winner

    for col in range(0, 3):
        if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
            winner =  board[0][col]
            for i in range(0, 3):
                graphical_board[i][col][0] = pygame.image.load(f"assets/Winning {winner}.png")
                SCREEN.blit(graphical_board[i][col][0], graphical_board[i][col][1])
            pygame.display.update()
            return winner
   
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
        winner =  board[0][0]
        graphical_board[0][0][0] = pygame.image.load(f"assets/Winning {winner}.png")
        SCREEN.blit(graphical_board[0][0][0], graphical_board[0][0][1])
        graphical_board[1][1][0] = pygame.image.load(f"assets/Winning {winner}.png")
        SCREEN.blit(graphical_board[1][1][0], graphical_board[1][1][1])
        graphical_board[2][2][0] = pygame.image.load(f"assets/Winning {winner}.png")
        SCREEN.blit(graphical_board[2][2][0], graphical_board[2][2][1])
        pygame.display.update()
        return winner
          
    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
        winner =  board[0][2]
        graphical_board[0][2][0] = pygame.image.load(f"assets/Winning {winner}.png")
        SCREEN.blit(graphical_board[0][2][0], graphical_board[0][2][1])
        graphical_board[1][1][0] = pygame.image.load(f"assets/Winning {winner}.png")
        SCREEN.blit(graphical_board[1][1][0], graphical_board[1][1][1])
        graphical_board[2][0][0] = pygame.image.load(f"assets/Winning {winner}.png")
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

    root = tk.Tk()
    root.withdraw() 

    max_episodes = simpledialog.askinteger(
        title="Max Episodes",
        prompt="Enter the number of episodes you want to train for:",
        minvalue=1,
        maxvalue=10_000_000
    )
    if max_episodes is None:
        print("No input provided for max_episodes. Using default = 20000.")
        max_episodes = 20000

    learning_rate = simpledialog.askfloat(
        title="Learning Rate",
        prompt="Enter the learning rate (alpha):\n(e.g., 0.1, 0.3, etc.)",
        minvalue=0.000001,
        maxvalue=1.0
    )
    if learning_rate is None:
        print("No input provided for alpha. Using default = 0.3.")
        learning_rate = 0.3

    discount_factor = simpledialog.askfloat(
        title="Discount Factor",
        prompt="Enter the discount factor (gamma):\n(e.g., 0.9, 0.99, etc.)",
        minvalue=0.0,
        maxvalue=1.0
    )
    if discount_factor is None:
        print("No input provided for gamma. Using default = 0.9.")
        discount_factor = 0.9

    root.destroy()  

    return max_episodes, learning_rate, discount_factor

def prompt_for_player_choice():
    def set_choice(selected_choice):
        nonlocal choice
        choice = selected_choice
        root.destroy()  # Close the window once a choice is made

    root = tk.Tk()
    root.title("Player Choice")

    # Set the window size and position
    root.geometry("300x150")
    root.eval('tk::PlaceWindow . center')  # Center the window

    # Add label
    label = tk.Label(root, text="Would you like to go first or second?", font=("Helvetica", 12))
    label.pack(pady=10)

    # Add buttons for "X" and "O"
    button_x = tk.Button(root, text="First", font=("Helvetica", 14), width=10, command=lambda: set_choice("X"))
    button_x.pack(pady=5)

    button_o = tk.Button(root, text="Second", font=("Helvetica", 14), width=10, command=lambda: set_choice("O"))
    button_o.pack(pady=5)

    # Initialize choice
    choice = None
    root.mainloop()  # Run the Tkinter event loop

    # Default to "X" if no choice was made (e.g., the window was closed)
    if choice is None:
        choice = "X"

    return choice


game_finished = False

count = 0
win_count = 0
loss_count = 0
stalemate_count = 0
q_values = defaultdict(lambda: defaultdict(float))
epsilon_greedy = 1.0

x_q_values = defaultdict(lambda: defaultdict(float))
x_epsilon_greedy = 1.0
x_learning_rate = 0.3
x_discount_factor = 0.9

win_rate_history = []
game_intervals = []

max_episodes, learning_rate, discount_factor = prompt_for_rl_params()
player_choice = prompt_for_player_choice()

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
        to_move = player_choice
        
        game_finished = False

    if to_move == "X":
        x_last_state = tuple(tuple(row) for row in logical_board)
        for i in range(3):
            for j in range(3):
                if logical_board[i][j] == 0: 
                    if (i,j) not in x_q_values[x_last_state]:
                        x_q_values[x_last_state][(i,j)] = 0.0

        if random.random() <  x_epsilon_greedy:
            row1, col1 = random.choice(get_empty_spots(logical_board))
        else:
            max_action1 = max(x_q_values.get(x_last_state, {}).items(), key=lambda x: x[1]) 
            action1, max_value1 = max_action1
            row1, col1 = action1

        place_X(board, logical_board, (row1, col1))

        x_new_state = tuple(tuple(row) for row in logical_board)
        for i in range(3):
            for j in range(3):
                if logical_board[i][j] == 0:
                    if (i,j) not in x_q_values[x_new_state]:
                        x_q_values[x_new_state][(i,j)] = 0.0

        reward1 = 0
        actions_dict1 = x_q_values.get(x_new_state, {})
        if len(actions_dict1) == 0:
            max_value1 = 0.0
        else:
            action1, max_value1 = max(actions_dict1.items(), key=lambda x: x[1])
        x_q_values[x_last_state][(row1, col1)] = x_q_values[x_last_state][(row1, col1)] + x_learning_rate*(reward1 + x_discount_factor*(max_value1) - x_q_values[x_last_state][(row1, col1)])

        to_move = 'O'

    else:
        last_state = tuple(tuple(row) for row in logical_board)
        for i in range(3):
            for j in range(3):
                if logical_board[i][j] == 0: 
                    if (i,j) not in q_values[last_state]:
                        q_values[last_state][(i,j)] = 0.0

        if random.random() <  epsilon_greedy:
            row, col = random.choice(get_empty_spots(logical_board))
        else:
            max_action = max(q_values.get(last_state, {}).items(), key=lambda x: x[1]) 
            action, max_value = max_action
            row, col = action

        place_O(board, logical_board, (row,col))

        new_state = tuple(tuple(row) for row in logical_board)
        for i in range(3):
            for j in range(3):
                if logical_board[i][j] == 0:
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
            x_q_values[x_last_state][(row1, col1)] = x_q_values[x_last_state][(row1, col1)] + x_learning_rate*(1 - x_q_values[x_last_state][(row1, col1)])
            q_values[last_state][(row, col)] = q_values[last_state][(row, col)] + learning_rate*(reward - q_values[last_state][(row, col)])
            loss_count += 1
        elif winner == "O":
            reward = 1
            x_q_values[x_last_state][(row1, col1)] = x_q_values[x_last_state][(row1, col1)] + x_learning_rate*(-1 - x_q_values[x_last_state][(row1, col1)])
            q_values[last_state][(row, col)] = q_values[last_state][(row, col)] + learning_rate*(reward - q_values[last_state][(row, col)])
            win_count += 1
        else:
            reward = 0
            x_q_values[x_last_state][(row1, col1)] = x_q_values[x_last_state][(row1, col1)] + x_learning_rate*(0 - x_q_values[x_last_state][(row1, col1)])
            q_values[last_state][(row, col)] = q_values[last_state][(row, col)] + learning_rate*(reward - q_values[last_state][(row, col)])
            stalemate_count += 1

        game_finished = True
        # 0.9999 Seems to yield the best results
        epsilon_greedy = max(epsilon_greedy * 0.99, 0.05)
        count += 1
        pbar.update(1) 
        # if count % 100 == 0: 
        #     current_win_rate = win_count / count 
        #     win_rate_history.append(current_win_rate) 
        #     game_intervals.append(count) 

        #     print_q_value(q_values)

        #     print(f'At {count} games, the current stats are:')
        #     print(f'Wins: {win_count}')
        #     print(f'Losses: {loss_count}')
        #     print(f'Stalemate: {stalemate_count}')
        #     print(f'Current epsilon value: {epsilon_greedy}')
        #     print(f'Win rate is {current_win_rate * 100}%')

pbar.close()

print(f'=========== Training Results ===========')
print(f'At {count} games, the current stats are:')
print(f'Wins: {win_count}')
print(f'Losses: {loss_count}')
print(f'Stalemate: {stalemate_count}')
print(f'Current epsilon value: {epsilon_greedy}')
print(f'Win rate is {(win_count/count) * 100}%')
# print_q_value(q_values)

play_count = 0
play_win_count = 0
play_loss_count = 0
play_stalemate_count = 0
epsilon_greedy = 0.4

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
                to_move = player_choice
                
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
                        if logical_board[i][j] == 0:
                            if (i,j) not in q_values[last_state]:
                                q_values[last_state][(i,j)] = 0.0

                if random.random() <  epsilon_greedy:
                    row, col = random.choice(get_empty_spots(logical_board))
                    print(f"We chose to explore: ({row, col})")
                else:
                    # print_state_q_values(q_values, last_state)
                    max_action = max(q_values.get(last_state, {}).items(), key=lambda x: x[1])  
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
                        if logical_board[i][j] == 0:
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
                epsilon_greedy = max(epsilon_greedy * 0.93, 0.1)
                play_count += 1
                win_rate = play_win_count / play_count 
                win_rate_history.append(win_rate)  
                game_intervals.append(play_count) 
                if play_count % 3 == 0: 
                    print(f'At {play_count} games, the current stats are:')
                    print(f'Wins: {play_win_count}')
                    print(f'Losses: {play_loss_count}')
                    print(f'Stalemate: {play_stalemate_count}')
                    print(f'Current epsilon value: {epsilon_greedy}')
                    print(f'Win rate is {win_rate * 100}%')
