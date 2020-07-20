# Using functions in Python

def total(num1, num2):
    return num1+num2

user_num1 = input('Enter first integer:')
user_num2 = input('Enter second integer:')

num1 = int(user_num1)
num2 = int(user_num2)

sum = total(num1, num2)
print("sum of", num1, "&", num2, "is", sum)