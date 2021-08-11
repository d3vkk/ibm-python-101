# COPY METHOD
lst1 = [1, 2, 3, "Hello", "World"]
lst2 = lst1.copy()
print(lst1)
print(lst2)


# SHALLOW COPY
'''
Slice copy and copy method are shallow copies
Assignment operator does not copy but points
to the original list
'''
lst1 = [1, 2, 3, "Hello", "World"]    # original list
lst2 = lst1                           # assignment operator
lst3 = lst1[:]                        # slice copy
lst4 = lst1.copy()                    # copy method
lst1[0] = 5
lst2[1] = 10
lst3[2] = 15
lst4[3] = 20
print("lst1:", lst1)
print("lst2:", lst2)
print("lst3:", lst3)
print("lst4:", lst4)

# IS OPERATOR
'''
DetermineS if two variables point to the same object
Note: A common mistake is to use the is operator as
a form of the == (equal to) comparison operator.
The two are not the same
'''
lst1 = [1, 2, 3, "Hello", "World"]    # original list
lst2 = lst1                           # assignment operator
lst3 = lst1[:]                        # slice copy
lst4 = lst1.copy()                    # copy method
print(lst2 is lst1)
print(lst3 is lst1)
print(lst4 is lst1)

# ID METHOD
lst1 = [1, 2, 3, "Hello", "World"]    # original list
lst2 = lst1                           # assignment operator
lst3 = lst1[:]                        # slice copy
lst4 = lst1.copy()                    # copy method
print("lst1 address:", id(lst1))
print("lst2 address:", id(lst2))
print("lst3 address:", id(lst3))
print("lst4 address:", id(lst4))

# NESTED LIST
# Declaration
nested_list = [[2, 4, 12], ["A", "B", "C"], [6.5, 4.2, 10.0]]
print(nested_list[0])
print(nested_list[1])
print(nested_list[2])
print(len(nested_list))

# Getters
print(nested_list[0][0])
print(nested_list[1][1])
print(nested_list[2][2])

# Setters
nested_list[0][0] = 20
nested_list[1][1] = "D"
nested_list[2][2] = 40.0
print(nested_list)

# SHALLOW COPY VS DEEP COPy
'''
Shallow copy only copies the first layer of a nested list
whereas a deep copy copies every layer. We will have to
create a deep copy, which copies every single level of the nested lists.
'''

# DEEP COPY
import copy
nested_list = [[2, 4, 12], ["A", "B", "C"], [6.5, 4.2, 10.0]]
nested_list_copy = copy.deepcopy(nested_list)
