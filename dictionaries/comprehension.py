# THIS THE FORMAT NEEDED FOR DICTIONARY COMPREHENSION

dict_variable = {key:value for (key,value) in dictonary.items()}

# THIS DOUBLES EACH VALUE IN THE DICTIONARY
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# k here is the key - which remains the same 
# v is * by 2 here for (k,v) (ie key, value) for all the dict1.items() - ie all the items
double_dict1 = {k:v*2 for (k,v) in dict1.items()}
print(double_dict1)


new_dict_comp = {n:n**2 for n in numbers if n%2 == 0}

print(new_dict_comp)


