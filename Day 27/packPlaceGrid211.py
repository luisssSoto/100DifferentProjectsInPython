"""pack(), place() and grid()"""

#Note: any of them could work together (only pack or only place or only grid)
import tkinter

# Window
my_window = tkinter.Tk()
my_window.title("My first window")
my_window.minsize(width=400, height=400)
my_window.config(padx=50, pady=50)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 20, "bold"))

# Set the attributes of the label
my_label["text"] = "Text was edited"
my_label.config(font=("Arial", 22, "italic"))

# pack()
# my_label.pack(side="left")

# place()
# my_label.place(x=100, y=100)

# grid()
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# function which will be triggered when a button obj will be clicked
def clicked_on_button():
    new_text = my_input.get()
    my_label["text"] = new_text

# Buttons
my_button = tkinter.Button(text="Click on me", command=clicked_on_button)
# pack()
# my_button.pack(side="left")

# place()
# my_button.place(x=100, y=150)

# grid()
my_button.grid(column=1, row=1)

new_button = tkinter.Button(text="new button")
new_button.grid(column=2, row=0)
# Entry

def write_input_value():
    my_label.config(text=my_input.get())

my_input = tkinter.Entry(width=10)
# pack()
# my_input.pack(side="left")

# place()
# my_input.place(x=1, y=2)

# grid()
my_input.grid(column=3, row=2)

my_window.mainloop()
# This sentence keep the window opened
my_window.mainloop()