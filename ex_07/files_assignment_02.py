# Write a program that prompts for a file name, 
# then opens that file and reads through the file, 
# looking for lines of the form: "X-DSPAM-Confidence:    0.8475"
# Count these lines and extract the floating point values from each of the lines 
# and compute the average of those values and produce an output as shown below. 
# Do not use the sum() function or a variable named sum in your solution.

# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
# Prompting user for the file-name
file_name = input("Enter the file name: ")
# Opening the file and reading through the file
try :
    file_handle = open(file_name, 'r')
except :
    print("File cannot be opened:", file_name)
    quit()
# Initialising the running sum
total = 0
count = 0
# Searching the line and extracting the floating-value, summing it immediately
for line in file_handle :
    if "X-DSPAM-Confidence:" in line :
        colon_position = line.find(":")
        line_extract = line[colon_position+1:]
        floating_point_value = float(line_extract)
        total = total + floating_point_value
        count = count + 1

print("Average spam confidence:", total/count)