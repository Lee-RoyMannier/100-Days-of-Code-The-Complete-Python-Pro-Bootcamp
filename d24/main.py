import tkinter as tk
import math
# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer_fct = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    global reps
    global timer_fct
    reps = 0
    screen.after_cancel(timer_fct)
    label_name.config(text="Timer")
    canvas.itemconfigure(timer_text, text="00:00")
    check_box.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        label_name["text"] = "WORK !"
        label_name["fg"] = "pink"
        change_count(work_sec)
    elif reps == 8:
        label_name["text"] = "NICE ONE !"
        label_name["fg"] = "green"
        change_count(long_break)
    else:
        label_name["text"] = "BREAK"
        label_name["fg"] = "blue"
        change_count(short_break)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def change_count(count):
    minute = math.floor(count / 60)
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfigure(timer_text, text=f"{minute}:{sec}")
    if count > 0:
        global timer_fct
        timer_fct = screen.after(1000, change_count, count-1)
    else:
        timer()
        marks = ""
        work_session = math.floor(reps/2)
        checked_value = "✓"
        for i in range(work_session):
            marks += checked_value
        check_box.config(text=marks, bg=GREEN)


# ---------------------------- UI SETUP ------------------------------- #
screen = tk.Tk()
screen.title("Pomodoro")
screen.config(padx=100, pady=50, bg=YELLOW)


label_name = tk.Label(text="Timer", fg=GREEN, bg=YELLOW,
                      font=(FONT_NAME, 50, "bold"))
label_name.grid(column=1, row=0)

start_btn = tk.Button(text="Start",  bg=YELLOW,
                      highlightthickness=0, command=timer)
start_btn.grid(column=0, row=2)

reset_btn = tk.Button(text="Reset",  bg=YELLOW,
                      highlightthickness=0, command=reset)
reset_btn.grid(column=2, row=2)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

check_box = tk.Label(fg=YELLOW, bg=YELLOW)
check_box.grid(column=1, row=3)

screen.mainloop()
