# Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Getting the input from the user
hours = input("Enter Hours:")
rate = input("Enter the Rate per hour:")

# Using type-cast and printing the gross_pay after calculation
gross_pay = float(hours) * float(rate)
print("Pay:", gross_pay)