from py_files import database

abb_table = {"adj.": "\t: adjective", "abb.": "\t: abbreviation",  "adv.": "\t: adverb", "conj.": "\t: conjunction",
             "n.": "\t\t: noun", "pl.": "\t: plural", "p. p.": "\t: prepositional phrase", "prep.": "\t: preposition",
             "v.": "\t\t: verb", "v. t.": "\t: transitive verb"}


def word_input():
    word = input("Enter the word to search: ")
    db = database.resolve_db(word)
    if type(db) == dict:
        for keys in db:
            if type(db[keys]) == list:
                print(keys)
                for values in db[keys]:
                    print(values)
    else:
        print('ERROR: Not a valid word or Word not in Database \n')
        print('Suggested/Similar words:')
        for x in range(1, 5):
            print(db[len(db) - x], end='\t')
        print()


def add_word():
    """
    Creates a wizard to add a word as per user.
    First it takes the word,
    then its part-of-speech type
    and finally the meaning.
    (Wizard aborts on faulty parts-of-speech type)
    Lastly it confirms the action and on positive reply adds to word in the database as per lexographical order!
    :return: None
    """
    word = input("Enter the word: ")
    print("Enter the abbreviated type/parts-of-speech of the word if any or just skip if nothing special: ")
    print_abbreviation_reference()

    word_type = input("\n>>> ")
    if word_type:
        if word_type not in abb_table:
            print("Not a known parts-of-speech! Aborting the wizard!")
            return
    word_type = '(' + word_type + ')'

    meaning = input("Enter Meaning: ")
    print("You are entering the following to the database!")
    print(word, word_type, meaning)

    choice = input("This action is IRREVERSIBLE!\nPLEASE CONFIRM WITH 'Y' FOR YES OR 'N' FOR NO\n>>> ")
    if choice is 'Y' or choice is 'y':
        print("The word has been added to the database!")
        # please add the word
    else:
        print("Word adding wizard has the stopped! WORD NOT ADDED!")
    return


def print_abbreviation_reference():
    for key in abb_table.keys():
        print(key, abb_table[key])

