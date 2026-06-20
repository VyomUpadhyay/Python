import tkinter as tk
from tkinter import messagebox
import random
import math
import winsound  # For sound effects (Windows only)
import pyttsx3  # For voice announcement

# Snake and ladder positions
snake = {28: 10, 37: 3, 48: 16, 75: 32, 94: 71, 96: 42}
ladder = {4: 56, 12: 50, 14: 55, 22: 58, 41: 79, 54: 88}

# Player positions
totalp1 = 1
totalp2 = 1
turn = 1

# Speech Engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def show_confetti_on_main(canvas, winner_name):
    dots = []
    for _ in range(150):
        x = random.randint(0, 600)
        y = random.randint(0, 600)
        color = random.choice(["red", "yellow", "green", "cyan", "magenta", "white", "orange"])
        dot = canvas.create_oval(x, y, x+6, y+6, fill=color, outline=color)
        dots.append(dot)

    def animate():
        for dot in dots:
            dx = random.randint(-3, 3)
            dy = random.randint(2, 5)
            canvas.move(dot, dx, dy)
        canvas.after(50, animate)

    animate()
    speak(f"Congratulations! {winner_name} wins the game!")
    messagebox.showinfo("Game Over", f"{winner_name} wins the game!")

# Setup GUI
root = tk.Tk()
root.title("\U0001F40D Snake & Ladder \U0001FA9C")
root.geometry("750x850")
root.configure(bg="#FFF3E0")

# Title label
title_label = tk.Label(root, text="\U0001F40D Snake & Ladder \U0001FA9C", font=("Comic Sans MS", 28, "bold"), fg="#4A148C", bg="#FFF3E0")
title_label.pack(pady=10)

# Canvas
canvas = tk.Canvas(root, width=600, height=600, bg="#FAF3DD", bd=0, highlightthickness=0)
canvas.pack(pady=20)

cell_size = 60
positions_map = {}
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

# Drawing snakes and ladders
def draw_snake(x1, y1, x2, y2, color="#D32F2F"):
    for i in range(51):
        t = i / 50
        xt = (1 - t) * x1 + t * x2 + 20 * math.sin(t * math.pi)
        yt = (1 - t) * y1 + t * y2 + 20 * math.cos(t * math.pi)
        canvas.create_oval(xt - 6, yt - 6, xt + 6, yt + 6, fill=color, outline=color)
    canvas.create_oval(x2 - 12, y2 - 12, x2 + 12, y2 + 12, fill=color, outline=color)

def draw_ladder(x1, y1, x2, y2, color="#388E3C"):
    steps = 8
    dx = x2 - x1
    dy = y2 - y1
    length = math.hypot(dx, dy)
    if length == 0: return
    ux, uy = dx / length, dy / length
    perp_x, perp_y = -uy, ux
    offset = 10
    r1s = (x1 + perp_x * offset, y1 + perp_y * offset)
    r1e = (x2 + perp_x * offset, y2 + perp_y * offset)
    r2s = (x1 - perp_x * offset, y1 - perp_y * offset)
    r2e = (x2 - perp_x * offset, y2 - perp_y * offset)
    canvas.create_line(*r1s, *r1e, fill=color, width=4)
    canvas.create_line(*r2s, *r2e, fill=color, width=4)
    for i in range(steps + 1):
        t = i / steps
        midx = x1 + dx * t
        midy = y1 + dy * t
        rx1 = midx + perp_x * offset
        ry1 = midy + perp_y * offset
        rx2 = midx - perp_x * offset
        ry2 = midy - perp_y * offset
        canvas.create_line(rx1, ry1, rx2, ry2, fill=color, width=2)

for s, e in snake.items():
    draw_snake(*positions_map[s], *positions_map[e])

for s, e in ladder.items():
    draw_ladder(*positions_map[s], *positions_map[e])

# Draw tokens
def draw_token(x, y, color, tag, offset=0):
    canvas.create_oval(x - 10 + 2, y - 10 + offset + 2, x + 10 + 2, y + 10 + offset + 2, fill="#888888", outline="")
    return canvas.create_oval(x - 10, y - 10 + offset, x + 10, y + 10 + offset, fill=color, tags=tag)

p1_token = draw_token(*positions_map[1], "red", "p1", offset=-5)
p2_token = draw_token(*positions_map[1], "blue", "p2", offset=5)

status_label = tk.Label(root, text="Player 1's Turn", font=("Helvetica", 14), bg="#FFF3E0", fg="#4A148C")
status_label.pack()

# Button controls
btn_frame = tk.Frame(root, bg="#FFF3E0")
btn_frame.pack(pady=10)

btn1 = tk.Button(btn_frame, text="🎲 Roll Dice - Player 1", font=("Helvetica", 12, "bold"), bg="#F8BBD0", fg="black", command=lambda: animate_dice_roll(1))
btn1.grid(row=0, column=0, padx=15)

btn2 = tk.Button(btn_frame, text="🎲 Roll Dice - Player 2", font=("Helvetica", 12, "bold"), bg="#BBDEFB", fg="black", command=lambda: animate_dice_roll(2))
btn2.grid(row=0, column=1, padx=15)

btn_restart = tk.Button(root, text="🔄 Restart Game", font=("Helvetica", 14, "bold"), bg="#FFEB3B", fg="black", command=lambda: restart_game())
btn_restart.pack(pady=20)

def restart_game():
    global totalp1, totalp2, turn
    totalp1 = 1
    totalp2 = 1
    turn = 1
    status_label.config(text="Player 1's Turn")
    canvas.coords("p1", *positions_map[1][0]-10, positions_map[1][1]-10, positions_map[1][0]+10, positions_map[1][1]+10)
    canvas.coords("p2", *positions_map[1][0]-10, positions_map[1][1]-10, positions_map[1][0]+10, positions_map[1][1]+10)

def play_sound(effect):
    winsound.Beep(500 if effect == "snake" else 1000, 500)

def check_for_snake_or_ladder(player):
    global totalp1, totalp2
    if player == 1:
        if totalp1 in snake:
            totalp1 = snake[totalp1]
            messagebox.showinfo("🐍 Snake!", "Player 1 was bitten by a snake!")
            play_sound("snake")
            move_player(1, totalp1)
        elif totalp1 in ladder:
            totalp1 = ladder[totalp1]
            messagebox.showinfo("🪜 Ladder!", "Player 1 climbed a ladder!")
            play_sound("ladder")
            move_player(1, totalp1)
    elif player == 2:
        if totalp2 in snake:
            totalp2 = snake[totalp2]
            messagebox.showinfo("🐍 Snake!", "Player 2 was bitten by a snake!")
            play_sound("snake")
            move_player(2, totalp2)
        elif totalp2 in ladder:
            totalp2 = ladder[totalp2]
            messagebox.showinfo("🪜 Ladder!", "Player 2 climbed a ladder!")
            play_sound("ladder")
            move_player(2, totalp2)

def move_player(player, position):
    target_x, target_y = positions_map[position]
    coords = canvas.coords("p1" if player == 1 else "p2")
    current_x = (coords[0] + coords[2]) / 2
    current_y = (coords[1] + coords[3]) / 2
    steps = 50
    dx = (target_x - current_x) / steps
    dy = (target_y - current_y) / steps

    def update_position(step):
        if step <= steps:
            new_x = current_x + step * dx
            new_y = current_y + step * dy
            canvas.coords("p1" if player == 1 else "p2", new_x - 10, new_y - 10, new_x + 10, new_y + 10)
            root.after(20, update_position, step + 1)
        else:
            check_for_snake_or_ladder(player)
            if totalp1 == 100:
                show_confetti_on_main(canvas, "Player 1")
            elif totalp2 == 100:
                show_confetti_on_main(canvas, "Player 2")

    update_position(1)

def animate_dice_roll(player):
    dice = random.randint(1, 6)
    num_rolls = 10

    def update_roll(count):
        nonlocal dice
        if count < num_rolls:
            dice_display = random.randint(1, 6)
            status_label.config(text=f"Player {player} rolled a {dice_display}")
            root.after(100, update_roll, count + 1)
        else:
            dice = random.randint(1, 6)
            status_label.config(text=f"Player {player} rolled a {dice}")
            process_roll(player, dice)

    update_roll(0)

def process_roll(player, dice):
    global totalp1, totalp2, turn
    if player == 1 and turn % 2 != 0:
        if totalp1 + dice > 100:
            messagebox.showwarning("Invalid Move", "You need exactly the remaining boxes to reach 100!")
            return
        totalp1 += dice
        move_player(1, totalp1)
        turn += 1
        status_label.config(text="Player 2's Turn")
    elif player == 2 and turn % 2 == 0:
        if totalp2 + dice > 100:
            messagebox.showwarning("Invalid Move", "You need exactly the remaining boxes to reach 100!")
            return
        totalp2 += dice
        move_player(2, totalp2)
        turn += 1
        status_label.config(text="Player 1's Turn")

root.mainloop()