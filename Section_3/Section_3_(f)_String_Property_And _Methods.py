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


#----------------------------------------------------------------------------------------------------------------


# Sample string to test methods
s = "  Hello, World!  "
t = "hello123"
u = "123"
v = "HELLO"
w = "hello world"

# 1. Case Conversion
print(s.lower())            # '  hello, world!  '
print(s.upper())            # '  HELLO, WORLD!  '
print(s.capitalize())       # '  hello, world!  '
print(s.title())            # '  Hello, World!  '
print(s.swapcase())         # '  hELLO, wORLD!  '
print(s.casefold())         # '  hello, world!  '

# 2. Check Type / Content
print(t.isalnum())          # True
print(t.isalpha())          # False
print(u.isdigit())          # True
print(u.isnumeric())        # True
print(u.isdecimal())        # True
print(t.isidentifier())     # True
print(s.isspace())          # False
print(w.islower())          # True
print(v.isupper())          # True
print(s.istitle())          # False

# 3. Alignment & Padding
print(s.ljust(20, "*"))     # '  Hello, World!   ***'
print(s.rjust(20, "*"))     # '***  Hello, World!  '
print(s.center(20, "*"))    # '**  Hello, World!  **'
print("42".zfill(5))        # '00042'

# 4. Strip & Trim
print(s.strip())            # 'Hello, World!'
print(s.lstrip())           # 'Hello, World!  '
print(s.rstrip())           # '  Hello, World!'

# 5. Search & Count
print(s.find("World"))      # 9
print(s.rfind("l"))         # 15
print(s.index("World"))     # 9
# print(s.index("zzz"))     # ValueError
print(s.count("l"))         # 3
print(s.startswith("  He")) # True
print(s.endswith("!  "))    # True

# 6. Replace & Split
print(s.replace("World", "Python")) # '  Hello, Python!  '
print(s.split(","))        # ['  Hello', ' World!  ']
print(s.split("World"))        # ['  Hello', '!  ']
print(s.rsplit(","))       # ['  Hello', ' World!  ']
print(s.splitlines())      # ['  Hello, World!  '] (if multiline, splits on \n)
print("...".join(["a", "b"])) # 'a...b'
print(s.partition(","))    # ('  Hello', ',', ' World!  ')
print(s.rpartition(","))   # ('  Hello', ',', ' World!  ')

# 7. Encoding & Translation
print(s.encode())          # b'  Hello, World!  '
table = str.maketrans("HW", "hw")
print(s.translate(table))  # '  hello, world!  '

# 8. Formatting
print("Hello {}".format("World"))  # 'Hello World'
print("{:>10}".format("test"))     # '      test'
print(f"Value: {42:.2f}")          # 'Value: 42.00'

# 9. Unicode Methods
print("\u00bd".isnumeric())        # True (½)

# 10. Other Methods
print(s.expandtabs(4))    # Tabs replaced by spaces


s = "Hello, World!"

# Substring from index 0 to 4 (excluding 5)
print(s[0:5])      # 'Hello'

# From index 7 to end
print(s[7:])       # 'World!'

# From beginning to index 4
print(s[:5])       # 'Hello'

# Last 6 characters
print(s[-6:])      # 'World!'

# Every second character
print(s[::2])      # 'Hlo ol!'

# Reverse the string
print(s[::-1])     # '!dlroW ,olleH'

print(s[:-7:-1])  # '!dlroW'