# (c) Class Object Attributes And Methods

class Dog():

    # Class Object Attribute
    # Same For Any Instance Of A Class
    species = "mammal"

    def __init__(self,breed,name,spots):

        # Attributes 
        # We take in the arguments
        # Assign it with the self.attribute_name
        self.breed = breed
        self.name = name
        self.spots = spots

    #Operation / actions --->  Methods  
    def bark(self,number):

        print(f"WOOF! my name is {self.name} and the number is {number}")


my_dog = Dog("Lab" ,"Sammy" ,False)

# Type printing
print(type(my_dog))

# Attribute Printing 
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
print(my_dog.species)

# Method printing
print(my_dog.bark(10))




class Circle():

    # class object attribute
    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius * radius * self.pi  # OR Cicle.pi

    # Method
    def get_circumfrence(self):
        return   2 * self.radius * self.pi # OR Circle.pi
    
my_circle = Circle(30)      # Circle(30) will change radius to 30 from defualt 1

print(my_circle.area)

print(my_circle.get_circumfrence())
