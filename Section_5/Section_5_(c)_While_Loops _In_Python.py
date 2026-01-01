# While Loop In Python

# While loop will continue to excute a block of code while code condition remains True

x = 0
while x < 5:
    print(f"The current value of x is {x}")
    x = x + 1
else:
    print("X is not less than 5 ")


# Keywords in Loops

# (1) Pass
y  = [1,2,3]
for item in y:
    pass                      # Pass will do nothing it acts like a palce holder
print("End of this loop")


# (2) Continue
my_string = "Tushar"
for x in my_string:
    if x == "h":
        continue              # It will skip that condition and will excute the rest 
    print(x)


# (3) Break
my_string = "Tushar"
for x in my_string:
    if x == "h":
        break                # It  will break th eloop at that condition and will excute the before part
    print(x)

x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1



