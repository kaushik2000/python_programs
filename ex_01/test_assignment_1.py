# Getting user-input and storing it
user_hrs = input("Enter the worked Hours: ")
user_rate = input("Enter the Rate per hour: ")

try:
    hrs = float(user_hrs)
    rate = float(user_rate)
except:
    print("Please enter numeric value!")
    quit()
    
# Problem-statement: Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
if hrs <= 40:
    gross_pay = hrs * rate
else:
    gross_pay = (40 * rate) + (hrs - 40) * (rate * 1.5 )

print(gross_pay)