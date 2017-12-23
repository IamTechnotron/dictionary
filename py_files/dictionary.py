from os import path
import database


def word_input():
    word = input("Enter the word to search: ")
    db = database.create_db(database.resolve_path(), word[0].lower())
    sorted(db)
    if not valid_word(word):
        print("ERROR: Not a proper word")
    if type(db) == dict:
        for key in db:

            if key == word:
                print(db[key])
                continue
    '''else:
        print('ERROR: Not a valid word or Word not in Database ')'''


def valid_word(word):

    # checking or a word starting with a special character or number
    if ord(word[0].upper()) not in range(65, 93):
        return 0

    # checking for a phrase
    if ' ' in word:
        return 0

    return 1


# Test Case:
word_input()
