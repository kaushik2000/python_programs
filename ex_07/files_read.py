# Reading an entire file as a string

file_handler = open("test_file.txt", "r")

file_read = file_handler.read()
print(file_read)

for line in file_read :
    print(line)