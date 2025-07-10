from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
"""Get the data locally"""
# for question in question_data:
#     new_question = Question(question["text"], question["answer"])
#     question_bank.append(new_question)

"""Get the data from an API"""
import requests
def get_data_from_api(bank, api_url):
    try:
        response = requests.get(api_url)
        data = response.json()
        results = data['results']
        for result in results:
            text = result['question']
            answer = result['correct_answer']
            next_question = Question(text, answer)
            bank.append(next_question)
        return bank
    except Exception as e:
        print(f"Error: {e}")

url = "https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean"
question_bank = get_data_from_api(question_bank, url)
print(f"question bank: {question_bank}")

qb = QuizBrain(question_bank)
while qb.still_has_questions():
    qb.next_question()
print("Congrats You've completed the quiz")
print(f"Your final score was: {qb.current_score}/{len(question_bank)}")


