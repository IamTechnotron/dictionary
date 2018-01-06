from os import path


def word_match(word_1, word_2):
    """
    Finds the number of mismatched letter in a word
    :param word_1:
    :param word_2:
    :return: no. of mismatched word!
    """
    mismatch = 0
    if len(word_1) >= len(word_2):
        for letter_index in range(len(word_1)):
            if letter_index > len(word_2)-1 or word_2[letter_index] != word_1[letter_index]:
                mismatch += 1
    else:
        for letter_index in range(len(word_2)):
            if letter_index > len(word_1)-1 or word_2[letter_index] != word_1[letter_index]:
                mismatch += 1
    return mismatch


def resolve_path(letter):
    letter = letter.lower()
    py_path = path.dirname(path.abspath(__file__))
    temp_path = py_path.split('/')
    db_path = ""

    for folder in temp_path:
        if folder == "py_files":
            break
        else:
            db_path += folder + "/"
    db_path += "db_files/" + letter
    return db_path


def resolve_db(word):
    """

    :param word: word that is input!
    :return: a dictionary or -1(if database is missing)
    :working: It creates a dictionary with the input as key and its meanings as values.
              However, if a word does not match any of word in database, it searches for substring!
              If even that fails, then, it searches for no of mismatches, and takes words with mismatches < word length.
              Unmatched words are used for suggestions! Last for of the word are shown!
              Note: If a word is not found, db is a list type. Else dictionary!
    """
    word = word.upper()
    first_letter = word[0]
    word_length = len(word)
    db_path = resolve_path(first_letter)
    db = []
    found = 0
    print('path =' + db_path)
    if path.isfile(db_path):
        with open(db_path) as file:
            for line in file:
                temp = line.split(line[line.find('(')])
                temp[0] = temp[0][0:-1].upper()

                if temp[0] == word.upper():
                    found = 1
                    meanings = list()
                    meanings.append('(' + temp[1])
                    if temp[0] in db and type(db) == dict:
                        meanings = db[temp[0]] + meanings
                    del db
                    db = {temp[0]: meanings}

                elif word in temp[0] and found == 0:
                    if temp[0] not in db:
                        db.append(temp[0])
                    found = 1

                elif word_match(word, temp[0]) <= word_length and found == 0:
                    if temp[0] not in db:
                        db.append(temp[0])
        return db
    else:
        print("ERROR : Data-base Missing")
        return -1


# Test case
# print(create_db('/home/avik/Documents/dictionary', 'a'))
