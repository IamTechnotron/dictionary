from os import path


def create_db(first_letter):
    db_path = resolve_path(first_letter)
    db = {}
    print('path =' + db_path)
    if path.isfile(db_path):
        with open(db_path) as file:
            for line in file:
                temp = line.split(line[line.find('(')])
                temp[0] = temp[0][0:-1]
                temp[1] = '(' + temp[1]
                db[temp[0].upper()] = temp[1]
        return db
    else:
        print("ERROR : Data-base Missing")
        return -1


def resolve_path(letter):
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


# Test case
#print(create_db('/home/avik/Documents/dictionary', 'a'))
