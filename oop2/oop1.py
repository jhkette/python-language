# a key feature of oop is the ability to define a class which inherits from another class 
# a base or parent class
# In python, inheritance works by passing the parent class as an argument to the definition of 
# a child class.
class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
    
    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        print(f"this animal makes {sound}")


class Cat(Animal):
    # 
   
    def __init__(self,name,breed,toy):
        # call values from parent class - ie looks for init
        # method in animal
        super().__init__(name, species="Cat")
        self.breed = breed
        self.toy = toy

blue = Cat()

blue.make_sound('Meow') # will print 


print(isinstance(blue, Cat))