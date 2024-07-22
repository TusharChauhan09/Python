# Basics Of Python Functions

# E.g 1       single line function
def say_hello():
    print("hello")

say_hello()


#E.g 2         multi-line function
def say_hello():
    print("hello")
    print("how")
    print("are")
    print("you ?")

say_hello()


# e.g 3
def say_hello(name):
    print(f"Hello {name}")

say_hello("Tushar")

 # if value is not to be mentioned then us Defualt
def say_hello(name = "Defualt"):
    print(f"Hello {name}")

say_hello()


# E.g  4   Print Function             # In print statement we can not save the result 
def print_result(num1,num2):
    print(num1 + num2)

print_result(10,20)
result = print_result(10,20)
print(result)
print(type(result))



# E.g 5    Return Function                # In return function we can save the result in a variable 
def return_result(num1,num2):
    return num1 + num2

return_result(10,20)                       # This can't we like this therefore we need to assigne it first
result = return_result(10,20)
print(result) 









