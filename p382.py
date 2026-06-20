import tkinter as tk
from tkinter import messagebox
import random
import winsound  # For sound effects (Windows only)
from PIL import Image, ImageTk  # For handling images

# Snake and ladder positions
snake = {28: 10, 37: 3, 48: 16, 75: 32, 94: 71, 96: 42}
ladder = {4: 56, 12: 50, 14: 55, 22: 58, 41: 79, 54: 88}

# Player positions
totalp1 = 1
totalp2 = 1
turn = 1

# Setup GUI
root = tk.Tk()
root.title("🐍 Snake & Ladder 🪜")
root.geometry("750x850")
root.configure(bg="#FFF3E0")

# Title label
title_label = tk.Label(root, text="🐍 Snake & Ladder 🪜", font=("Comic Sans MS", 28, "bold"), fg="#4A148C", bg="#FFF3E0")
title_label.pack(pady=10)

# Canvas
canvas = tk.Canvas(root, width=600, height=600, bd=0, highlightthickness=0)
canvas.pack(pady=20)

cell_size = 60
positions_map = {}

# Background image for the board
bg_image = Image.open("background_image.jpg")
bg_image = bg_image.resize((600, 600))  # Resize to fit the canvas
bg_photo = ImageTk.PhotoImage(bg_image)

canvas.create_image(0, 0, anchor="nw", image=bg_photo)  # Place the background

# Draw the grid
colors = ["#FDEBD0", "#FADBD8"]
for row in range(10):
    for col in range(10):
        x1 = col * cell_size
        y1 = (9 - row) * cell_size
        x2 = x1 + cell_size
        y2 = y1 + cell_size

        pos_num = row * 10 + (col + 1 if row % 2 == 0 else 10 - col)
        positions_map[pos_num] = (x1 + 30, y1 + 30)

        color = colors[(row + col) % 2]
        canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
        canvas.create_text(x1 + 5, y1 + 5, anchor="nw", text=str(pos_num), font=("Helvetica", 9, "bold"))

# Load snake and ladder images
snake_img = Image.open("snake_image.png")  # Add snake image here
ladder_img = Image.open("ladder_image.png")  # Add ladder image here

# Resize images to fit the cells
snake_img = snake_img.resize((cell_size, cell_size))
ladder_img = ladder_img.resize((cell_size, cell_size))

# Place the snake and ladder images on the board
for start, end in snake.items():
    x1, y1 = positions_map[start]
    x2, y2 = positions_map[end]
    canvas.create_image(x1, y1, anchor="center", image=ImageTk.PhotoImage(snake_img))  # Snake image

for start, end in ladder.items():
    x1, y1 = positions_map[start]
    x2, y2 = positions_map[end]
    canvas.create_image(x1, y1, anchor="center", image=ImageTk.PhotoImage(ladder_img))  # Ladder image

# Player tokens (rounded with shadow)
def draw_token(x, y, color, tag, offset=0):
    shadow = canvas.create_oval(x-10+2, y-10+offset+2, x+10+2, y+10+offset+2, fill="#888888", outline="")
    token = canvas.create_oval(x-10, y-10+offset, x+10, y+10+offset, fill=color, tags=tag)
    return token

p1_token = draw_token(*positions_map[1], "red", "p1", offset=-5)
p2_token = draw_token(*positions_map[1], "blue", "p2", offset=5)

# Status label
status_label = tk.Label(root, text="Player 1's Turn", font=("Helvetica", 14), bg="#FFF3E0", fg="#4A148C")
status_label.pack()

# Move player token
def move_player(player, position):
    position = min(position, 100)
    x, y = positions_map[position]
    if player == 1:
        canvas.coords("p1", x-10, y-15, x+10, y+5)
    else:
        canvas.coords("p2", x-10, y+5, x+10, y+25)

# Roll dice function with animation
def roll_dice(player):
    global totalp1, totalp2, turn
    dice = random.randint(1, 6)

    if player == 1 and turn % 2 != 0:
        status_label.config(text=f"Player 1 rolled a {dice}")
        totalp1 += dice
        msg = ""
        if totalp1 > 100:
            messagebox.showwarning("Invalid Move", "The number you rolled exceeds the remaining boxes to 100!")
            totalp1 -= dice  # Undo the invalid move
        elif totalp1 in snake:
            totalp1 = snake[totalp1]
            msg = "🐍 Oh no! Player 1 got bitten by a snake!"
        elif totalp1 in ladder:
            totalp1 = ladder[totalp1]
            msg = "🪜 Woohoo! Player 1 climbed a ladder!"
        move_player(1, totalp1)
        if msg:
            messagebox.showinfo("Game Update", msg)
        if totalp1 >= 100:
            messagebox.showinfo("🎉 Game Over", "Player 1 Wins!")
            save_game_result("Player 1 Wins!")
            root.quit()
        turn += 1
        status_label.config(text="Player 2's Turn")

    elif player == 2 and turn % 2 == 0:
        status_label.config(text=f"Player 2 rolled a {dice}")
        totalp2 += dice
        msg = ""
        if totalp2 > 100:
            messagebox.showwarning("Invalid Move", "The number you rolled exceeds the remaining boxes to 100!")
            totalp2 -= dice  # Undo the invalid move
        elif totalp2 in snake:
            totalp2 = snake[totalp2]
            msg = "🐍 Oh no! Player 2 got bitten by a snake!"
        elif totalp2 in ladder:
            totalp2 = ladder[totalp2]
            msg = "🪜 Woohoo! Player 2 climbed a ladder!"
        move_player(2, totalp2)
        if msg:
            messagebox.showinfo("Game Update", msg)
        if totalp2 >= 100:
            messagebox.showinfo("🎉 Game Over", "Player 2 Wins!")
            save_game_result("Player 2 Wins!")
            root.quit()
        turn += 1
        status_label.config(text="Player 1's Turn")

# Function to save the game result
def save_game_result(winner):
    with open("game_results.txt", "w") as file:
        file.write(f"Winner: {winner}\n")
        file.write(f"Player 1's final position: {totalp1}\n")
        file.write(f"Player 2's final position: {totalp2}\n")
        file.write(f"Total moves taken: {turn // 2}\n")

# Restart Game function
def restart_game():
    global totalp1, totalp2, turn
    totalp1 = 1
    totalp2 = 1
    turn = 1
    status_label.config(text="Player 1's Turn")
    canvas.delete("all")  # Clear the canvas
    canvas.create_image(0, 0, anchor="nw", image=bg_photo)  # Recreate the background
    # Redraw the grid, snake, ladder, and player tokens
    # (Same drawing code as above)

# Buttons
btn_frame = tk.Frame(root, bg="#FFF3E0")
btn_frame.pack(pady=10)

btn1 = tk.Button(btn_frame, text="🎲 Roll Dice - Player 1", font=("Helvetica", 12, "bold"),
                 bg="#F8BBD0", fg="black", command=lambda: roll_dice(1))
btn1.grid(row=0, column=0, padx=15)

btn2 = tk.Button(btn_frame, text="🎲 Roll Dice - Player 2", font=("Helvetica", 12, "bold"),
                 bg="#BBDEFB", fg="black", command=lambda: roll_dice(2))
btn2.grid(row=0, column=1, padx=15)

# Restart button
restart_btn = tk.Button(btn_frame, text="🔁 Restart Game", font=("Helvetica", 12, "bold"),
                        bg="#A5D6A7", fg="black", command=restart_game)
restart_btn.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
