#Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

#edad = int(input("Ingrese su Edad: "))

#if edad > 18:
#    print("Es mayor de edad")
#pass

#Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”

#nota = int(input("Ingrese su nota: "))

#if nota >= 6:
#    print("Aprobado")
#else:
#    print("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

#num = int(input("Ingrese un numero: "))

#if num % 2 == 0:
#    print("Ha ingresado un numero par")
#else:
#    print("Por favor ingrese un numero par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

#edad = int(input("Ingrese su edad: "))

#if edad < 12:
#    print("Perteneces a la categoria: Niño/a")
#elif edad >= 12 and edad < 18:
#    print("Perteneces a la categoria: Adolecente")
#elif edad >= 18 and edad < 30:
#    print("Perteneces a la categoria: Adulto/a joven")
#elif edad >= 30:
#    print("Perteneces a la categoria: Adulto/a")

# Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.

#contrasenia = input("Ingrese su contraseña:")

#if len(contrasenia) >= 8 and len(contrasenia)<= 14:
#    print("Ha ingresado una contraseña corresta")
#else:
#    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# El paquete statistics de python contiene funciones que permiten tomar una lista de números
#y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
#siguiente:
#from statistics import mode, median, mean
#mi_lista = [1,2,5,5,3]
#mean(mi_lista)
#En la documentación oficial se puede encontrar más información sobre este paquete:
#https://docs.python.org/es/3.8/library/statistics.html.
#La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
#pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
#● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
#mediana es mayor que la moda.
#● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
#la mediana es menor que la moda.
#● Sin sesgo: cuando la media, la mediana y la moda son iguales.
#Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#Definir la lista numeros_aleatorios de la siguiente forma:
#import random
#numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
#Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
#forma aleatoria.

#import random
#from statistics import mean, median, mode

#numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

#print("Lista:", numeros_aleatorios)

#media = mean(numeros_aleatorios)
#print("Media: " , media)
#mediana = median(numeros_aleatorios)
#print("Mediana: ", mediana)
#moda = mode(numeros_aleatorios)
#print("Moda: ", moda)

#if media > mediana > moda:
#    print("Sesgo positivo")
#elif media < mediana < moda:
#    print("Sesgo negativo")
#elif media == mediana == moda:
#    print("Sin sesgo")


#Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.


#palabra = input("Ingrese una palabra o frase: ")

#vocal = "aeiouAEIOU"

#if len(palabra) > 0 and palabra [-1] in vocal:
#    palabra = palabra + "!"

#print (palabra)

#Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
#dependiendo de la opción que desee: 
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
#lower() y title() de Python para convertir entre mayúsculas y minúsculas. 

#nombre = input("Ingrese su nombre: ")

#opcion = int(input("Ingrese: 1 si quiere su nombre en mayuscula.2 si quiere su nombre en minuscula. 3 si quiere su nombre con la primera letra en mayuscula: "))

#if opcion == 1:
#    print(nombre.upper())
#elif opcion == 2:
#    print(nombre.lower())
#elif opcion == 3:
#    print (nombre.title())

#Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
#por pantalla: 
#● Menor que 3: "Muy leve" (imperceptible). 
#● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
#● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
#generalmente no causa daños). 
#● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
#débiles). 
#● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

#magnitud = float(input("Por favor ingrese la marnitud del terremoto en escala Richter: "))

#if magnitud < 3:
#    print("Muy leve (imperceptible)")
#elif magnitud >= 3 and magnitud < 4:
#    print ("leve (ligeramente perceptible)")
#elif magnitud >= 4 and magnitud < 5:
#    print("Moderado (Sentido por personas pero generalmente no causa daños)")
#elif magnitud >= 5 and magnitud < 6:
#    print("Fuerte (Puede causar daños a estructuras debiles)")
#elif magnitud >=6 and magnitud < 7:
#    print("Muy Fuerte (Puede causar daños significativos)")
#elif magnitud >= 7:
#    print("Extremo (puede causar graves daños a gran escala)")

#Utilizando la información aportada en el pdf del trabajo practico condicionales en el punto 10 

#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
#si el usuario se encuentra en otoño, invierno, primavera o verano. 

emisferio = input("Por favor ingrese el emisferio en el que se encentra con una S para sur y una N para norte: ")

fecha_dia = int(input("Ingrese en que dia del mes se encuentra: "))

fecha_mes = int(input("Ingrese el mes en el que se encuentra teniendo en cuenta que enero es 1, febrero es 2, marzo es 3 y asi susesivamente: "))

if emisferio == "N" or emisferio == "n":
    if fecha_mes == 12 :
        if fecha_dia >= 21:
            print ("Estas en Invierno")
        elif fecha_dia <= 20:
            print("Estas en Otoño")
        else:
            print("Ingrese un dia valido")
    elif fecha_mes == 1 :
        print ("Estas en Invierno")
    elif fecha_mes == 2:
        print ("Estas en Invierno")
    elif fecha_mes == 3:
        if fecha_dia <= 20 :
            print ("Estas en Invierno")
        elif fecha_dia >= 21:
            print ("Estas en Primavera")
        else:
            print("Ingrese un dia valido")
    elif fecha_mes == 4 :
        print ("Estas en Primavera")
    elif fecha_mes == 5:
        print ("Estas en Primavera")
    elif fecha_mes == 6:
        if fecha_dia <= 20 :
            print ("Estas en Primavera")
        elif fecha_dia >= 21:
            print ("Estas en Verano")
        else:
            print("Ingrese un dia valido")
    elif fecha_mes == 7 :
        print ("Estas en Verano")
    elif fecha_mes == 8:
        print ("Estas en Verano")
    elif fecha_mes == 9:
        if fecha_dia <= 20 :
            print ("Estas en Verano")
        elif fecha_dia >= 21:
            print ("Estas en Otoño")
        else:
            print("Ingrese un dia valido")
    elif fecha_mes == 10 :
        print ("Estas en otoño")
    elif fecha_mes == 11:
        print ("Estas en otoño")
    else:
        print("Ingrese un mes valido")

if emisferio == "S" or emisferio == "s":
    if fecha_mes == 12 :
        if fecha_dia >= 21:
            print ("Estas en Verano")
        elif fecha_dia <= 20:
            print("Estas en Primavera")
        else:
            print("Ingrese un dia valido")
    elif fecha_mes == 1 :
        print ("Estas en Verano")
    elif fecha_mes == 2:
        print ("Estas en Verano")
    elif fecha_mes == 3:
        if fecha_dia <= 20 :
            print ("Estas en Verano")
        elif fecha_dia >= 21:
            print ("Estas en Otoño")
        else:
            print("Ingrese un dia valido")
    elif fecha_mes == 4 :
        print ("Estas en Otoño")
    elif fecha_mes == 5:
        print ("Estas en Otoño")
    elif fecha_mes == 6:
        if fecha_dia <= 20 :
            print ("Estas en Otoño")
        elif fecha_dia >= 21:
            print ("Estas en Invierno")
        else:
            print("Ingrese un dia valido")
    elif fecha_mes == 7 :
        print ("Estas en Invierno")
    elif fecha_mes == 8:
        print ("Estas en Invierno")
    elif fecha_mes == 9:
        if fecha_dia <= 20 :
            print ("Estas en Invierno")
        elif fecha_dia >= 21:
            print ("Estas en Primavera")
        else:
            print("Ingrese un dia valido")
    elif fecha_mes == 10 :
        print ("Estas en Primavera")
    elif fecha_mes == 11:
        print ("Estas en Primavera")
    else:
        print("Ingrese un mes valido")






