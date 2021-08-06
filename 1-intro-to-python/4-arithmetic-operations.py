# BASIC ARITHMETIC OPERATORS
Var1 = 10
Var2 = 10 + 2   # Addition
Var3 = 10 - 2   # Subtraction
Var4 = 10 * 2   # Multiplication
Var5 = 10 / 2   # Division
print(Var1)
print(Var2)
print(Var3)
print(Var4)
print(Var5)

# WITH VARIABLES
Var1 = 10         # Assignment
Var2 = Var1 + 2   # Addition
Var3 = Var1 - 2   # Subtraction
Var4 = Var1 * 2   # Multiplication
Var5 = Var1 / 2   # Division
print(Var1)       # int
print(Var2)       # int
print(Var3)       # int
print(Var4)       # int
print(Var5)       # float

# WITHOUT VARIABLES
print(10)
print(10 + 2)
print(10 - 2)
print(10 * 2)
print(10 / 2)

# WITH FLOAT DATA TYPES
Var1 = 12.5 + 2.5   # Addition
Var2 = 12.5 - 2.5   # Subtraction
Var3 = 12.5 * 2.5   # Multiplication
Var4 = 12.5 / 2.5   # Division
print(Var1)         # float
print(Var2)         # float
print(Var3)         # float
print(Var4)         # float

# VARIABLE UPDATE OPERATOR
# Also applies to multiplication and power operator
x = 6
x += 6
print(x)

x = 5
x = x + 5 + 5
print(x)

# POWER OPERATOR
Num1 = 5**2
print(Num1)

Num1 = 5**2.0
Num2 = 5.0**2
print(Num1)
print(Num2)

Num1 = 5.0**2.0
print(Num1)

# INTEGER DIVISION OPERATOR
# Rounds down to the closest integer
print(14 // 3)
print(14.0 // 3)

# MODULAR OPERATOR
# Gives you the remainder
print(14 % 3)
print(14.0 % 3.0)

# ADDITION OF STRINGS
String1 = "Orange" + "Juice"
print(String1)

String1 = "Orange"
String2 = "Juice"
String3 = String1 + String2
print(String3)

String1 = "Orange"
String2 = "Juice"
print(String1 + String2)

# MULTIPLICATION OF STRINGS
String1 = "Orange"
String2 = String1 * 3
print(String1)
print(String2)

# VARIABLE UPDATE OPERATOR ON STRINGS
string1 = "Apple"
string1 += "Juice" # addition
print(string1)

string1 = "Apple"
string1 *= 3
print(string1)
