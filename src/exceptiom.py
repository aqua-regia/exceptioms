from jokes_en import jokes
import random


class Exceptioms(Exception):
    def __init__(self, *args, **kwargs):
        length_jokes = len(jokes)
        joke_to_pick = random.randint(0, length_jokes)
        selected_jokes = jokes[joke_to_pick]
        Exception.__init__(self, selected_jokes, args, kwargs)

