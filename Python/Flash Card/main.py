import tkinter as tk
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
current_sample = None

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")


def pick_random_word():
    global current_sample, timer_start
    current_sample = data.sample()
    language_text = "French"
    window.after_cancel(timer_start)
    canvas.itemconfig(tagOrId=word, text=current_sample["French"].to_list()[0], fill='black')
    canvas.itemconfig(tagOrId=language, text=language_text, fill="black")
    canvas.itemconfig(tagOrId=img, image=img_file_front)
    timer_start = window.after(3000, flip_card)


def flip_card():
    global current_sample, timer_start
    language_text = "English"
    canvas.itemconfig(tagOrId=word, text=current_sample["English"].to_list()[0], fill="white")
    canvas.itemconfig(tagOrId=language, text=language_text, fill="white")
    canvas.itemconfig(tagOrId=img, image=img_file_back)


def known_word():
    global data
    data = data[data["French"] != current_sample["French"].to_list()[0]]
    data.to_csv("data/words_to_learn.csv", index=False)
    pick_random_word()


def unknown_word():
    pick_random_word()


window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)

timer_start = window.after(3000, pick_random_word)

canvas = tk.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
img_file_front = tk.PhotoImage(file="images/card_front.png")
img_file_back = tk.PhotoImage(file="images/card_back.png")
img = canvas.create_image(400, 263, image=img_file_front)
language = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = tk.PhotoImage(file="images/wrong.png")
wrong_btn = tk.Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=unknown_word)
wrong_btn.grid(row=1, column=0)

right_img = tk.PhotoImage(file="images/right.png")
right_btn = tk.Button(image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=known_word)
right_btn.grid(row=1, column=1)

pick_random_word()

window.mainloop()
