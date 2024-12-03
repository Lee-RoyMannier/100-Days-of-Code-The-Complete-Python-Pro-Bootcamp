import tkinter as tk
import math
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# Ajout fct start timer

def start_timer(count):
    minute = math.floor(count/60)
    sec = count % 60

    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfigure(timer, f"{minute}:{sec}")
    screen.after(1000, start_timer, count - 1)


screen = tk.Tk()
screen.title("Pomodoro")
screen.config(padx=20, pady=20, bg=YELLOW)

# AJout titre
title_app = tk.Label(text="Timer", font=(
    FONT_NAME, 34, "bold"), bg=YELLOW, fg="black")
title_app.config(pady=25)
title_app.grid(column=1, row=0)

# Ajout image
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 102, image=img)
timer = canvas.create_text(100, 100, text="00:00", font=(
    FONT_NAME, 34))
canvas.grid(column=1, row=1)

# AJout btn start

start_btn = tk.Button(text="Start", highlightthickness=0,
                      bg=YELLOW, command=start_timer)
start_btn.grid(column=0, row=2)

# Ajout Reset btn
start_btn = tk.Button(text="Reset", highlightthickness=0, bg=YELLOW)
start_btn.grid(column=2, row=2)

# Marks label
mark_label = tk.Label(text="test", bg=YELLOW)
mark_label.grid(column=1, row=2)
screen.mainloop()
