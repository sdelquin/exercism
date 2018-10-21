import string


def is_pangram(sentence):
    ascii = list(string.ascii_lowercase)
    for char in sentence.lower():
        try:
            ascii.remove(char)
        except ValueError as err:
            print(err)
    return len(ascii) == 0
