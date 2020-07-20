# Trying out 'elif' block

user_number = input("Enter a number: ")
number = int(user_number)

if number <= 0:
    print(number, "is less than or equal to zero")
elif number <= 10:
    print(number, "is smaller")
elif number <= 20:
    print(number, "is small")
elif number <= 30:
    print(number, "is medium")
elif number <= 40:
    print(number, "is large")
elif number <= 50:
    print(number, "is larger")
else:
    print(number, "is ginarmous")