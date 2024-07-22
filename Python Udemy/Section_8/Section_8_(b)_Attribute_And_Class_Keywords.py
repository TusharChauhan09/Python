# (b)  Attribute And Class Keywords

'''
class Sample():
    pass
my_sample = Sample()

print(type(my_sample))
'''
class Dog():
    def __init__(self,breed,name,spots):
        
        # Attributes 
        # We take in the argumebts
        # Assign it with the self.attribute_name

        self.breed = breed
        self.name = name
        # Expect boolean True/False
        self.spots = spots

my_dog = Dog( breed= "Lab" ,name="Sammy" ,spots=False)
print(type(my_dog))
print(my_dog.breed)
print(my_dog.name, my_dog.spots)     