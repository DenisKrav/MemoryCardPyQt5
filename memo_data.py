new_quest_templ = "Нове питання"
new_answer_templ = "Нова відповідь"

class Form():
    def __init__(self, question=new_quest_templ, answer=new_answer_templ, wrong_answer1="", wrong_answer2="", wrong_answer3=""):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.isActive = True
        self.attempts = 0
        self.correct = 0