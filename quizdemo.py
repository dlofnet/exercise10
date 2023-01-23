from questions import ChoiceQuestion


def main():
    one = ChoiceQuestion()
    one.set_text("Who are the muggle aunt and uncle that Harry must live with every summer?")
    one.add_choice("Vernon and Petunia", True)
    one.add_choice("James and Lily", False)
    one.add_choice("Severus and Minerva", False)
    one.add_choice("Arthur and Molly", False)

    two = ChoiceQuestion()
    two.set_text("Which of these Hogwarts professors teaches Transfiguration?")
    two.add_choice("Lupin", False)
    two.add_choice("Snape", False)
    two.add_choice("McGonagall", True)
    two.add_choice("Dumbledore", False)

    three = ChoiceQuestion()
    three.set_text("Which of the following is an unforgivable curse?")
    three.add_choice("Lumos", False)
    three.add_choice("Avada Kedavra", True)
    three.add_choice("Expelliarmus", False)
    three.add_choice("Impedimenta", False)

    four = ChoiceQuestion()
    four.set_text("Who was the prisoner of Azkaban?")
    four.add_choice("Remus Lupin", False)
    four.add_choice("James Potter", False)
    four.add_choice("Sirius Black", True)
    four.add_choice("Peter Pettigrew", False)

    five = ChoiceQuestion()
    five.set_text("What kind of creature is Dobby?")
    five.add_choice("Goblin", False)
    five.add_choice("Centaur", False)
    five.add_choice("Hippogriff", False)
    five.add_choice("House elf", True)

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
