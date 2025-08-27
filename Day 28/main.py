from tkinter import Tk, Canvas, PhotoImage, Label, Button
from math import floor
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
times = 1
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    my_window.after_cancel(timer)
    my_canvas.itemconfig(timer_text, text="00:00")
    my_label.config(text="Timer")
    checkmark_label["text"] = ""
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_time():
    global reps
    reps += 1
    work_sec = .2 * 60
    break_sec = .1 * 60
    long_break_sec = .3 * 60

    if reps % 2 != 0:
        count_down(work_sec) # green
        my_label.config(text="Work", fg=GREEN)
    elif reps == 8:
        count_down(long_break_sec) # red
        my_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(break_sec) # pink
        my_label.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    my_canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = my_window.after(1000, count_down, count - 1)
    else:
        start_time()
        if reps % 2 == 0:
            global times
            checkmarks = "✔"
            checkmarks *= times
            checkmark_label.config(text=checkmarks)
            times += 1



# ---------------------------- UI SETUP ------------------------------- #
# Window
my_window = Tk()
my_window.title("Pomodoro Technique")
my_window.config(padx=100, pady=50, bg=YELLOW)

# Image
tomato_img = PhotoImage(file="tomato.png")

# Canvas
my_canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
my_canvas.create_image(100, 112, image=tomato_img)
timer_text = my_canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 20, "bold"), fill="white")
my_canvas.grid(row=1, column=1)

# Label
my_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
my_label.grid(row=0, column=1)

# Button "Start"
start_button = Button(command=start_time, highlightthickness=0)
start_button["text"] = "Start"
start_button["font"] = FONT_NAME
start_button.grid(row=2, column=0)

# Button "Reset"
reset_button = Button(highlightthickness=0, command=reset)
reset_button["text"] = "Reset"
reset_button["font"] = FONT_NAME
reset_button.grid(row=2, column=2)

# Checkmark
checkmark_label = Label()
checkmark_label.config(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12))
checkmark_label.grid(column=1, row=3)

my_window.mainloop()