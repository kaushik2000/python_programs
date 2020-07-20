# Lists are mutable; Strings are immutable(Item assignment not allowed)
size = input("Enter the size of the list: ")
number_list = list()
for count in range(int(size)) :
    input_num = input("Enter the integer no. {}: ".format(count+1))
    input_num = int(input_num)
    number_list.append(input_num)
    print(number_list)

total = sum(number_list)
count = len(number_list)
average = total/count
print("Sum:", total, "\nCount", count, "\nAverage:", average)