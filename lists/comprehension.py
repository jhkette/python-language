nums = [1,2,3,4]

x = [x* 10 for x in num]
#[ _manipulate_list for item in list]

name = 'colt'

[char.upper() for char in name]

friends = ['ashley', 'matt', 'michael']
[friend[0].upper() for friend in friends]

[bool(num) for num in nums]
# use bool function to see if
# a num is truthy or falsey

x = [str(num) for num in nums]

############################################
# CONDITIONAL LOGIC

# https://stackoverflow.com/questions/4260280/if-else-in-a-list-comprehension
# USEFUL STACK OVERFLOW

 evens = [num for num in numbers if num % 2 == 0]
#  if logic at end of the statement

# else is different

with_vowels = "This is so much fun!"

' '.join(char for char in with_vowels if char not in "aeiou")


lst = [1,2,3,4]
lst1 = [3,4,5,6]
answer = [ l for l in lst if l in lst1]
# just to get 3,4
names = [ "Elie", "Tim", "Matt"]
# to get reversed lower string names
answer2 = [n[::-1].lower() for n in names ]

s = 'amazing'
answer = [c for c in s if c not in "aeiou"]
# removes vowels from amazing


answer = [[n for n in range(0,3)] for val in range(0,3)]
# creates 
[[0,1,2], [0,1,2],[0,1,2]]

answer = [[n for n in range(0,10)] for val in range(0,10) ]
# create the sublist first then then for val in range to create the numbers of lists in the list