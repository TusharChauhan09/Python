# Error And Exception  Handling
"""
def add(a,b):
    print(a+b)

number1 = 10
number2 = input("Please provide a number: ")
print("something here")

add(number1,number2)                     # error as number2 is a string



try:                                     # try block wher the error may or may not occur
    # Want to attempt this code
    # may have an error
    result  = 10 + 10
except:                                  # if error occurs then only except block will run
    print("Hey the input is wrong!") 

print(result)



try:                                     # try block wher the error may or may not occur
    # Want to attempt this code
    # may have an error
    result  = 10 + 10
except:                                  # if error occurs then only except block will run
    print("Hey the input is wrong!") 
else:
    print("add went well!")
    print(result)

print(result)

try:
    f = open("testfile","w")
"""