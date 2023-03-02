class QuizBrain:
    def __init__(self, questions_bank):
        self.question_number = 0
        self.questions_list = questions_bank
        self.score = 0
    
    def still_has_questions(self):
        return self.question_number < len(self.questions_list)
    
    def next_question(self):
        asking_question = self.questions_list[self.question_number]
        self.question_number += 1
        choice = input(f"Q.{self.question_number}: {asking_question.text} (True/False)?: ").capitalize()
        return choice
    
    def check_answer(self, choice):
        correct_answer = self.questions_list[self.question_number - 1].answer
        if correct_answer == choice:
            self.score += 1
            print("You've got it right!")
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}.\n")
