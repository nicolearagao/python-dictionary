from dictionary import translate


def program_execution():
    quit_program = False
    while not quit_program:
        output = translate()


        exit_question = input("Would you like to know another word? Press Q to quit or another key to continue. ")
        if exit_question == "":
            continue
        elif exit_question[0].lower() == "q":
            print("Bye!")
            quit_program = True
        else:
            continue


program_execution()
