import random


def rand_color():
    random_color = str(random.randint(0, 255))
    return ['hsl(' + random_color + ', 100%, 60%)', 'hsl(' + str(random.randint(0, 255)) + ', 50%, 75%)']


def make_selection(selection):
    return [word.upper() for word in selection]

