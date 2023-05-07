import random


def rand_color():
    rc = str(random.randint(0, 255))
    return ['hsl(' + rc + ', 100%, 60%)', 'hsl(' + rc + ', 50%, 75%)']


def make_selection(selection):
    return [word.upper() for word in selection]

