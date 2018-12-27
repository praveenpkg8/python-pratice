
class Dog():

    species = "mammal"

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

sam = Dog('lab','honey')
tom = Dog('Golden', 'salt')

print(sam.breed + " " + sam.name )
print(tom.breed + " " + tom.name )
print(sam.species)
