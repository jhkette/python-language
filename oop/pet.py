class Pet:
    allowed = ['cat', 'dog', 'fish', 'rat']
    #  if you only need values to be in init method put them in init
    # otherwise it is (as now) a class attribute
    def __init__(self, name, species):
        
        # could also have self.allowed
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet")
        self.name = name
        self.species = species
    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet")
        self.species = species

cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")
# croc = Pet("Wyatt", "croc")

# both cat and dog have the attribute 'allowed' but they are both
# pointing to the same allowed array in the class definition. If we 
# change this we can add a new animal species to cat or whatever

# we can add to the class attribute
Pet.allowed.append("pig")
cat.set_species('pig')

# if you did -
cat.allowed = ['dog', 'bear']
# this would changed the allowed array in memory.
# it would be specific to cat but dog would stay the same

