class Animal:
    cool = True

    def make_sound(self, sound):
        print(f"this animal makes {sound}")


class Cat(Animal):
    pass

blue = Cat()

blue.make_sound('Meow') # will print 


print(isinstance(blue, Cat))