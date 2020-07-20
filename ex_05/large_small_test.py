largest_value = None
smallest_value = None
print("Before", smallest_value, largest_value)

for current_value in [132, 5, 65, 25, 4, 818] :
    if smallest_value is None and largest_value is None :
        largest_value = current_value
        smallest_value = current_value
    else :
        if current_value > largest_value :
            largest_value = current_value
        if current_value < smallest_value :
            smallest_value = current_value

print("After", smallest_value, largest_value)