from dictionary import translate
import json


def program_execution():
    quit_program = False
    while not quit_program:
        data = json.load(open('data.json'))
        output = translate(data)

        if type(output) == list:
            for item in output:
                print(item + " ")
        else:
            print(output)

        exit_question = input("Would you like to know another word? Press Q to quit or another key to continue. ")
        if exit_question == "":
            continue
        elif exit_question[0].lower() == "q":
            print("Bye!")
            quit_program = True
        else:
            continue


program_execution()