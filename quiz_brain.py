
class QuizBrain:
    def __init__(self,questionlist):
        self.question_number=0
        self.list=questionlist
        self.score=0

    def still_has_question(self):
        return len(self.list) > self.question_number


    def next_question(self):
        current_question=self.list[self.question_number]
        self.question_number +=1
        user_answer=input(f"Q.{self.question_number}: {current_question.text} (True/False) :")
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            print("You got it right!!")
            self.score += 1
            print(f"Your current score is : {self.score}/{self.question_number}")
        else:
            print("That's wrong answer")
            print(f"Your score is {self.score}/{self.question_number}")

        print(f"The correct answer is {correct_answer} ")

