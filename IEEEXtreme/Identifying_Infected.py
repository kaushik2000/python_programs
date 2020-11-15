'''Bad-virus is a highly contagious virus that can seriously complicate people’s health. This virus is only spread from person to person and the only way to prevent infection (not 100\%100% safe) is by wearing masks.

Chief of epidemiology has received the first case of bad-virus in your country, this case is imported from the other country. In this context, in coordination with the president, it was decided to close the country's borders, prohibit encounters of more than two persons and make the use of masks mandatory. But in order not to affect the economy, no type of quarantine will be carried out.

Two days later, Chief of epidemiology has been notified about the second case of bad-virus (now necessarily is a national case). Knowing that there are NN persons in the country (including the imported case) enumerated by an integer from 1 to NN, they ask you to identify all people who necessarily are infected. For this task, the department of epidemiology provides you with a list of the MM encounters of two persons during this time. You will be given QQ scenarios that you should handle separately. In the ii-th scenario, you will be given the IDs of the first and the second case of bad-virus, and you should count how many people that can be 100\%100% identified as infected (including the first and the second case).


Standard input
The first line contains two integers NN and MM, denoting the number of persons and number of encounters respectively.

Each one of the next MM lines contains two different integers A_iA
​i
​​  and B_iB
​i
​​ , denoting the two persons in the encounter (there aren't two equal pairs of integers).

The next line contains an integer QQ, denoting the number of scenarios.

Each one of the next QQ lines contains two different integers F_iF
​i
​​  and S_iS
​i
​​ , denoting the first and second case of bad-virus in the ii-th scenario.


Standard output
For each scenario, output the number of people that can be 100\%100% identified as infected on a single line.

Input	Output	Explanation
6 5
1 2
1 3
2 4
3 4
4 5
2
1 5
4 3

Below is the illustration of the encounters.


In the first scenario, there are only two ways such that the fifth person can be infected by the first person, i.e. 1 \rightarrow 2 \rightarrow 4 \rightarrow 51→2→4→5 and 1 \rightarrow 3 \rightarrow 4 \rightarrow 51→3→4→5. We cannot identify which one of the second and the third person that is actually infected. So, the people that can be 100\%100% identified as infected are 11, 44, and 55.

In the second scenario, the people that can be 100\%100% identified as infected are 33 and 44.'''

'''def resolve(first, last, mapping, enc):
    if type(first) != list():
        first = first
    else:
        first = int(first[0])
    mapping.append(first)
    mapping.append(enc[first])
    if enc[first] == last:
        return mapping
    else:
        return resolve(eninputc[first], last, mapping, enc)
'''
user_input = input("Enter the number of people and the encounters: ")
user_input = user_input.split(" ")
# People count
N = int(user_input[0])
#print(N)
# Encounter count
M = int(user_input[1])
#print(M)

encounters = []
for count in range(M):
    print("Enter encounter {}".format(count+1))
    user_input = input()
    user_input = user_input.split(" ")
    encounters.append([ int(user_input[0]), int(user_input[1]) ])

print(encounters)
case_count = int( input("Enter the number of reported cases: ") )

while case_count != 0:
    dup_enc = encounters
    print(dup_enc)
    chain_list = list()
    encounter_chain = list()
    user_input = input("Enter the first and last reported cases")
    user_input = user_input.split(" ")
    first = int(user_input[0])
    #print(first)
    last = int(user_input[1])
    #print(last)
    for i in range(len(dup_enc)):
        if dup_enc[i].count(first) != 1 : continue

        encounter_chain.append(first)
        print(encounter_chain)
        new_index = dup_enc.index(first)-1
        first = dup_enc[new_index]
        print(first)
