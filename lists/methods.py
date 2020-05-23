lst =[1,2,3,4,5,6,7,2,2]
lst.append(8) # adds to end of the list

lst.extend([1,2,3]) #will spread a list into old list

# If one item use append, multiple items use extend

# inserts 'hi' on 2nd list index
lst.insert(2, 'hi')

lst.pop()
# pop the last list item
lst.pop(2) 
# removes item at index 2. #modifies list. Slice doesn't -creates copy

lst.remove(2)
# would remove the first instance of two in a list

lst.index(2)  # specifies index of listitem
lst.index(2,4,8)  # specifies index of listitem that is 2 between index 4 and 8

lst.count(2) #this would be 3 as two is there three times
# if none it doesn't throw an error just gives 0

lst.reverse() # reverses list in places. ie. Doesn't create
# a copy then reverse list. Don't see anything
# nothing is returned. 

lst.sort() #with no input just sorts list asc. Sorts in place like reverse. Can add input. 

words = ['coding', 'is', 'fun']
' '.join(words) # converts a list or another iterable argument and concatenates them
# ie would be 'coding is fun'