from questions import ChoiceQuestion


def main():
    one = ChoiceQuestion()
    one.set_text("1x1")
    one.add_choice("1", True)
    one.add_choice("0", False)
    one.add_choice("-1", False)
    one.add_choice("11", False)

    two = ChoiceQuestion()
    two.set_text("2x2")
    two.add_choice("22", False)
    two.add_choice("4", True)
    two.add_choice("8", False)
    two.add_choice("16", False)

    three = ChoiceQuestion()
    three.set_text("2x2")
    three.add_choice("22", False)
    three.add_choice("4", True)
    three.add_choice("8", False)
    three.add_choice("16", False)

    four = ChoiceQuestion()
    four.set_text("2x2")
    four.add_choice("22", False)
    four.add_choice("4", True)
    four.add_choice("8", False)
    four.add_choice("16", False)

    five = ChoiceQuestion()
    five.set_text("2x2")
    five.add_choice("22", False)
    five.add_choice("4", True)
    five.add_choice("8", False)
    five.add_choice("16", False)

    print("Welcome to this short Harry Potter quiz!")

    present_question(one)
    present_question(two)
    present_question(three)
    present_question(four)
    present_question(five)


def present_question(q):
    q.display()
    response = input("Your answer: ")
    print(q.check_answer(response))


main()
