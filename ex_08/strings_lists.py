# String to list conversion
new_string = "Hello to the world of python"

new_list = new_string.split()
print(new_list)
print(len(new_list))
print(new_list[0])

# split() ignores multiple whitespaces as one
# A delimiter can be used to split at that point in the string. Syntax: split('delimiter')

new_list.remove('of')
print(new_list)

print('Sorting the list:')
new_list.sort()
print(new_list)
