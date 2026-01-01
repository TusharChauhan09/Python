# Dictionaries In Python

my_dict = {"key1":"value1", "key2":"value2"}    # To create  Dictionaries  Dictionaries = {"key1":"value1" , "key2":"value2"}
print(my_dict["key2"])                          # Calling the dictionary with a key

price_lookup = {"apple":2.99 , "oranges":1.99 , "milk":5.80}
print(price_lookup["apple"])

# (1) Nesting A Dicionary

# (1.a) Nesting A Dictionary With Lists
 
d = {"k1":123 , "k2":[50,11,21], "k3":"Tushar"}   # To Nest a List with a Dictionary for calling the list nested use print(dict[key list][index no.])
print(d["k2"][1])

# (1.b) Nesting A Dictionary With a Dictionary   

d = {"k1":123 , "k2":"Tushar" , "k3":{"insidekey":100}}  # To nest the dictionary with a dictionary for calling use print(dict[key dict][inside key]) 
print(d["k3"]["insidekey"])

# (1.c) Nesting A dictionary with both List and Dictionary

d = {"k1":123 , "k2":[50,11,21], "k3":{"insidekey1":100 ,"insidekey2":200 ,"insidekey3":300}}
print(d["k2"][2],d["k3"]["insidekey2"])


# (2) To Add A New Key or To Replace Value 

d = {"k1":100 , "k2":200 , "k3":300}

d["k4"] = 400
print(d)

d["k4"] = "New Value"
print(d)

# (3) Methods In Dictionaries

d = {"k1":123 , "k2":[50,11,21], "k3":{"insidekey1":100 ,"insidekey2":200 ,"insidekey3":300}}

# (3.a) dict.key()                         # It is used to display all the keys in the Dictionary
print(d.keys())

# (3.b) dict.value()                       # It is used to dispaly all the values in the Dictionary
print(d.values())   

# (3.c) dict.items()                       # It is used to dispaly all the keys and values sapratelly inside brackets 
print(d.items())





