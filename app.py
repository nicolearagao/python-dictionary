import json

data = json.load(open('data.json'))


def translate():
    word = input("Which word would you like to know? ")
    try:
        meaning = data[word]
        print(meaning)
    except:
        print("The word was not found.")

translate()