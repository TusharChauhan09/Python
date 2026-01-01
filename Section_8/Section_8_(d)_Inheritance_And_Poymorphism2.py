# (d) Inheritance And Polymorphism

# (1) Polymorphism

 # class 1
class Dog():             

    def __init__(self,name):
        self.name = name
    
    def speak(self):      # same method name
        return self.name + " Say woof!"   # different function


 # class 2
class Cat():             

    def __init__(self,name):
        self.name = name
    
    def speak(self):       # same mehode name
        return self.name + " Say meow!"   # different function 
    


niko = Dog("niko")
felix = Cat("felix")
"""
print(niko.speak())
print(felix.speak())
"""

"""
for pet in [niko,felix]:
    print(type(pet))
    print(pet.speak())

    OR
"""

def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)

"""
print(niko.speak())
print(felix.speak())
"""



# Abstract Classes And Inheritance
class Animal():            # Base class

    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract methode")
    
class Dog(Animal):

    def speak(self):
        return self.name + " says Woof!"

class Cat(Animal):

    def speak(self):
        return self.name + " says meow!" 

fido = Dog("fido")
isis = Cat("isis")

print(fido.speak())
print(isis.speak())
