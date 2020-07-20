# Counting the no. of words in a line and the most occuring word
while True:
    if input('Word frequency counter:\n(Enter "Exit" to quit) or (Press Enter to continue): ').lower() == 'exit' : 
        print("Exiting....")
        break

    counts = dict()
    line = input("Enter a line: ")
    words = line.split()
    print("List of words from the entered line\n", words, "\n") # Getting a list of all  words in the line

    print("Counting....")
    for word in words :
        counts[word] = counts.get(word, 0) + 1
    print(counts, '\n')

    # Finding the most occuring word
    max_count = None
    max_word = list()
    for word in counts :
        if max_count == None :
            max_count = counts[word]
            max_word.append(word)
            continue
        if counts[word] > max_count :
            max_count = counts[word]
            max_word.clear()
            max_word.append(word)
        elif counts[word] == max_count :
            max_word.append(word)

    print("The word(s) \'{}\'".format(max_word), "occurs the most with", max_count, "occurrences\n")
    print("------------------------------------------------------------------------------------------------")