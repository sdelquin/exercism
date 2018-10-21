from collections import defaultdict
import string
import re

DELIMITERS = string.punctuation.replace("'", '') + string.whitespace


def word_count(phrase):
    words = defaultdict(int)
    splitted_phrase = re.split(f"'?[{DELIMITERS}]+'?", phrase.lower())
    for word in splitted_phrase:
        if word:
            words[word] += 1
    return dict(words)
