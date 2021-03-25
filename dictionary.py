from difflib import get_close_matches


def translate(data):
    word = input("Which word would you like to know? ").lower()

    if word in data:
        return data[word]

    elif word.title() in data:
        return data[word.title()]

    elif word.upper() in data:
        return data[word.upper()]

    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        answer = input(
            "Did you mean %s instead? Enter Y if yes, or N if no.\n " % get_close_matches(word, data.keys(), cutoff=0.8)[
                0])[0].upper()
        if answer == "Y":
            return data[get_close_matches(word, data.keys(), cutoff=0.8)[0]]
        elif answer == "N":
            return "Alrighty then. Bye!"
        else:
            return "Invalid answer."

    else:
        return "This word doesn't exist."