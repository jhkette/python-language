contains_purple("purple", "hello",2) # True

# args are an indefinate amount of arguments
# that are in the form of a tuple.
# you can loop through them. Or check them
# to see if they are in the 
def contains_purple(*args):
    if "purple" in args:
        return True
    else:
        return False
    