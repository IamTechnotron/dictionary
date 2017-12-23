from os import path
import database


def valid_word(word):

    # checking or a word starting with a special character or number
    if ord(word[0].upper()) not in range(65, 93):
        return 0

    # checking for a phrase
    if ' ' in word:
        return 0

    return 1


def resolve_path():
    py_path = path.dirname(path.abspath(__file__))
    temp_path = py_path.split('/')
    db_path = ""

    for folder in temp_path:
        if folder == "py_files":
            break
        else:
            db_path += folder + "/"
    db_path += "database"
    return db_path


# Test Case:


word = input("Enter the word to search: ")
word = word.upper()
db = database.create_db(resolve_path(), word[0].lower())
sorted(db)
if type(db) == dict:
    for key in db:

        if key == word:
            print(db[key])
            continue
'''else:
    print('Not a valid word! ')'''

