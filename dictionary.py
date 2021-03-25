from difflib import get_close_matches
from db import connection


def find_by_name(name):
    cursor = connection.cursor()
    sql_query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % name)
    results = cursor.fetchone()
    return results


def find_all_words():
    cursor = connection.cursor()
    sql_query = cursor.execute("SELECT Expression FROM Dictionary")
    results = cursor.fetchall()
    list_of_words = []
    for result in results:
        list_of_words.append(result[0])
    return list_of_words


def translate():
    word = input("Which word would you like to know? ").lower()

    results = find_by_name(word)
    all_words = find_all_words()

    if results is not None:
        if word == results[0]:
            return results[1]
        elif word.title() == results[0]:
            return results[1]
        elif word.upper() == results[0]:
            return results[1]
    else:
        similar_word = get_close_matches(word, all_words, cutoff=0.8)
        print(similar_word)


    """elif len(len_similar_word) > 0:
        answer = input(
            "Did you mean %s instead? Enter Y if yes, or N if no.\n " % similar_word)[0].upper()
        if answer == "Y":
            correct_word = find_by_name(similar_word)
            return correct_word[0]
        elif answer == "N":
            return "Alrighty then. Bye!"
        else:
            return "Invalid answer."

    else:
        return "This word doesn't exist."""
