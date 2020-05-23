def say_sup():
    print(f"sup my __name__ is {__name__}")

say_sup()

# this will only run if you are actually executing file
if __name__ == "__main__":
    say_sup()