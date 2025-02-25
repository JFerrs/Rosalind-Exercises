
dna_string = 'CATTGGGATTATATAACAGCGACCCGATCCTTACTGCACAATCAGCGCTTGCCGTACCGAATAGTTTGTACGTCTCCTCGCCTAGAAGCTCACAGAATTCCCGAACACAAGTCATTACGTGTTGATCATAAAGCCGATGGGTCCCGATATTCGTGGTAGCGAACGCAGTCTAACCGTATCGCTGTGTAACTCGCCTCGGCGACTTCTATATACAAGATTCAAATTTTCTCGCTTGGCTTTTCAAGTTCCAGGGGTACGAGGCCTCGAATGCGCTCCGGGGAGGAGTCCGGTTATAGGTTCGACTCACCCTTCTACAATGTTCACTCGTCTATGCTCGACAGACCTCAGTCTTGTCGTCAACTCCGTATTGAAGGAGGCGTGAAGTCTTCGCAATGCCGGCTATGGCAAAGGGTCCGGCGTATGATCGAGTCAAGCCTCACCGCTTCACATAGTATCCTAGGGTTCGGAGCTAGTTTTCCCGCAAGGTCAAGGGGACTCTATCTTCCGGAGTAGCTTTTCTGCGACGGAGAACCCCTCTTATCTCGAAAAGGGCATTCTAGCCATCTGCCGCAGGGTACTACTTTAACCGTTCTTCTCGTACGATGGCTGTTAATGCGTCTATATAAGACTCTGTAGTTAAGCGACATCGGCCCATGAGGCTGTTGTCACCGTAGGGTAATGTCAGATTCATGATGAAGAGACTCTTTGCTGAAGCGCAAGTTGGCCTATATAAGCGCAGCCGGGGGGTGCGACGCGAAAATTGAAACCCCCAAGAATCACCCCTGACCAAAACAAATTCACGGGGAACCACATGCGGAAAGA'

#Create a dictionary with the bases and their complementary as values.
complementary_symbols = {'A' : 'T', 'T' : 'A', 'C':'G','G': 'C'}
complementary_string = ""

#now a for loop will change the original nucleotid with the complementary and with [::-1] we reverse the string

for base in dna_string:
    complementary_string += complementary_symbols[base]
    reverse_dna_string = complementary_string[::-1]
print(reverse_dna_string)