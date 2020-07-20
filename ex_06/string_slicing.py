# Getting full-name from the user
full_name = input('Enter full name: ')

# Finding the whitespace's "index" in the string
# index_of_whitespace = -1
# for letter in full_name :
#     index_of_whitespace = index_of_whitespace + 1
#     if letter == ' ' :
#         break
index_of_whitespace = full_name.find(' ')

# Slicing the obtained full-name into first and last names
print('Index of whitespace:', index_of_whitespace)
print('Position of whitespace:', index_of_whitespace)
print('First name:', full_name[:index_of_whitespace])
print('Last name:', full_name[index_of_whitespace+1:])