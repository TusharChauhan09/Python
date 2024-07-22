# Tuples In Python

my_tuple = ("one",2,3.14,"Tushar")      # To crerst a tuple use round brackets Tuple = (" "," "," " )
print(my_tuple)

# (1) Indexing In Tuple

print(my_tuple[1::2])                  # Start + Stop + Step

print(my_tuple[::-1])                  # Reversing in Tuple

# (2) Methods In Tuple

# (2.a) tuple.count()                 # It is used to count the no. of the element inside bracket () in a tuple

my_tuple = ("a","a","a","b","c","d","d")
print(my_tuple.count("a"))

# (2.b) tuple.index()                 # It gives us the first position of the element present inside the brackets ()
my_tuple = ("a","a","a","b","c","d","d")
print(my_tuple.index("b"))

print(len(my_tuple))                   # It gives the length of the tuple


# (3) Immutability                     # Tuple can't be re-assigned the values or update unlikey that of lists

# my_tuple[0] = "New"                  # it will give us the error
