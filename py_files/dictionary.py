from os import path
from py_files import database


def word_input():
    word = input("Enter the word to search: ")
    db = database.create_db(word[0].lower())
    #sorted(db)

    if type(db) == dict:
        for key in db:

            if key == word:
                print(db[key])
                continue
    '''else:
        print('ERROR: Not a valid word or Word not in Database ')'''


# Test Case:
word_input()
