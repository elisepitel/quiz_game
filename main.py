from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# question bank of question object
question_bank = []

# Loop though question_data elements to create & initialise question objects
# "text" & "answer" are attributes of question_data
for question in question_data:
    q_object = Question(question['question'], question['correct_answer'])
    #print(q_object.answer)
    #print(q_object.text)
    question_bank.append(q_object)
#print(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    user_response = quiz.next_question()

print(f"You've completed the quiz, your final score is: {quiz.score}/{quiz.question_number}")
print("Have a nice day! 🧚")
