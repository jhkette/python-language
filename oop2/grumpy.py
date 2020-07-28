# grumpydict INHERITS from Dict class
# we are using the dictionarys dunder/magic methods to
# alter how a dictionary works
class GrumpyDict(dict):
	def __repr__(self):
		print("NONE OF YOUR BUSINESS")
		# we call __repr__ method from the dict class
		return super().__repr__()

	# missing ona a dict usually returns error
	# here we return this message
	def __missing__(self, key):
		print(f"YOU WANT {key}?  WELL IT AINT HERE!")

	# change setitem dunder method of dictionary
	def __setitem__(self, key, value):
		print("YOU WANT TO CHANGE THE DICTIONARY?")
		print("OK FINE...")
		super().__setitem__(key, value)

	def __contains__(self, item):
		print("NO IT AINT IN HERE!")
		return False

data = GrumpyDict({"first": "Tom", "animal": "cat"})
print(data)
data['city'] = 'Tokyo'
print(data)
'city' in data





























class GrumpyDict(dict):
	def __repr__(self):
		print("NONE OF YOUR BUSINESS")
		return super().__repr__()

	def __missing__(self, key):
		print(f"THAT THING YOU WANT ISN'T IN HERE")

	def __setitem__(self, key, value):
		print("Why do you always have to change things?")
		print(f"Ugh fine, setting {key} to {value}")
		super().__setitem__(key, value)