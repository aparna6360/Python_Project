import tkinter as tk
from tkinter import messagebox

theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

# Define winning combinations
winning_combinations = [
    ('7', '8', '9'), ('4', '5', '6'), ('1', '2', '3'),  # rows
    ('1', '4', '7'), ('2', '5', '8'), ('3', '6', '9'),  # columns
    ('1', '5', '9'), ('3', '5', '7')                    # diagonals
]

# Initialize variables
turn = 'X'
count = 0
winner = None


# Function to handle the player's move
def player_move(position):
    global turn, count
    if theBoard[position] == ' ':
        theBoard[position] = turn
        count += 1
        if turn == 'X':
            buttons[position].config(text='X', state='disabled')
            turn = 'O'
        else:
            buttons[position].config(text='O', state='disabled')
            turn = 'X'
        check_winner()
        check_tie()
    else:
        messagebox.showerror("Error", "That place is already filled.")

# Function to check if there is a winner
def check_winner():
    global winner
    for combo in winning_combinations:
        if theBoard[combo[0]] == theBoard[combo[1]] == theBoard[combo[2]] != ' ':
            winner = theBoard[combo[0]]
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            disable_buttons()
            return

# Function to check if the game is a tie
def check_tie():
    if count == 9 and winner ==None:
        messagebox.showinfo("Game Over", "It's a Tie!")
        disable_buttons()

# Function to disable all buttons after the game ends
def disable_buttons():
    for button in buttons.values():
        button.config(state='disabled')

# Function to restart the game
def restart_game():
    global theBoard, count, turn, winner
    theBoard = {'7': ' ', '8': ' ', '9': ' ',
                '4': ' ', '5': ' ', '6': ' ',
                '1': ' ', '2': ' ', '3': ' '}
    count = 0
    turn = 'X'
    winner = None
    for position, button in buttons.items():
        button.config(text='', state='normal')

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")


# Create buttons for each position on the board
buttons = {}
for i in range(3):
    for j in range(3):
        position = str(i * 3 + j + 1)
        buttons[position] = tk.Button(root, text='', width=10, height=5,
                                       command=lambda pos=position: player_move(pos))
        buttons[position].grid(row=i, column=j)



# Create a restart button
restart_button = tk.Button(root, text='Restart', command=restart_game)
restart_button.grid(row=3, columnspan=3)

# Run the main loop
root.mainloop()