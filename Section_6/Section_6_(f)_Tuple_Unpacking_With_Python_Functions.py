# Tuple Unpacking With Python Functions

# 1
stock_price = [("Apple",200),("Google",400),("Micro",100)]
for item in stock_price:
    print(item)
for ticker,price in stock_price:
    print(ticker)
    print(price + (0.1*price))

print("_____________________________________")


# 2  By function

work_hours = [("Abby",100),("billy",400),("cassie",800)]
def employee_check(work_hours):

    current_max = 0
    employee_of_month = " "

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    return (employee_of_month,current_max)

print(employee_check(work_hours)) 

name,hours = employee_check(work_hours)
print(name)
print(hours)


print("_____________________________________")





