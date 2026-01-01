# Lists In Python

my_list = ["one",2,3.14]          # assigen the values by List = [ " "," "," "]
print(my_list)

# (1) Indecing And Slicig In Lists
my_list = ["one", 2, 3.14, "Tushar", "Hi", 5.64]

print(my_list[2])                 # Calling a obeject in a List

print(my_list[1:])                # start

print(my_list[1:5])               # stop (n-1)

print(my_list[1:5:2])             # step


# (2) Concatination of lists
my_list = ["one", 2, 3.14 ]
another_list = ["four", 5,  6.1]

print(my_list + another_list)         # We can also add 2 list 


# (3) Mutability                      # Lists are mutable unlike string
my_list = ["one", 2, 3.14 ]  
my_list[0] = "Not one" 

print(my_list)


# (4) Multiplication
my_list = ["one", 2, 3.14 ]         # List can also be multiplied also like string 

print(my_list * 2)

# (5) Methods In Lists

new_list = ["one", "two", "three", "four"]
 
# (5.a) list.append
new_list.append("five")              # It adds a extra obeject at the end of the list

print(new_list) 

#(5.b) list.pop()                    # It removes an object from the list

new_list.pop()                       # If the indexing is not mentioned then it will remove last object
print(new_list)                    

# we can use print(list.pop() to know that which obeject is removed
print(new_list.pop(3))               # The object will be removed at the indexed positon mentioned
print(new_list)

# (5.c) list.sort()                  # The sort helps to arrange the list in a sequence or order
new_list = ["x","d","a","f","t"]

new_list.sort()
print(new_list)

new_list = [1,1110,1105,222,175,875]

new_list.sort()
print(new_list)

# (5.d) list.reverse()                             #  It just reverse the list  
new_list = ["a","b","c","d","e","f","g"]

new_list.reverse()
print(new_list)


# Alternative TRICK
new_list = ["a","b","c","d","e","f","g"]
print(new_list[::-1])

