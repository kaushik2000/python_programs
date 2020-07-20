# Opening a text-file using a file handler

file_handler = open("test_file.txt", "r")
line_count = 0
for line in file_handler :
    print(line)
    line_count = line_count + 1
print("Line count:", line_count)

file_handler = open("test_file.txt", "r")
print("Printing without extra newlines: ")
for line in file_handler :
    line = line.rstrip()
    print(line)