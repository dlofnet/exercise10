class Question:

    def __init__(self):
        self._text = ""
        self._answer = ""

    def set_text(self, question_text):
        self._text = question_text

    def set_answer(self, correct_response):
        self._answer = correct_response

    def check_answer(self, response):
        return response == self._answer

    def display(self):
        print(self._text)


class ChoiceQuestion(Question):
    def __init__(self):
        super().__init__()
        self._choices = []

    def add_choice(self, choice, correct):
        self._choices.append(choice)
        if correct:
            choice_string = str(len(self._choices))
            self.set_answer(choice_string)

    def display(self):
        super().display()
        for i in range(len(self._choices)):
            choice_number = i + 1
            print("%d: %s" % (choice_number, self._choices[i]))
