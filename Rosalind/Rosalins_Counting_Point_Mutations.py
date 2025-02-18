

#Open Rosalid file as read and split it  in two rows using splitlines.
data = open('rosalind_hamm.txt', "r")

dnas = data.read().splitlines()
#now we assing firstsplit to dna1 and secondsplit to dna2
dna1 = dnas[0]
dna2 = dnas[1]

#define a function to count mutations with the counter in 0
def number_mutations():
    count = 0
    #a for loop in wich every lap (i) for the length of dna1 will find out if it dont match de dna2
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            #if it the doesnt match, count increases in 1
            count += 1
    #now count will be the value that number_mutations will return when called
    return count

print(number_mutations())
