from principal import *
from configuracion import *
import random
import math

def lectura(diccionario):
    lemario = "lemario.txt"
    with open(lemario,"r",encoding="latin-1") as archivo:
        for linea in archivo:
            palabra = linea.rstrip('\n')
            diccionario.append(palabra)
    return diccionario

diccionario = []


def dame7Letras(list1,list2,list3): #tomo como parametros 3 listas
    cadena="" #Creo una cadena vacia
    vocales=random.sample(list2, random.randint(2, 3)) #Con random.sample selecciono una vocal de forma aleatoria, con random.randint aleatoriamente se elige entre 2 y 3 (quien determinara la cantidad de vocales que se elegirán)
    cadena=cadena+"".join(vocales) #Agrego lo anterior a la cadena

    cantidadDeLetras=4 if len(vocales)==2 else 3 #La cantidad de letras a elegir se condiciona: serán 4 si las vocales en el paso anterior fueron 2, sino serán 3
    letras=random.sample(list1,cantidadDeLetras) #uso random.sample para que aleatoriamente elija las letras
    cadena=cadena+"".join(letras) #Agrego lo anterior a la cadena

    consonanteDif=random.choice(list3) #Elijo una consonante dificil aleatoriamente con random
    cadena=cadena+"".join(consonanteDif) #Agrego lo anterior a la cadena

    desordenarCadena=random.sample(cadena,len(cadena)) #Paso como argumento la cadena y su longitud, para que random.sample la desordene aleatoriamente
    cadenaDesordenada="".join(desordenarCadena) #Almaceno la cadena desordenada en la variable

    return cadenaDesordenada #retorno la cadena desordenada

letras=["b","c","d","f","g","h","j","l","m","n","p","q","r","s","t","u","v","w"]
vocales=["a","e","i","o","u"]
consonanteDif=["k","x","y","z"]

dame7Letras(letras,vocales,consonanteDif) #llamo a la función

#elige una letra de las letras en pantalla
def dameLetra(letrasEnPantalla): #toma el parámetro de letras en pantalla
    cadena=letrasEnPantalla #Se pasa el valor del letras en pantalla a una variable llamada cadena
    letraAleatoria=random.choice(cadena) #Se utiliza random choice para elegir una letra aleatoria de la cadena

    return letraAleatoria #retorna la letra aleatoria elegida anteriormente


#chequea que se use la letra principal, solo use letras de la pantalla y
#exista en el diccionario
def esValida(letraPrincipal, letrasEnPantalla, candidata, diccionario):
    if letraPrincipal in candidata:
        for letra in candidata:
            if letra not in letrasEnPantalla:
                return False
        if candidata in diccionario:
            return True
    return False


#Esta funcion toma a la palabra del usuario y verifica que no haya salido, luego que cumpla los codicionales para otorgar los puntos y agregarla a la lista de yaSalieron.Si no cumple los requisitos, resta ptos.
palabrasSalidas=[]
def procesar(letraPrincipal, candidata, diccionario, palabrasSalidas):
    if candidata in palabrasSalidas:
        return -1
    elif len(candidata) >= 3 and letraPrincipal in candidata and candidata in diccionario:
        palabrasSalidas.append(candidata)
        return puntos(candidata)
    else:
        return -1


#devuelve los puntos
def puntos(candidata):

    if len(candidata)==3:
        return(1)
    if len(candidata)==4:
        return(2)
    if len(candidata)==5 or len(candidata)==6:
        i=1
        for i in range(len(candidata)):
            i=i+1
        return(i)
    if len(candidata)>=7:
        return(10)
    else:
        return(-1)

#busca en el diccionario paralabras correctas y devuelve una lista de estas
def dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario):
    algunasCorrectas = []
    cont=0  # Variable para contar las palabras encontradas
    for palabra in diccionario:
        if letraPrincipal in palabra:
            todasCumplen=True
            for letra in palabra:
                if letra not in letrasEnPantalla:
                    todasCumplen=False
                    break
            if todasCumplen:
                algunasCorrectas.append(palabra)
    return algunasCorrectas