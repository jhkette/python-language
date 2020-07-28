# A class can implement certain operations that are invoked by special syntax 
# (such as arithmetic operations or subscripting and slicing) by defining methods with 
# special names. This is Python’s approach to operator overloading, allowing classes 
# to define their own behavior (!important) with respect to language operators. For instance, if a 
# class defines a method named __getitem__(), and x is an instance of this class, then x[i] 
# is roughly equivalent to type(x).__getitem__(x, i). Except where mentioned, attempts to 
# execute an operation raise an exception when no appropriate method is defined 
# (typically AttributeError or TypeError).

# Setting a special method to None indicates that the corresponding operation is not available. 
# For example, if a class sets __iter__() to None, the class is not iterable, so calling iter() 
# on its instances will raise a TypeError (without falling back to __getitem__()). 2

# When implementing a class that emulates any built-in type, it is important that the 
# emulation only be implemented to the degree that it makes sense for the object being modelled. 
# For example, some sequences may work well with retrieval of individual elements, but extracting 
# a slice may not make sense. (One example of this is the NodeList interface in the W3C’s Document 
# Object Model.)


from copy import copy
class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		
	def __repr__(self):
		return f"Human named {self.first} {self.last} aged {self.age}"

	# we use the special double underscpre method here - this allows us to access age
	# like # j = new Human("Jenny", "Larsen", 47)
	# print(len(j)) - this would the age
	def __len__(self):
		return self.age
	# __add__ is the built in add method of class
	def __add__(self, other):
		# When you add two humans together...you get a newborn baby Human!
		if isinstance(other, Human):
			return Human(first='Newborn', last=self.last, age=0)
		return "You can't add that!"
	# mul is the built in multiply method
	def __mul__(self, other):
		# When you multiply a Human by an int, you get clones of that Human!
		if isinstance(other, int):
			# create a copy that has a new space in memory (ie) literally a copy not just
			# 
			return [copy(self) for i in range(other)]
		return "CANT MULTIPLY!"
	


j = Human("Jenny", "Larsen", 47)
k = Human("Kevin", "Jones", 49)
# print(j)
# print(len(j))
# triplets = j * 3

# kevin and jessica have triplets!
# K+J is a newborn - then * by three
triplets = (k + j) * 3
print(triplets)
mul = j * 2
print(mul)