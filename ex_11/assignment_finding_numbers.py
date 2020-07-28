# Finding Numbers in a Haystack
# In this assignment you will read through and parse a file with text and numbers. 
# You will extract all the numbers in the file and compute the sum of the numbers.
import re

file_name = input("Enter the file name: ")
try:
    file_handle = open(file_name)
except:
    print("File cannot be opened:", file_name)
    quit()

num_list = list()
for line in file_handle :
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line) # Removing numbers in each line
    if len(numbers) == 0 : continue 
    for number in numbers : 
        number = int(number)
        num_list.append(number)
    
print("Sum:", sum(num_list))
    