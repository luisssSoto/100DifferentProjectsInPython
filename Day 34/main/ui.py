from tkinter import Tk, Canvas, Label, Button, PhotoImage
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", font=("Arial", 16, "bold"), fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.question_canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.question_canvas.create_text(150, 125, text="any", width=280, font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.question_canvas.grid(row=1, column=0, columnspan=2, pady=50)

        right_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_img, highlightthickness=0, command=self.true_answer)
        self.right_button.grid(row=2, column=0)

        left_img = PhotoImage(file="images/false.png")
        self.left_button = Button(image=left_img, highlightthickness=0, command=self.false_answer)
        self.left_button.grid(row=2, column=1)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.question_canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            question_text = self.quiz_brain.next_question()
            self.question_canvas.itemconfig(self.question_text, text=question_text)
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
        else:
            self.question_canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz, your final score is: {self.quiz_brain.score}")
            self.left_button.config(state="disabled")
            self.right_button.config(state="disabled")


    def true_answer(self):
        self.give_feedback(self.quiz_brain.check_answer("True"))
    def false_answer(self):
        self.give_feedback(self.quiz_brain.check_answer("False"))

    def give_feedback(self, answer):
        if answer is True:
            self.question_canvas.config(bg="green")
        else:
            self.question_canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



