# APPEND
# Adds item to the back of the list
grocery_list = ["milk", "eggs", "bread", "rice"]
grocery_list.append(20.00)
print(grocery_list)
print(len(grocery_list))

# GETTER/ACCESS
# Positive indexing
grocery_list = ["milk", "eggs", "bread", "rice", 20.00]
print(grocery_list[0])
print(grocery_list[4])

# Negative indexing
grocery_list = ["milk", "eggs", "bread", "rice", 20.00]
print(grocery_list[-5])
print(grocery_list[-1])

# SETTER
# Updating items using indices
grocery_list = ["milk", "eggs", "bread", "rice", 20.00]
print(grocery_list)
grocery_list[0] = "juice"
print(grocery_list)

# SLICING
grocery_list = ["milk", "eggs", "bread", "rice"]
your_list = grocery_list[:2]
my_list = grocery_list[2:]
print(your_list)
print(my_list)

# SLICING TO COPY A LIST
grocery_list = ["milk", "eggs", "bread", "rice"]
my_slice = grocery_list[:]
print(my_slice)
