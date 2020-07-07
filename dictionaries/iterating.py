###############iterating##########################
instructor ={
    "name": "Colt",
    "owns_dog": "true",
    "num_courses": 4,


}
# gets values - as a list
instructor.values()

# gets keys as a list
instructor.keys()

for v in instructor.values():
    print(v)

# creates a list of tuples
instructor.items()

for k,v in instructor.items():
    print(k,v)

