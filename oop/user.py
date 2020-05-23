
class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        # like a private method in PHP. 
        # Does actually work outside class though
        # _secret or _pass is just a convetion to show value is private
        self._secret = 'secret password'

        # name mangling. Python will change this property to
        #  _User__msg . This means with inhereited classes
        #  the msg will always be attributed to this this class
        # see print below
        self.__msg = 'another message'

    # this represent the instantiation of the class
    # ie in this instance it would return a users name and age
    # So for example if we print User1 we get name and age as opposed to a number
    def __repr__(self):
        return f"{self.first} is {self.age}"

    active_users = 0
    # we write the decocrater at classmethod
    # automatically the class is passed in as arguement (hence convention 
    # parameter arguement)
    # you only write method if you do not need any data about the class instances
    # 
    @classmethod
    def display_active_users(cls):
        f"There are currently {cls.active_users} active users"

    # this creates a new User instance from a class
    @classmethod
    def from_string(cls, data_str):
        first,last,age = data_str.split(",")
        return cls(first, last, int(age))
    
    def login(self):
        User.active_users += 1
        return f"{self.first} has logged in"
    
    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out"

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.first}"


# user1 = User('steve')
# print(user1.name)

# print(user1._User__msg)

# print(user1.likes("Ice Cream"))
# print(user2.likes("Chips"))

# print(user2.initials())
# print(user1.initials())

# print(user2.is_senior())
# print(user1.age)
# print(user1.birthday())
# print(user1.age)
# user1.say_hi()

print(User.active_users)
user1 = User("Joe", "Smith", 68)
print(user1.login())
# have to add underscore user to access
print(user1._User__msg)

user2 = User("Blanca", "Lopez", 41)
print(user2)
print(user2.login())
print(User.active_users)
print(user2.logout())
print(User.active_users)