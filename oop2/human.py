
#  a class that has prviate properties that then uses getters and setters

class Human: 
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        if age >= 0:
            self._age = age
        else:
            self._age = 0
    # def get_age(self):
    #     return self._age
    # def set_age(self, new_age):
    #     if new_age >= 0:
    #         self._age = new_age
    #     else:
    #         self._age = 0

    # this is a getter
    # def age needs to be the same for getter and setter
    @property
    def age(self):
        return self._age
    
    #  this is a setter
    # we can use this insead of method above
    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("age can't be negative")

    @property
    def full_name(self):
        return f"{self.first} {self.lastt}"

    @full_name.setter
    def full_name(self,name):
        self.first, self.last = name.split(" ")

    
    

jane = Human("Jane", "Goodall", -9)
print(jane.age)
# we don't have to call the methods
# with parens