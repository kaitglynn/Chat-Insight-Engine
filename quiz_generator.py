```python
import random

class QuizGenerator:
    def __init__(self):
        self.quizData = []

    def load_data(self, data):
        self.quizData = data

    def generate_quiz(self, topic, difficulty):
        topic_questions = [q for q in self.quizData if q['topic'] == topic and q['difficulty'] == difficulty]
        if len(topic_questions) < 5:
            return "Not enough questions for this topic and difficulty. Please choose another topic or difficulty."
        else:
            quiz_questions = random.sample(topic_questions, 5)
            return quiz_questions

    def check_answer(self, question, user_answer):
        correct_answer = question['answer']
        if user_answer.lower() == correct_answer.lower():
            return True
        else:
            return False

quizGenerator = QuizGenerator()
quizGenerator.load_data(quizData)
quiz = quizGenerator.generate_quiz('math', 'easy')

for question in quiz:
    print(question['question'])
    user_answer = input("Your answer: ")
    if quizGenerator.check_answer(question, user_answer):
        print("Correct!")
    else:
        print("Incorrect. The correct answer is " + question['answer'])
```