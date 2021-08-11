# FOR LOOP
'''
range(start = 0, stop, steps = 1), simplified to range(stop)
range(start, stop, steps = 1), simplified to range(start, stop)
range(start, stop, steps)
'''
for i in range(10):
    print(i)

# ITERATE THROUGH A SLICE
for i in range(10)[:5]:
    print(i)

# PRINT LIST ITEMS
beverages = ["water", "juice", "soda", "tea", "coffee"]
for i in range(len(beverages)):
    print(beverages[i])

# TWO STEPS
for i in range(0, 10, 2):
    print(i)

# ITERATE BACKWARDS
for i in range(5, 0, -1):
    print(i)

# ITERATING THE LOOP TWICE OVER
beverages = ["water", "juice", "soda", "tea", "coffee"]
for i in range(-len(beverages), len(beverages)):
    print(beverages[i])

# PRINT CHARACTERS IN A STRING
string = "Alphabet"
for char in string:
    print(char)

# PRINT CHARACTERS IN A STRING SEPARATED BY WHITESPACE
string = "Alphabet"
for char in string:
    print(char, end = " ")

# PRINT CHARACTERS IN A STRING SEPARATED BY COMMAS
string = "Alphabet"
for char in string:
    print(char, end = ",")

# MULTIPLY INTEGERS IN A LIST BY 2
int_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(int_list)):
    int_list[i] *= 2
print(int_list)

# FOR IN LOOP
beverages = ["water", "juice", "soda", "tea", "coffee"]
if "soda" in beverages:
    print("I will purchase soda.")
else:
    print("Soda is not available.")

# Not operator can also be used
beverages = ["water", "juice", "soda", "tea", "coffee"]
if "soda" not in beverages:
    print("Soda is not available.")
else:
    print("I will purchase soda.")

# PRINT LOWER LEFT ISOSCELES RIGHT TRIANGLES
n = 3
for i in range(n):
    print(n*"*")
    n -= 1

# NESTED FOR LOOPS
nested_list = [[1, 2, 3], ["a", "b"], [10.5, 22.4]]
for lst in nested_list:
    for val in lst:
        print(val)

# MUTATING THE LAST VALUE OF EACH LIST
nested_list = [[1, 2, 3], ["a", "b"], [10.5, 22.4]]
for lst in nested_list:
    lst[-1] *= 2
print(nested_list)

# COMPREHENSION SYNTAX
# This is the equivalent of
int_list = [ i for i in range(10)]
print(int_list)
# This
int_list = []
for i in range(10):
    int_list.append(i)
print(int_list)

# Squaring the values
int_list = [ i**2 for i in range(10)]
print(int_list)
# Equivalent
int_list = []
for i in range(10):
    int_list.append(i**2)
print(int_list)

# Printing even numbers only
int_list = [ i for i in range(10) if i%2 == 0]
print(int_list)
# Equivalent
int_list = []
for i in range(10):
    if i%2 == 0:
        int_list.append(i)
print(int_list)

# PRACTICE
# Printing odd numbers only
int_list = [ i for i in range(16) if i%2 != 0]
print(int_list)

# Printing squares of odd numbers
int_list = [ i for i in range(16) if i%2 != 0]
print(int_list)

# Removes vowels in a string
string = "Alphabet"
string = string.lower()
vowels = ['a', 'e', 'i', 'o', 'u']
lst = []
for char in string:
    if char not in vowels:
        lst.append(char)
print(lst)
