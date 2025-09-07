from tkinter import Tk, PhotoImage, Canvas, Button

BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = ("Arial", 20, "italic")
FONT_WORD = ("Arial", 60, "bold")

# ---------- FLASHCARDS FUNCTIONALITY ---------- #
import pandas
import random

current_words = {}
english_spanish_dict = {}

try:
    english_words = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    english_words = pandas.read_csv('data/english_words.csv')
    english_spanish_dict = english_words.to_dict(orient='records')
else:
    english_spanish_dict = english_words.to_dict(orient='records')

def flip_card():
    front_canvas.itemconfig(bg_img, image=back_card)
    front_canvas.itemconfig(english_title, text="Spanish", fill="white")
    front_canvas.itemconfig(english_word_text, text=current_words["Spanish"], fill="white")

def next_card():
    global current_words, flip_timer
    my_window.after_cancel(flip_timer)
    current_words = random.choice(english_spanish_dict)
    front_canvas.itemconfig(bg_img, image=front_card)
    front_canvas.itemconfig(english_title, text="English", fill="black")
    front_canvas.itemconfig(english_word_text, text=current_words["English"], fill="black")
    my_window.after(3000, flip_card)

def is_it_know():
    english_spanish_dict.remove(current_words)
    data = pandas.DataFrame(english_spanish_dict)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()


# ---------- UI ---------- #
my_window = Tk()
my_window.title("Flashy")
my_window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = my_window.after(3000, flip_card)

front_card = PhotoImage(file="images/card_front.png")

front_canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
bg_img = front_canvas.create_image(400, 263, image=front_card)
english_title = front_canvas.create_text(400, 150, text="English", font=FONT_LANGUAGE, fill="black")
english_word_text = front_canvas.create_text(400, 262, text="Word", font=FONT_WORD, fill="black")
front_canvas.grid(row=0, column=0, columnspan=2)

back_card = PhotoImage(file="images/card_back.png")

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=is_it_know)
right_button.grid(row=1, column=1)

next_card()

my_window.mainloop()