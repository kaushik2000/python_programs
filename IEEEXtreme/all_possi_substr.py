test_str = input("Enter the string: ")
res = [test_str[i: j] for i in range(len(test_str))
          for j in range(i + 1, len(test_str) + 1)]

# printing result
print("All substrings of string are : " + str(res))
