class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.current_score = 0
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it!")
            self.current_score += 1
        else:
            print("Sorry, that's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.current_score}/{self.question_number + 1}", "\n")
    def next_question(self):
        user_answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False)?: ")
        self.check_answer(user_answer, self.question_list[self.question_number].answer)
        self.question_number += 1
    def still_has_questions(self):
        return self.question_number < len(self.question_list)