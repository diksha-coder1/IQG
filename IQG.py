
# Interactive Quiz Game
# Beginner Level Python Project

# Function to create the question file if it does not exist
def create_file():
    try:
        file = open("questions.txt", "r")
        file.close()
    except FileNotFoundError:
        file = open("questions.txt", "w")
        file.close()


# Function to load questions from the text file
def load_questions():

    questions = []

    try:
        file = open("questions.txt", "r")

        for line in file:

            data = line.strip().split("|")

            if len(data) == 6:
                question = data[0]
                option_a = data[1]
                option_b = data[2]
                option_c = data[3]
                option_d = data[4]
                answer = data[5]

                questions.append({
                    "question": question,
                    "A": option_a,
                    "B": option_b,
                    "C": option_c,
                    "D": option_d,
                    "answer": answer
                })

        file.close()

    except FileNotFoundError:
        print("Question file not found.")

    return questions


# Function to start the quiz
def start_quiz():

    questions = load_questions()

    if len(questions) == 0:
        print("\nNo questions available. Please add questions first.")
        return

    score = 0
    correct = 0
    wrong = 0

    print("\n========== START QUIZ ==========")

    for i in range(len(questions)):

        print("\nQuestion", i + 1)
        print(questions[i]["question"])

        print("A.", questions[i]["A"])
        print("B.", questions[i]["B"])
        print("C.", questions[i]["C"])
        print("D.", questions[i]["D"])

        answer = input("Enter your answer (A/B/C/D): ")
        answer = answer.upper().strip()

        if answer not in ["A", "B", "C", "D"]:
            print("Invalid answer! Please enter A, B, C or D.")
            wrong = wrong + 1
            score = score - 1
            print("Correct answer:", questions[i]["answer"])

        elif answer == questions[i]["answer"]:
            print("Correct Answer! Well done.")
            score = score + 1
            correct = correct + 1

        else:
            print("Wrong Answer!")
            print("Correct answer:", questions[i]["answer"])
            score = score - 1
            wrong = wrong + 1

    # Display final result
    print("\n========== QUIZ RESULT ==========")

    print("Total Questions:", len(questions))
    print("Correct Answers:", correct)
    print("Wrong Answers:", wrong)
    print("Final Score:", score)

    print("=================================")


# Function to add a new question
def add_quiz():

    print("\n========== ADD NEW QUESTION ==========")

    question = input("Enter your question: ")

    option_a = input("Enter Option A: ")
    option_b = input("Enter Option B: ")
    option_c = input("Enter Option C: ")
    option_d = input("Enter Option D: ")

    answer = input("Enter correct answer (A/B/C/D): ")
    answer = answer.upper().strip()

    while answer not in ["A", "B", "C", "D"]:
        print("Invalid answer. Please enter A, B, C or D.")
        answer = input("Enter correct answer: ")
        answer = answer.upper().strip()

    # Save question in text file
    file = open("questions.txt", "a")

    file.write(
        question + "|" +
        option_a + "|" +
        option_b + "|" +
        option_c + "|" +
        option_d + "|" +
        answer + "\n"
    )

    file.close()

    print("\nNew question added successfully!")


# Main menu function
def main():

    create_file()

    while True:

        print("\n================================")
        print("       WELCOME TO QUIZ GAME")
        print("================================")
        print("1. Start Quiz")
        print("2. Add New Quiz")
        print("3. Exit Quiz")
        print("================================")

        choice = input("Please enter your choice: ")

        if choice == "1":

            start_quiz()

        elif choice == "2":

            add_quiz()

        elif choice == "3":

            print("\nThank you for playing the Quiz Game. Goodbye!")
            break

        else:

            print("\nInvalid choice! Please select 1, 2 or 3.")


# Run the main programme
main()
