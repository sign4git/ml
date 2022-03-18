import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(tagOrId=timer_text, text="00:00")
    check_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        timer_label.config(text="Break", fg=RED, bg=YELLOW)
    elif reps % 2 == 0:
        count_down(short_break)
        timer_label.config(text="Break", fg=PINK, bg=YELLOW)
    else:
        count_down(work_sec)
        timer_label.config(text="Work Time", fg=GREEN, bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(tagOrId=timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            check_text = ""
            for i in range(0, int(reps / 2)):
                check_text += "✔"
            check_label.config(text=check_text)


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.config(bg=YELLOW)
window.config(padx=100, pady=50)

timer_label = tk.Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(row=1, column=1)

start_button = tk.Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tk.Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

check_label = tk.Label(font=(FONT_NAME, 10, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)

window.mainloop()
