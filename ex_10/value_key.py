di = {'a' : 22, 'b' : 54, 'c' : 6}
print(sorted(di.items())) # Dictionary items soreted by key

tup = di.items() # Storing the dicyionary items in the tuple

new_tup = list()
for (k, v) in tup :
    new_tup.append( (v, k) )
print(new_tup) # Storing value-key pairs

print(sorted(new_tup, reverse = True)) # Sorting the new_tup in descending order based on values