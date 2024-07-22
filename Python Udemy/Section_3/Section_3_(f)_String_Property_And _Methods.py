# String Property And Methodes

# (1) Properties

# (1) Immutability

name = "Sam"

'''
name[0] = "p"                       # Can reassign or update the value in a string 
print(name)
'''

# (2) Concatenate String

new_name = "P"
final_name = new_name + name[1:]    # We can add 2 strings 
print(final_name)

print( "2" + "3" )                  # Dynamic Typing backdraw

# (3) Multiplication In Strings

str1 = "z"
print(str1 * 10)

# (2) Methods

x = "Hello World! it's beautiful outside"


#(a)
print(x.upper())           # It capatilaize all the characters in a string
#(b)
print(x.lower())           # It result in low case of all elements

#(c)
print(x.split())           # It result in individual characters into list form ["ch1","ch2",...]
print(x.split("World!"))   # It results in the removal of the characters or letter in a String 

#(d)
print(len(x))              #It results in the length of the string

