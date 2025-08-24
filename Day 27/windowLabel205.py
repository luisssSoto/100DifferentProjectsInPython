"""Window and Label with Tkinter"""
import tkinter

# Window
my_window = tkinter.Tk()
my_window.title("My first window")
my_window.minsize(width=400, height=400)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 20, "bold"))
my_label.pack(side="top")


# This sentence keep the window opened
my_window.mainloop()