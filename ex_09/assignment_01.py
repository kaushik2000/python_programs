"""
Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committe
"""
counts = dict()
file_name = input("Enter file name: ")
try :
    file_handle = open(file_name) 
except :
    print("file not found...")
    quit()

for line in file_handle :
    line = line.rstrip()
    # Ignoring lines that don't start with "From "
    if not line.startswith("From ") : continue
    # Finding/Slicing the e-mail addresses from the line
    words = line.split()
    email_id = words[1]
    # Updating the count of the occurrence of that email-id in "counts" dict()
    counts[email_id] = counts.get(email_id, 0) + 1
    #print(counts)

#Finding the maximum occurring email address
max_email = None
max_count = None
for email, count in counts.items() :
    if max_count is None or count > max_count :
        max_count = count
        max_email = email


print(max_email, max_count)