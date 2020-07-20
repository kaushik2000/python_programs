total = 0
count = 0
print('Before', count, total)

for value in [10, 20, 30, 40, 50] :
    count = count + 1
    total = total + value
    print(count, total, value)

average = total / count
print('After', count, total, average)
