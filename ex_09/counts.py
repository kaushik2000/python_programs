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
    max_word = None
    for word,count in counts.items() :
        if max_count == None or count > max_count:
            max_count = count
            max_word = word
        elif count == max_count :
            max_word = max_word + ", " + word

    print("The word(s) \'{}\'".format(max_word), "occurs the most with", max_count, "occurrences\n")
    print("------------------------------------------------------------------------------------------------")