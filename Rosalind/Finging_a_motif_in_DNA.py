

data = open('rosalind_subs.txt', 'r')
# Dividimos el archivo por lineas
string = data.read().splitlines()

s= string[0]
t = string[1]


def finding(s, t):
    posiciones = []
    #Creamos dos variables de longitud para cada una de las cadenas
    len_s = len(s)
    len_t = len(t)
    #El rango de busqueda del bucle for se establece así para asegurarnos que no buscamos fuera de los limites de la cadena s y asi evitar errores
    for i in range(len_s - len_t +1):
        #Si el trozo de cadena (que tiene una longitud de 4 (posicion 0 + longitud de la cadena t, es decir 4)) es igual a t, se añade al array posiciones 
        if s[i:i+len_t] ==t:
             posiciones.append(i+1) #Se añade +1 porque en programacion se empieza en posicion 0, por lo que para nosotros habría que sumarle 1!
    return posiciones

posiciones = finding(s,t)
#Para obtener una lista sin comas convertimos el array en una linea de texto
# para ello usamos map, que convierte en string la lista posiciones. Como esto 
# nos daría una lista igualmente con comas, usamos el método join para que los 
# iterables de la cadena de texto los una en una unica cadena usando el espacio(' ') como separador.
posiciones_sin_comas =  ' '.join(map(str, posiciones))
print(posiciones_sin_comas)






