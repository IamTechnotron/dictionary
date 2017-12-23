from os import path


def create_db(db_path, char):
    db_path += '/'
    db_path += char
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

# Test case
#print(create_db('/home/avik/Documents/dictionary', 'a'))
