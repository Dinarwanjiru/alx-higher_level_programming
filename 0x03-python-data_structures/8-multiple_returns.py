#!/usr/bin/python3
''' function that returns a tuple with the length of a string and
its first character.'''

def multiple_returns(sentence):
    if sentence != '':
        first_char = sentence[0]
    else:
        first_char = None
    return (len(sentence), first_char)
