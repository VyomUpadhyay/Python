import tkinter as tk
from tkinter import messagebox
import time
from colorama import Fore

turn = 1
list1 = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
Name1 = str(input("Enter the name of Player 1 -> "))
Name2 = str(input("Enter the name of Player 2 -> "))

# Set up the main game window
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("400x400")
root.configure(bg="lightblue")

# Title Label with nice font and centered
title_label = tk.Label(root, text="Tic Tac Toe", font=("Comic Sans MS", 24, "bold"), bg="lightblue", fg="darkblue")
title_label.grid(row=0, column=0, columnspan=3, pady=10)

# Status label with nice font and centered
status_label = tk.Label(root, text="Player 1's Turn", font=("Comic Sans MS", 14), bg="lightblue", fg="red")
status_label.grid(row=1, column=0, columnspan=3, pady=10)


# Function to update the status based on the current player's turn
def update_status():
    if turn % 2 == 0:
        status_label.config(text=f"{Name1}'s Turn (X)", fg="red")
    else:
        status_label.config(text=f"{Name2}'s Turn (O)", fg="blue")


# Function to check the winner
def check_winner():
    for i in range(3):
        # Check rows and columns
        if list1[i * 3] == list1[i * 3 + 1] == list1[i * 3 + 2] != "_":
            return list1[i * 3]
        if list1[i] == list1[i + 3] == list1[i + 6] != "_":
            return list1[i]

    # Check diagonals
    if list1[0] == list1[4] == list1[8] != "_":
        return list1[0]
    if list1[2] == list1[4] == list1[6] != "_":
        return list1[2]

    return None


# Function to reset the game
def reset_game():
    global turn
    turn = 1
    for i in range(9):
        list1[i] = "_"
        buttons[i].config(text="_", bg="lightgray")
    status_label.config(text="Player 1's Turn", fg="red")


# Function to handle button click
def on_button_click(i):
    global turn
    if list1[i] != "_":
        return
    if turn % 2 == 0:
        list1[i] = "X"
        buttons[i].config(text="X", fg="red", bg="lightyellow", font=("Comic Sans MS", 20))
    else:
        list1[i] = "O"
        buttons[i].config(text="O", fg="blue", bg="lightgreen", font=("Comic Sans MS", 20))

    # Check for winner
    winner = check_winner()
    if winner:
        winner_name = Name1 if winner == "X" else Name2
        messagebox.showinfo("Winner", f"{winner_name} Wins!")
        reset_game()
    elif "_" not in list1:
        messagebox.showinfo("Tie", "It's a Tie!")
        reset_game()
    else:
        turn += 1
        update_status()


# Create the buttons and grid layout
buttons = []
for i in range(9):
    button = tk.Button(root, text="_", font=("Comic Sans MS", 20), width=10, height=3,
                       command=lambda i=i: on_button_click(i), bg="lightgray", relief="solid", bd=3)
    button.grid(row=2 + i // 3, column=i % 3, padx=10, pady=10)

    buttons.append(button)

# Center the grid layout on the window by applying the column and row configurations
for i in range(3):
    root.grid_columnconfigure(i, weight=1, uniform="equal")
    root.grid_rowconfigure(i + 2, weight=1, uniform="equal")

# Start the game
update_status()
root.mainloop()