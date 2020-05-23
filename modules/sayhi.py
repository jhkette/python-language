
from saysup import say_sup

def sayhi():
    print(f"Hi my __name__ is {__name__}")

sayhi()
say_sup()

# the name is main for the FILE we are running. it is the main file
#  we are running it is __main__ if not it is the name of the file.
# here says_sup is run twice becuase the file is executed as soon as it 
# is imported
# we don't get it a third time because we added if __name__ = "__main__"