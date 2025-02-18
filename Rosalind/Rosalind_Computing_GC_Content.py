#Abrimos el archivo de datos
data = open('rosalind_gc.txt', "r")
#Creamos FASTAFile con el archivo de datos pidiendole que nos lo lea linea por linea
FASTAFile = data.readlines()
#Creamos un diccionario para almacenar la informacion de las cadenas, tanto del "Nombre" de 
# la cadena como la propia cadena en si, establecemos tambien una String vacia para almacenar
# a esta última

FASTADict = {}
FASTALabel = ""

print(FASTALabel)

#Creamos la funcion computeGC
def computeGC():
    global FASTALabel #Nos aseguramos que se usa la variable global FASTALabel
    for line in FASTAFile:
        line = line.strip() #Eliminamos los saltos de linea y los espacios en blanco
        if '>' in line: #Si la linea comienza con el símbolo >, esa linea se almacena como FASTALabel
                        # y se le asigna una string vacia
            FASTALabel = line
            FASTADict[FASTALabel] = "" #Añade la nueva etiqueta como clave del diccionario
        else: 
            FASTADict[FASTALabel] += line # Si no, concatena el valor de la linea con el valor de la clave

    print(FASTADict)

computeGC()
#Creamos la funcion para obtener el porcentaje de G/C de las cadenas
def GCcontent(seq):
    #Cuenta las Cs y las Gs, las divide por el total de la cadena y las multiplica por 100 para el %
    return round(((seq.count('C') + seq.count('G'))/ len(seq))*100, 6)

#Creamos ahora un nuevo diccionario para almacenar el resultado en el cual a partir de los items de FASTADict (key y value),
# obtendremos para el primero el valor key original y para value, el return de contentGC
RESULTDict = {key: GCcontent(value) for (key, value) in FASTADict.items()}
print(RESULTDict)

#Por último, creamos una variable para devolver la clave que tiene un value mayor. Usamos max()
# en el diccionario de RESULTDict, pero como los key son Strings, nmecesitamos que tome los datos de la parte de 
# values, que se hace utilizando .get
MaxGCcontent = max(RESULTDict, key = RESULTDict.get)
print('El maximo porcentaje está en la cadena: ' + MaxGCcontent)