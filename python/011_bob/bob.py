from collections import namedtuple

INTERACTION_TYPE = namedtuple(
    'InteractionType', 'QUESTION YELL YELL_QUESTION ANYTHING ANYTHING_ELSE')
INTERACTION_TYPE.QUESTION = 'Sure.'
INTERACTION_TYPE.YELL = 'Whoa, chill out!'
INTERACTION_TYPE.YELL_QUESTION = "Calm down, I know what I'm doing!"
INTERACTION_TYPE.ANYTHING = 'Fine. Be that way!'
INTERACTION_TYPE.ANYTHING_ELSE = 'Whatever.'


def get_interaction_type(phrase):
    if not phrase:
        return INTERACTION_TYPE.ANYTHING
    elif phrase.isupper():
        if phrase.endswith('?'):
            return INTERACTION_TYPE.YELL_QUESTION
        else:
            return INTERACTION_TYPE.YELL
    elif phrase.endswith('?'):
        return INTERACTION_TYPE.QUESTION
    else:
        return INTERACTION_TYPE.ANYTHING_ELSE


def hey(phrase):
    return get_interaction_type(phrase.strip())
