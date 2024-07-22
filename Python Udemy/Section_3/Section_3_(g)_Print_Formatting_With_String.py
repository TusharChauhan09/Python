# Print Formatting with String

# (1) Formatting With .format() Method
print("This is a String {}".format("INSERTED"))         # Where you need the string to be placed leave that palce holder {}    

print("The {} {} {}".format("fox","brown","quick"))     # The  are placed in the sequence in which they are present in the .format()

#(1.a) Inserted by Index position
print("The {2} {1} {0}".format("fox","brown","quick"))     # The  can be palced in the sequence of the of there indexed numbers

#(1.b) Inserted by assigned keywords
print("The {q} {b} {f}".format(f="fox",b="brown",q="quick"))     # The value can assigned with the help of a key or keywords

#(1.c) Float Formatting Follows                                   #  The floating value can be assigned by .format(value:width.precision f)
result = 100/77
print("The result is {r:1.4f}".format(r = result))               # print("statement {value:width.precision}").format(result))


# (2)  Formatting With -String                                   # To apply f-string put f before print statement ane valve insde {}
name = "Tushar"
print(f"Hello, his name is {name}")

#(2.a)
result = 100/77
print(f"The result is {result:{1}.4f} ")                         # print(f"statement {value:{width}.{precision}})
