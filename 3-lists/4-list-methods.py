# POP
# Removes item from the back of the list
my_list = [1, 2, 3, "Hello", "World"]
print(my_list)
my_list.pop()
print(my_list)

# Store that last item
my_list = [1, 2, 3, "Hello", "World"]
last_item = my_list.pop()
print(last_item)

# Specify index
my_list = [1, 2, 3, "Hello", "World"]
print(my_list.pop(2))
print(my_list)

# REMOVE
# Removes an item by value
my_list = [1, 2, 3, "Hello", "World"]
my_list.remove(3)
print(my_list)

# With duplicates, removes on the first item
my_list = [1, 2, 3, "Hello", "World", 3]
my_list.remove(3)
print(my_list)

# INDEX
# Finds the index value of an item
# With duplicates, finds for the first item
my_list = [1, "Hello", 2, 3, "Hello", "World"]
print(my_list.index("Hello"))

# INSERT
my_list = [1, 2, 3, "Hello", "World"]
my_list.insert(0,4)
# inserts 4 to the front of my_list
print(my_list)
my_list.insert(3,"WORLD")
# inserts "WORLD" to the 3rd index position
print(my_list)

# CLEAR
my_list = [1, 2, 3, "Hello", "World"]
my_list.clear()
print(my_list)

# COUNT
# Count the number of times a value appears in the list
my_list = [1, 2, 3, "Hello", "World", 1, 1]
print(my_list.count(1))
print(my_list.count("Hello"))
print(my_list.count("HELLO"))

# REVERSE
my_list = [1, 2, 3, "Hello", "World"]
print(my_list)
my_list.reverse()
print(my_list)

# SORT NUMBERS
num_lst = [1, 0.5, 3.6, 17, 121, 12.1]
print(num_lst)
num_lst.sort()
print(num_lst)

# SORT ALPHABET
alpha_lst = ['a', 'z','c' ,'b']
print(alpha_lst)
alpha_lst.sort()
print(alpha_lst)
