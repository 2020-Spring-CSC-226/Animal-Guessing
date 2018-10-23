import json
import time


def intro():
    print("Welcome to the animal guessing game!")
    print("Rules are simple: ")
    print("You will guess an animal without telling me,")
    print("And I will try to find it by asking you different questions.")
    print("Ready??? Then guess a random animal...")
    time.sleep(3)
    print("Let's begin!")


def recursive(data, node):
    print()
    CurNode = input("Question: " + data[node]).lower()
    print("Your answer: " + CurNode)
    if CurNode in data[CurNode].keys():
        recursive(data[CurNode], node)
    else:
        print()
        print("Your guess is " + data[CurNode]["G"])
        print()
        inp = input("Do you want to play again?").lower()
        if inp == "yes":
            main()
        return


def main():
    data = json.load(open('data.json'))
    q = "Q"

    intro()
    recursive(data, q)


if __name__ == '__main__':
    main()