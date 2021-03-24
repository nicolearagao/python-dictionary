import json
from difflib import get_close_matches

data = json.load(open('data.json'))


def translate():
    word = input("Which word would you like to know? ").lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        return "Did you mean %s instead?" % get_close_matches(word, data.keys(), cutoff=0.8) [0]

    else:
        pass


print(translate())