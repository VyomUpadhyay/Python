import tkinter as tk
from tkinter import messagebox
import random
import math
import winsound  # For sound effects (Windows only)

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
canvas = tk.Canvas(root, width=600, height=600, bg="#FAF3DD", bd=0, highlightthickness=0)
canvas.pack(pady=20)

cell_size = 60
positions_map = {}

# Draw the board with alternating colors
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

# Draw curved snakes and ladders
def draw_curved_line(x1, y1, x2, y2, color, emoji):
    steps = 20
    for i in range(steps):
        t = i / steps
        xt = (1 - t) * x1 + t * x2 + 20 * math.sin(t * math.pi * 4)
        yt = (1 - t) * y1 + t * y2 + 20 * math.cos(t * math.pi * 4)
        canvas.create_oval(xt - 2, yt - 2, xt + 2, yt + 2, fill=color, outline=color)
    canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=emoji, font=("Arial", 16, "bold"))

for start, end in snake.items():
    x1, y1 = positions_map[start]
    x2, y2 = positions_map[end]
    draw_curved_line(x1, y1, x2, y2, "#D32F2F", "🐍")

for start, end in ladder.items():
    x1, y1 = positions_map[start]
    x2, y2 = positions_map[end]
    draw_curved_line(x1, y1, x2, y2, "#388E3C", "🪜")

# Player tokens (rounded with shadow)
def draw_token(x, y, color, tag, offset=0):
    shadow = canvas.create_oval(x - 10 + 2, y - 10 + offset + 2, x + 10 + 2, y + 10 + offset + 2, fill="#888888",
                                outline="")
    token = canvas.create_oval(x - 10, y - 10 + offset, x + 10, y + 10 + offset, fill=color, tags=tag)
    return token

p1_token = draw_token(*positions_map[1], "red", "p1", offset=-5)
p2_token = draw_token(*positions_map[1], "blue", "p2", offset=5)

# Status label
status_label = tk.Label(root, text="Player 1's Turn", font=("Helvetica", 14), bg="#FFF3E0", fg="#4A148C")
status_label.pack()

# Sound effects
def play_sound(effect):
    if effect == "snake":
        winsound.Beep(500, 500)  # Example beep for snake bite
    elif effect == "ladder":
        winsound.Beep(1000, 500)  # Example beep for ladder climb

# Move player token
def move_player(player, position):
    position = min(position, 100)
    x, y = positions_map[position]
    if player == 1:
        canvas.coords("p1", x - 10, y - 15, x + 10, y + 5)
    else:
        canvas.coords("p2", x - 10, y + 5, x + 10, y + 25)

# Dice roll animation function
def animate_dice_roll(player):
    dice = random.randint(1, 6)
    num_rolls = 10

    def update_roll(count):
        nonlocal dice
        if count < num_rolls:
            dice_display = random.randint(1, 6)  # Random number for animation
            status_label.config(text=f"Player {player} rolled a {dice_display}")
            root.after(100, update_roll, count + 1)
        else:
            dice = random.randint(1, 6)  # Final roll value
            status_label.config(text=f"Player {player} rolled a {dice}")
            process_roll(player, dice)

    update_roll(0)

# Process the roll after animation
def process_roll(player, dice):
    global totalp1, totalp2, turn
    if player == 1 and turn % 2 != 0:
        if totalp1 + dice > 100:
            messagebox.showwarning("Invalid Move", "You need exactly the remaining boxes to reach 100!")
            return
        totalp1 += dice
        msg = ""
        if totalp1 in snake:
            totalp1 = snake[totalp1]
            msg = "🐍 Oh no! Player 1 got bitten by a snake!"
            play_sound("snake")
        elif totalp1 in ladder:
            totalp1 = ladder[totalp1]
            msg = "🪜 Woohoo! Player 1 climbed a ladder!"
            play_sound("ladder")
        move_player(1, totalp1)
        if msg:
            messagebox.showinfo("Game Update", msg)
        if totalp1 >= 100:
            messagebox.showinfo("🎉 Game Over", "Player 1 Wins!")
            export_results("Player 1")
            root.quit()
        turn += 1
        status_label.config(text="Player 2's Turn")

    elif player == 2 and turn % 2 == 0:
        if totalp2 + dice > 100:
            messagebox.showwarning("Invalid Move", "You need exactly the remaining boxes to reach 100!")
            return
        totalp2 += dice
        msg = ""
        if totalp2 in snake:
            totalp2 = snake[totalp2]
            msg = "🐍 Oh no! Player 2 got bitten by a snake!"
            play_sound("snake")
        elif totalp2 in ladder:
            totalp2 = ladder[totalp2]
            msg = "🪜 Woohoo! Player 2 climbed a ladder!"
            play_sound("ladder")
        move_player(2, totalp2)
        if msg:
            messagebox.showinfo("Game Update", msg)
        if totalp2 >= 100:
            messagebox.showinfo("🎉 Game Over", "Player 2 Wins!")
            export_results("Player 2")
            root.quit()
        turn += 1
        status_label.config(text="Player 1's Turn")

# Export results to a text file
def export_results(winner):
    with open("game_results.txt", "w") as file:
        file.write(f"Winner: {winner}\n")
        file.write(f"Player 1 Final Position: {totalp1}\n")
        file.write(f"Player 2 Final Position: {totalp2}\n")
        file.write("Game over!")

# Restart game function
def restart_game():
    global totalp1, totalp2, turn
    totalp1 = 1
    totalp2 = 1
    turn = 1
    status_label.config(text="Player 1's Turn")
    canvas.coords("p1", *positions_map[1])
    canvas.coords("p2", *positions_map[1])
    messagebox.showinfo("Game Restarted", "The game has been reset!")

# Buttons
btn_frame = tk.Frame(root, bg="#FFF3E0")
btn_frame.pack(pady=10)

btn1 = tk.Button(btn_frame, text="🎲 Roll Dice - Player 1", font=("Helvetica", 12, "bold"),
                 bg="#F8BBD0", fg="black", command=lambda: animate_dice_roll(1))
btn1.grid(row=0, column=0, padx=15)

btn2 = tk.Button(btn_frame, text="🎲 Roll Dice - Player 2", font=("Helvetica", 12, "bold"),
                 bg="#BBDEFB", fg="black", command=lambda: animate_dice_roll(2))
btn2.grid(row=0, column=1, padx=15)

# Restart Button
btn_restart = tk.Button(root, text="🔄 Restart Game", font=("Helvetica", 14, "bold"),
                        bg="#FFEB3B", fg="black", command=restart_game)
btn_restart.pack(pady=20)

root.mainloop()
