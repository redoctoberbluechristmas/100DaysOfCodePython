from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #

# Go to colorhunt.co for ideas on color schemes.
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLACK = "#000000"
WHITE = "#FFFFFF"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None     #< ---- Need to initialize my timer value globally, to use in count_down()
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    #timer_text.config(text="00:00")
    timer_label.config(text="Timer")
    checkmarks.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    print(reps)
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text=f"Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text=f"Short Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text=f"Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    # Convert seconds to normal time display
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:     # (int)
        count_sec = f"0{count_sec}"   # use fstrings for easy formatting. This will dynamically type count_sec as str.

    # https://stackoverflow.com/questions/11328920/is-python-strongly-typed
    # Strong typing means values doesn't change in unexpected ways.
    # Dynamic typing means that runtime objects (values) have a type, while in static typing variables have a type.


    # How you change an element of Canvas class.
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)  #<--- this is what you must cancel to reset.
    else:
        start_timer()  # If you don't do this, the timer will just stop at zero and not go to the next session.
        checks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            checks += "✔"
        checkmarks.config(text=checks)  #for every two reps completed, add check to checkmark label

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
# Change background color of window
window.config(padx=100, pady=50, bg=YELLOW)



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# Need to save image path as PhotoImage var.
tomato_img = PhotoImage(file="tomato.png")
# Give values of half the width and height to place image in center of canvas.
# Xcoord is adjusted a bit to 103, to better center the image after padding.
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Timer Label
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)

# Start Button
start_button = Button(text="Start", fg=BLACK, bg=WHITE, font=("Helvetica", 8, "bold"), command=start_timer)
start_button.grid(column=0, row=2)

# Reset Button

reset_button = Button(text="Reset", fg=BLACK, bg=WHITE, font=("Helvetica", 8, "bold"), command=reset_timer)
reset_button.grid(column=2, row=2)

# Checkmark Label

checkmarks = Label(fg=GREEN, bg=YELLOW)
checkmarks.grid(column=1, row=3)

window.mainloop()