# Indexing And Slicing With Strtings

mystring = "Hello World"     # Assigining String in double quotes (" ")
print(mystring)

# (1) Indexing 
print(mystring[0])            # Calling H as it is at 0 position in positive indexing

print(mystring[10])           # Calling d by positive indexing
print(mystring[-1])           # Calling d by negitive Indexing 

# Start
print(mystring[4])            # Calling o  


# (2) Slicing

# Stop
print(mystring[:7])            # It will print from 0 to 6
print(mystring[:7])            # (n-1) printing property of Stop string in Positive
print(mystring[:-7])           # (-n-1) printing property of Stop String in Negitive

# Start + Stop
print(mystring[4:7])           # It will print from 4 to 6 charcters in the string


# Step
print(mystring[::2])           # it will print all the characters with a difference of 1 

# Start + Stop + Step
print(mystring[4:7:2])         # it will print character 4 to 6 but will skip 5 as step of 2


# Extra - Reverse a String Trick
str1 = "abcdefgh"
print(str1[::-1]) 
 