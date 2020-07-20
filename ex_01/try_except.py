# Program to convert Eur-floor to Us-floor level
user_inp = input(">>Enter floor level: ")

# Using Try and Except to catch errors
try:
    eur_floor = int(user_inp)
except:
    print("!!-- Enter valid floor number --!!")
    quit()

# Conversion is done here
us_floor = eur_floor + 1
print(">>The US floor level is:", us_floor) 
