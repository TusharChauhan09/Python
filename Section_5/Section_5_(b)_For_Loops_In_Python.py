# For Loops In Python

# It Itrates over a range , str , dict , tup or   over a list

# E.G 1    Iterating Over A Range
for x in range(1,11,2):               # Iterating over a range
    print(x)


#           Iterating Over A List
my_list = [1,2,3,4,5,6,7,8,9,10]      # Iterating over a list

# E.G 2
for num in my_list:
    print(num)

# E.G 3
for x in my_list:
    print("Hello")

# E.G 4
for x in my_list:                  # Check the no. is even in list by for loop 
    # Check for even no.
    if x%2 == 0:
        print(f"Even no. {x}")
    else:
        print(f"Odd no. {x}")

# E.G 5
list_sum = 0
for x in my_list:
    list_sum = list_sum + x
    print(list_sum)

print(f"Final sun : {list_sum}")


#              Iterating Over A String
# E.G 6
my_string =  "Hello World"             # Iterating over a String
for letter in  my_string:
    print(letter)

for letter in  my_string:
    print("x")



#              Iterating Over A Tuple        
# E.g 7
my_tup = (1,2,3)                     # Iterating over Tuple
for x in my_tup:
    print(x)


# E.g 8     Tuple unpacking
my_list = [(1,2),(3,4),(5,6)]        # We need to store tuple inside a list and we can unpack it with tuple unpacking property
for x in my_list:
    print(x)

for (a,b) in my_list:
    print(a)
    print(b)


#               Iterating Over A Dictionary
# E.G 9    
my_dict = {"k1":1,"k2":2,"k3":3}           # Iterating over a dictionary
for x in my_dict:
    print(x)

for key,value in my_dict:
    print(key)
    print(value)


