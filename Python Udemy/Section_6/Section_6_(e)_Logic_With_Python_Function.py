# Logic With Python Function

def even_check(num):                # check the no. is even or not with logic and function
    result = num % 2 == 0
    return result

print(even_check(20))
print(even_check(43))
print("____________")


def even_check(num):                  # same as above
    return num % 2 == 0
    
print(even_check(20))
print(even_check(43))
print("____________")

# (2) Return even if any no. is even inside a list

def check_even_list(mylist):
    for num in mylist:
        if num % 2 == 0:
            return True
        else:
            pass

print(check_even_list([1,2,3,4,5,6]))
print(check_even_list([1,3,5,7,9,]))
print(check_even_list([2,4,6,8,10]))
print("____________")


def check_even_list(mylist):
    for num in mylist:
        if num % 2 == 0:
            return True
        else:
            pass
    return False

print(check_even_list([1,2,3,4,5,6]))      # Same as above but returns false on odd no.
print(check_even_list([1,3,5,7,9,]))
print(check_even_list([2,4,6,8,10]))
print("____________")

# Return All the even number in a list 

def check_even_list(mylist):
# place holder variable
    even_number = []                    # To put all the even numbers inside the same list

    for num in mylist:
        if num % 2 == 0:
            even_number.append(num)
        else:
            pass
    return even_number

print(check_even_list([1,2,3,4,5,6]))




