class FruitQuiz:
    def __init__(self):
        self.score = 0

    def ask_question(self, question, answer):
        print(question)
        user_answer = input("Your answer: ")

        if user_answer.lower() == answer.lower():
            print("Correct!\n")
            self.score += 1
        else:
            print("Wrong! The answer is", answer, "\n")

    def show_score(self):
        print("Your final score:", self.score, "/ 3")


# Create an object
quiz = FruitQuiz()

quiz.ask_question("1. Which fruit is yellow and curved?", "Banana")
quiz.ask_question("2. Which fruit is red and often keeps the doctor away?", "Apple")
quiz.ask_question("3. Which fruit is known for its spiky green skin and sweet yellow flesh?", "Pineapple")

quiz.show_score()