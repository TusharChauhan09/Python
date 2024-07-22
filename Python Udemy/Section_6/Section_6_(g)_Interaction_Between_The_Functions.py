# Interaction Between The Functions

# example of shuffle function

example = [1,2,3,4,5,6,7]
from random import shuffle
shuffle(example)
print(example)

def shuffle_list(mylist):         # To shuffle the List or box
    shuffle(mylist)
    return mylist

result = shuffle_list(example)
print(result)


print("__________________________________")
# Three cup Monte

mylist = [" ","O"," "]              
shuffle_list(mylist)

def player_guess():
    guess = ""

    while guess not in ["0","1","2"]:    # To pick a no. between 0,1 or  2
        guess = input("Pick a number: 0 , 1 or 2 : ")
    
    return int(guess)


def check_guess(mylist,guess):       # To check that the guess is correct
    if mylist[guess] == "O":
        print("Correct!")
    else:
        print("Wrong")

# INITAL LIST
mylist = [" ","O"," "]

# SHUFFLE LIST
mixedup_list = shuffle_list(mylist)

# USER GUESS
guess = player_guess()

# CHECK GUESS 
check_guess(mixedup_list,guess)








