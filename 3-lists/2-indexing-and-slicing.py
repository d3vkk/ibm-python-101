# POSITIVE INDEXING
# First index
string = "Hello World"
first_char = string[0]
print(first_char)

# Last index
string = "Alphabet"
last_char = string[len(string)-1]
print(last_char)

# NEGATIVE INDEXING
# First index
string = "Hello World"
first_char = string[-len(string)]
print(first_char)

# Last index
string = "Alphabet"
last_char = string[-1]
print(last_char)

# SLICING
# For slicing, it is collection[start:end].
# By default, start is 0, and end is len(collection).

# SLICING AT THE START
string = "Alphabet"
slice_start3 = string[3:]
print(slice_start3)

# SLICING AT THE END
string = "Alphabet"
slice_end3 = string[:3]
print(slice_end3)

# SLICING TO COPY A STRING
slice_copy = string[:]
print(slice_copy)
string = "Alphabet"

# SLICING AT THE START AND END
string = "Alphabet"
slice2_to_6 = string[2:6]
print(slice2_to_6)

# SLICING USING NEGATIVE INDICES
string = "Alphabet"
slice_end_negative_1 = string[:-1]
print(slice_end_negative_1)
string = "Alphabet"
slice_start_negative_1 = string[-1:]
print(slice_start_negative_1)
