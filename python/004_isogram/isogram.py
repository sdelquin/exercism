def is_isogram(string):
    string = string.upper()
    for i, char in enumerate(string):
        if (char not in [' ', '-']) and (char in string[i+1:]):
            return False
    return True
