# CAPITALIZE METHOD
string = "python CODING 123!"
print(string)
new_string = string.capitalize()
print(new_string)

# LOWER METHOD
string = "python CODING 123!"
print(string)
new_string = string.lower()
print(new_string)

# UPPER METHOD
string = "python CODING 123!"
print(string)
new_string = string.upper()
print(new_string)

# ISDIGIT METHOD
# checks if the string value is
# only composed of digits
only_digits = "12512"
print(only_digits.isdigit())
has_digits = "12mn3"
print(has_digits.isdigit())

# ISALPHA METHOD
# checks if the string value is
# only composed of alphabetical letters
only_letters = "abcdef"
print(only_letters.isalpha())
has_letters = "12mn3"
print(has_letters.isalpha())

# ISSPACE METHOD
# checks if the string value is
# only composed of white spaces
only_spaces = "    "
print(only_spaces.isspace())
has_spaces = "12  3"
print(has_spaces.isspace())

# ISALNUM METHOD
# checks if the string value is
# only composed of alphanumeric characters
has_digits_letters = "12mn3"
print(has_digits_letters.isalnum())
has_digits = "1245@"
print(has_digits.isalnum())

'''
Using not isalnum may seem like a way to
check if there are no digits and letters,
meaning only symbols, but it does not.
It can only check if there is at least one
symbol in the string.
'''
