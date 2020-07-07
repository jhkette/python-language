instructor ={
    "name": "Colt",
    "owns_dog": "true",
    "num_courses": 4,
}

################## IN ###########################

"name" in instructor
# true

"Colt" in instructor.values()
# true

# fromkeys
{}.fromkeys("a", "b") # {"a": "b"}

new_user = {}.fromkeys(['name', 'score', 'unknown', 'profile_bio'], None)
# creates new_user dict with none values
print(new_user)


# clear dictionary

d = dict(a=1, b=2, c=3)
d.clear()
# empties dictionary
d # {}

# 
instructor.get("name") # returns Colt
# 
instructor.get("date") # returns None
