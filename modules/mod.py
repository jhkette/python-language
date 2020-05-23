from random import choice, randint
# can also 
# import randome
# or random import *
# can also add aliases
# from random import choice as choicey

print(choice(['apple', 'bannana', 'pear']))

# import keyword and create function to see
# if something is a reserved keyword or not

from keyword import iskeyword

def contains_keyword(*args):
    for a in args:
        if iskeyword(a):
            return True
    return False


    