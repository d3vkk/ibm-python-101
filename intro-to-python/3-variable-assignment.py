# Variable definition
x = 1.5          # The variable x now has the float value 1.5
y = 2            # The variable y now has the int value 2
z = "Hello"      # The variable z now has the string value “Hello”

# Naming variables
my_Variable = 1.5
my_Variable_2 = 2
MyVariable3 = "Hello"

# Unacceptable naming
# 1Variable = 5            # variable names cannot start with digits (1)
# Variable@3 = “Hello”     # variable names cannot contain symbols (@)
# “Hello” = “hello”        # variable names cannot contain symbols (“ and ”)

# print = 10               # using keywords
# print("Hello World")


# Prinitng variables
x = 1.5
y = 2
z = "Hello"
print(x)
print(y)
print(z)

# Reassignment
x = 12
y = x
print(x)
print(y)

# Dynamically typed (i.e. no variable type declaration)
x = 12
x = "twelve"
print(x)

# Swapping (Long Form)
x = 10
y = "ten"
# Step 1
temp = x
# temp now has 10
# Step 2
x = y
#x now has the value of y, which is "ten"
# Step 3
y = temp
# y now has the value of temp, which is 10 (the original value of x)
print(x)
print(y)

# Swapping (Short Form)
x = 10
y = "ten"
# Step 1
x,y = y,x
print(x)
print(y)

# Swapping example
you = "apple"
friend = "money"

you,friend = friend,you

print(friend)
print(you)

# Nonetype variable
x = None
print(x)
print(type(x))
