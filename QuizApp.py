import time
import random


class Question:
    def __init__(self, question: str, options: list, answer: list):
        self.question = question
        self.options = options
        self.answer = answer

    def __str__(self):
        output = f"{self.question}\n"
        for i, option in enumerate(self.options):
            output = output + f"\n{i+1}. {option}"

        return output


def shutdown():
    print("Exiting", end="\r")
    time.sleep(0.4)
    print("Exiting.", end="\r")
    time.sleep(0.4)
    print("Exiting..", end="\r")
    time.sleep(0.4)
    print("Exiting...")
    time.sleep(1)
    exit()


def loadQuestions(file: str = "CyberOps.txt"):
    questions = []
    with open(file, "r") as f:
        lines = f.readlines()
        options = []
        answer = []
        question = ""
        opt = False
        index = 1

        for line in lines:
            line = line.strip()

            if line == "":
                continue

            if opt:
                if "END" in line:
                    questions.append(Question(question, options, answer))
                    opt = False
                    index = 1
                    options = []
                    answer = []
                elif "CORRECT" in line:
                    options.append(line[:-8])
                    answer.append(index)
                    index += 1
                else:
                    options.append(line)
                    index += 1
            elif "START" in line:
                opt = True
            else:
                question = line

    return questions


def main():
    CORRECT = 0
    WRONG = 0
    questions = loadQuestions()
    try:
        numberOfQuestions = int(input("How many questions do you want to take: "))
        print("----------------------------------------------------")
        print("                       TEST")
        print("----------------------------------------------------")
    except:
        print("EXITING DUE TO DUMB USER!")
        shutdown()

    if numberOfQuestions < 1 or numberOfQuestions > len(questions):
        print("Number out of range.\nEnjoy all questions :)")
        numberOfQuestions = len(questions)

    for i in range(numberOfQuestions):
        mistake = False
        question = questions.pop(random.randint(0, len(questions) - 1))
        print(f"\nQuestion {i+1}/{numberOfQuestions}")
        print(question)
        inp = input("\nEnter the index/indexes of correct answer/answers: ")
        ans = []
        if inp == "q":
            shutdown()
        for char in inp:
            try:
                ans.append(int(char))
            except:
                continue

        if len(ans) > 0:
            for a in ans:
                if int(a) not in question.answer:
                    mistake = True
                    break
        else:
            mistake = True

        if mistake:
            print("\n#################")
            print("#####MISTAKE#####")
            print("#################")
            print(f"Correct answer: {question.answer}\n")
            WRONG += 1
            mistake = False
        else:
            CORRECT += 1
            print("\n*****************")
            print("*****CORRECT*****")
            print("*****************\n")

    print(f"Score: {CORRECT*100/numberOfQuestions}%")
    print(f"Correct: {CORRECT}")
    print(f"Wrong: {WRONG}")


while True:
    inp = input("Press Enter continue or enter 'q' to leave: ")
    if inp == "q":
        print("See you later aligator :)")
        shutdown()
    main()
