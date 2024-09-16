class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        """checks if the question list still has questions left or not."""
        return self.question_number <= len(self.question_list)-1

    def next_question(self):
        """Asks the user if the statement is true or false and then moves to the next question."""
        statement = self.question_list[self.question_number]
        self.question_number += 1
        ques = input(f"Q.{self.question_number}: {statement.text} (True/False)?: ")
        self.check_answer(ques, statement.answer)

    def check_answer(self, user_answer, correct_answer):
        """checks if the user's answer is correct or not and manages the score accordingly,
         then reveals the right answer and the user's score."""
        if user_answer == correct_answer:
            self.score += 1
            print("You've got it right!")
        else:
            print("You're wrong!!")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
