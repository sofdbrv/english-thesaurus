import json
import difflib

thesaurus_data = json.load(open("data.json"))

thesaurus_open = True

def define_word(word):
    '''
    string -> string

    Finds all definitions of the searched word in a thesaurus
    '''
    suggestions = difflib.get_close_matches(word.lower(), thesaurus_data, 1)
    if word.lower() in thesaurus_data:
        word = word.lower()
        result = "\n" + word + "\n"
        for meaning in thesaurus_data[word]:
            result += (" = " + meaning + "\n")
        return result
    elif word.upper() in thesaurus_data:
        word = word.upper()
        result = "\n" + word + "\n"
        for meaning in thesaurus_data[word]:
            result += (" = " + meaning + "\n")
        return result
    elif word.title() in thesaurus_data:
        word = word.title()
        result = "\n" + word + "\n"
        for meaning in thesaurus_data[word]:
            result += (" = " + meaning + "\n")
        return result
    elif len(suggestions) > 0:
        suggested_word = suggestions[0]
        print("Did you mean '" + suggested_word + "'? Press Y to search the suggested word, or N to try a different word.")
        sugg_answer = input()
        if sugg_answer[0].lower() == "y":
            result = "\n" + suggested_word + "\n"
            for meaning in thesaurus_data[suggested_word]:
                result += (" = " + meaning + "\n")
            return result
        else:
            return ""
    else:
        return "Unfortunately, this word doesn't seem to exist in the thesaurus. Please try another word.\n"

while thesaurus_open == True:
    searched_word = input("Please enter a word: ")
    if searched_word == False or searched_word == 0:
        searched_word = input("Input not accepted. Please enter a word: ")
    elif searched_word == "\exit":
        thesaurus_open = False
    else:
        print(define_word(searched_word))