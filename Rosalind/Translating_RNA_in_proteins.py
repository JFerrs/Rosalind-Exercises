#Cargamos una tabla de codones de ARN
codon_table = { 
    'AUG': 'M', 'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'AUU': 'I', 
    'AUC': 'I', 'AUA': 'I', 'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 
    'GUG': 'V', 'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'ACU': 'T', 
    'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'GCU': 'A', 'GCC': 'A', 
    'GCA': 'A', 'GCG': 'A', 'UAU': 'Y', 'UAC': 'Y', 'CAU': 'H', 
    'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'AAU': 'N', 'AAC': 'N', 
    'AAA': 'K', 'AAG': 'K', 'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 
    'GAG': 'E', 'UGU': 'C', 'UGC': 'C', 'UGG': 'W', 'CGU': 'R',
    'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGU': 'S', 'AGC': 'S', 
    'AGA': 'R', 'AGG': 'R', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 
    'GGG': 'G', 'UAA': 'Stop', 'UAG': 'Stop', 'UGA': 'Stop' }

#Abrimos el archivo de rosalind y lo leemos, no hace falta splitearlo

data = open('rosalind_prot.txt', 'r')

rna_string = data.read()

#Creamos una funcion para convertir la cadena a proteinas por tripletes
def rna_into_protein(rna_string):
    protein_string  = "" #Creamos una variable vacia para almacenar el string proteina
    for base in range(0, len(rna_string), 3): #Establecemos que recorra cada una de las bases de toda la cadena de rna, pero cada 3 de ellas, porque si no se pisarían
        codon = rna_string[base:base+3]# Los codones son tripletes de bases, por lo que establecemos que coga desde la base 0 hasta la 0+3 para cada uno de los rangos que hemos establecido en la linea de arriba
        aminoacid = codon_table.get(codon, '') #Si el codon está en el codon_table, con .get cogerá el valor correspondiente, si no, devolvera una string vacia ''.
        #Otra forma de hacerlo más explicito y claro sin usar .get.
        # if codon in codon_table:
        # amino_acid = codon_table[codon]
        # else:
        # amino_acid = ''
        if aminoacid == 'Stop':
            break
        protein_string += aminoacid
    return protein_string

protein_string = rna_into_protein(rna_string)

print(protein_string)