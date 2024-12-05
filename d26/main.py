import tkinter as tk
import pandas as pd
import random


def display_translation():
    canvas.itemconfig(back, image=translation)
    canvas.itemconfig(word, text=curr["French"])
    canvas.itemconfig(title, text="French")


def get_random_word():
    global curr, b
    screen.after_cancel(b)
    canvas.itemconfig(back, image=img_bkg)
    curr = random.choice(word_to_dict)
    canvas.itemconfig(word, text=curr["English"])
    canvas.itemconfig(title, text="English")
    b = screen.after(3000, display_translation)


BACKGROUND_COLOR = "#B1DDC6"
curr = {}
words = pd.read_csv("data/french_words.csv")
word_to_dict = pd.DataFrame.to_dict(words, orient="records")

# Creation de la fenetre
screen = tk.Tk()
screen.title("Flashy")
screen.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
b = screen.after(3000, display_translation)
canvas = tk.Canvas(width=800, height=526)
img_bkg = tk.PhotoImage(file="images/card_front.png")
translation = tk.PhotoImage(file="images/card_back.png")

back = canvas.create_image(400, 263, image=img_bkg)

title = canvas.create_text(400, 150, text="English",
                           font=("Ariel", 40, "italic"), fill="black")
word = canvas.create_text(400, 263, text="Trouver", font=(
    "Ariel", 60, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR,  highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

valider = tk.PhotoImage(file="images/right.png")
wrong = tk.PhotoImage(file="images/wrong.png")
uncknow = tk.Button(image=valider, highlightthickness=0,
                    command=get_random_word)
validate = tk.Button(image=wrong, highlightthickness=0,
                     command=get_random_word)
uncknow.grid(column=0, row=1)
validate.grid(column=1, row=1)

get_random_word()

screen.mainloop()
