# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and
# put out an appropriate message and ignore the number.

largest_value = None
smallest_value = None
print('Largest and smallest number calculator (Enter \'done\' to exit)')

while True :
    # Getting user_input
    user_value = input('Enter a number: ')

    # Exits loop if 'done' is entered
    if user_value == 'done' :
        break

    try:
        current_value = int(user_value)
    except:
        print('Invalid input')
        continue

    # Evaluating the smallest and largest number
    if smallest_value is None and largest_value is None :
        largest_value = current_value
        smallest_value = current_value
    else :
        if current_value > largest_value :
            largest_value = current_value
        if current_value < smallest_value :
            smallest_value = current_value

print("Maximum is", largest_value)
print("Minimum is", smallest_value)