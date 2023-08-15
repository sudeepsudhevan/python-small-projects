from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    question = Question(data["question"], data["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the Quiz")

print(f"Your final score is was: {quiz.score}/{quiz.question_number}")

# print(question_bank[0].answer)
#
# for i in range(len(question_bank)):
#     print(question_bank[i].text)
