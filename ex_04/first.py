print("Hello")

print("Write \"exit\" to come out of the text writer/printer")

while True:
    line = input('> ')
    if line[0] == "#" :
        continue
    if line == "exit" :
        break
    print(line)
print('Done!')

for character in line :
    print(character)