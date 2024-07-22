# List Comprehensions In Python

mystring = "hello"        # Normal way to append 
mylist = []
for x in mystring:
    mylist.append(x)
print(mylist)

mystring = "hello"        # Comprehensions methode Short for loop
mylist=[x for x in mystring]
print(mylist)

# e.g
mylist = [x for x in range(0,11)]
print(mylist)

# e.g
mylist = [x for x in range(0,11) if x%2==0]    # Comprehensions + If statements
print(mylist)

# e.g
celsius = [0,10,20.1,34.5]                      # For complex equations
fahrenheit = [((9/5)*temp + 32) for temp in celsius ]
print(fahrenheit)


