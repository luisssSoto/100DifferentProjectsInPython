"""Window and Label with Tkinter"""
import tkinter

# Window
my_window = tkinter.Tk()
my_window.title("My first window")
my_window.minsize(width=400, height=400)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 20, "bold"))
my_label.pack(side="top")

# Set the attributes of the label
my_label["text"] = "Text was edited"
my_label.config(font=("Arial", 22, "italic"))

# function which will be triggered when a button obj will be clicked
def clicked_on_button():
    my_label["text"] = "The button was clicked"

# Challenge 1:
# Buttons
my_button = tkinter.Button(text="Click on me", command=clicked_on_button)
my_button.pack(side="bottom")

# Challenge 2.
# Entry

def write_input_value():
    my_label.config(text=my_input.get())

my_input = tkinter.Entry(width=10)
my_input.pack()
print(my_input.get())

my_button2 = tkinter.Button(text="Enter", command=write_input_value)
my_button2.pack()

# This sentence keep the window opened
my_window.mainloop()