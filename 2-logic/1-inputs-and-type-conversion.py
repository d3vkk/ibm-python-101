# INPUT WITH TYPE CONVERSION
x = int(input("Please enter an int "))
print(x + 5)

x = float(input("Please enter a float number "))
print(x * 5)

# FLOAT TO INT CONVERSION
is_a_float = 1.655
is_an_int = int(is_a_float)
print(is_an_int)

# STRING TO FLOAT AND INT CONVERSION
print(float("1.5"))
print(int("3"))

# FLOAT AND INT TO STRING CONVERSION
x = 1.5
print(x)
print(type(x))

y = 3
print(y)
print(type(y))

print(str(x))
print(type(str(x)))
print(str(y))
print(type(str(y)))

# FLOAT, INT AND STRING TO BOOL CONVERSION
print(bool(""))
print(bool("Hello World"))

print(bool(0))
print(bool(1))
print(bool(-1))

print(bool(0))
print(bool(1.5))
print(bool(-1.5))

print(bool(None))
