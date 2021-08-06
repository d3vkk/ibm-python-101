# IF STATEMENT
cost = 2.00
money = 3.00
if money > cost:
    print("I can afford the Apple")

# Boolena is the type of a condition
cost = 1.5
money = 4.5
print(money > cost)
print(type(money > cost))

# IF ELSE STATEMENT
num = 19
if num > 0:
    print("The number is positive")
else:
    print("The number is not positive")

# NESTED IF ELSE STATEMENTS
num = 19
if num > 0:
    if num < 20:
        print("The number is positive and less than 20")
    else:
        print("The number is positive")
else:
    print("The number is not postive")

# ELIF STATEMENT
drink = input("What drink is available?")
if drink == "soda":
    print("I will purchase soda")
elif drink == "juice":
    print("I will purchase juice")
else:
    print("I will purchase water")

# COMPARISON OPERATORS
num = float(input("Please enter a number")
if 10.5 < num < 20.5:
    print("The number is between 10.5 and 20.5, exclusively")

num = float(input("Please enter a number")
if 10.5 <= num <= 20.5:
    print("The number is between 10.5 and 20.5, inclusively")

# STRING COMPARISON USING ORDINANCE
# Ordinance is the numerical ranking of
# each character using an ASCII table
String1 = "Hello"
String2 = "World"
print(String1 < String2)

# PRACTICE (LONG FORM)
is_water = input("Is water available (True or False)?")
if is_water == "True":
    is_water = True
else:
    is_water = False
if is_water == True:
    print("I will purchase this drink")
else:
    print("I will not purchase this drink")

# PRACTICE (SHORT FORM)
is_water = input("Is water available (True or False)?")
if is_water == "True":
    print("I will purchase this drink")
elif is_water == "False"
    print("I will not purchase this drink")
