# AND OPERATOR
# With Booleans
is_soda = True
have_money = True
is_thirsty = False
if is_soda and have_money and is_thirsty:
    print("I will purchase this drink")
else:
    print("I will not purchase this drink")
    if is_soda == False:
        print("Soda is not available")
    if have_money == False:
        print("I do not have money")
    if is_thirsty == False:
        print("I am not thirsty")

# For Comparisons
num = int(input("Please enter an integer value "))
if num > 0 and num < 20:
    print("The number is positive and less than 20 ")
elif num > 0:
    print("The number is positive")
else:
    print("The number is not positive")

# OR OPERATOR
fever = True
cough = False
fatigue = False
if (fever or cough or fatigue):
    print("I will see a doctor")

# NOT OPERATOR
password = "3422"
if not password == "8734":
    print("Sorry, that's the wrong password")

# With int
if 1:
    print("1 is True")
if not 0:
    print("not 0 is True")

# With NoneType
x = None
if not x:
    print("not None is True")
