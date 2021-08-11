# STRING CONCATENATION BY ADDITION
string1 = "Hello"
string1 += "World"
print(string1)

# STRING CONCATENATION BY MULTIPLICATION
string1 = "Hello"
string1 *= 3
print(string1)

'''
Because strings are immutable, a new string
object is created during concatenation. This
can be seen in the different memory addresses
'''
string1 = "Hello"
print(id(string1))
string1 += "World"
print(id(string1))

string1 = "Hello"
print(id(string1))
string1 *= 3
print(id(string1))

# LIST CONCATENATION BY ADDITION
lst = [1, 2, "a", "b"]
lst += ["hello", 5]
print(lst)

# LIST CONCATENATION BY EXTEND METHOD
lst = [1, 2, "a", "b"]
lst.extend(["hello", 5])
print(lst)

'''
Because lists are mutable, a new list
object does not need to be created during
concatenation and mutation. This can be
seen in the unchanging memory address
of the list
'''
lst = [1, 2, 3]
lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
lst3 = [1, 2, 3]

print("\nConcatenating: +")
print(id(lst1))
lst1 = lst1 + lst
print(id(lst1))

print("\nMutating: +=")
print(id(lst2))
lst2 += lst2
print(id(lst2))

print("\nMutating: extend")
print(id(lst3))
lst3.extend(lst3)
print(id(lst3))

print("\nChecking the Values in the lists:\n")
print(lst1)
print(lst2)
print(lst3)

# LIST CONCATENATION BY MULTIPLICATION
llst = [1, 2, 3]
lst *= 3
print(lst)
