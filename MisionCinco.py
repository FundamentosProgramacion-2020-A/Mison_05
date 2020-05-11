# Autor: Paloma Argelia Cueto González
# Programa que contiene un menú y le pregunta al usuario que operacion quiere hacer.

import turtle 
from PIL import Image, ImageDraw
from random import randint


# Funcion que muestra el menú con las opciones y después pregunta
def menu():
    print("Misión 5. Seleccione qué quiere hacer.")
    print("1. Dibujar cuadros y círculos")
    print("2. Dibujar parábolas en forma de estrella")
    print("3. Dibujar espiral")
    print("4. Dibujar red")
    print("5. Contar divisibles entre 17")
    print("6. Imprimir pirámides de números")
    print("0. Salir")
    print (" ")
    opcion = int(input("Qué desea hacer?: "))
    return opcion


# Funcion para dibujar cuadros y circulos
def dibujarCuadrosCirculos(imagen):
    for y in range (1, 300, 10):
        a = (310+y, 290-y)
        b = (310+y, 310+y)
        imagen.line(a+b, "black")
        
    for y in range (1, 300, 10):
        a = (290-y, 290-y)
        b = (290-y, 310+y)
        imagen.line(a+b, "black")
        
    for y in range (1, 300, 10):
        a = (290-y, 290-y)
        b = (310+y, 290-y)
        imagen.line(a+b, "black")
        
    for y in range (1, 300, 10):
        a = (290-y, 310+y)
        b = (310+y, 310+y)
        imagen.line(a+b, "black")
        
    for y in range (1, 300, 10):
        a = (300-y,300-y)
        b = (300+y,300+y)
        imagen.arc(a+b, 0, 360, "black")
        
    
# Funcion que dibuja la estrella
def dibujarEstrella(imagen):
    
    for y in range (0,310, 10):  #Secuencia de 10 en 10
        a = (300,y)
        b = (300+y,300)
        #genera color aleatorio
        rojo = randint (0,255)
        verde = randint (0,255)
        azul = randint (0,255)
        #Para dibujar, primero valores, luego colores
        imagen.line (a+b, (rojo, verde, azul))
        
    for y in range (0,310, 10):  
        a = (300,y)
        b = (300-y,300)
        rojo = randint (0,255)
        verde = randint (0,255)
        azul = randint (0,255)
        imagen.line (a+b, (rojo, verde, azul))
        
    for y in range (310, 0, -10):  #Secuencia de 10 en 10 en negativo
        a = (600-y,300)
        b = (300,300+y)       
        rojo = randint (0,255)
        verde = randint (0,255)
        azul = randint (0,255)
        imagen.line (a+b, (rojo, verde, azul))
        
    for y in range (310, 0, -10):  
        a = (y,300)
        b = (300,300+y)       
        rojo = randint (0,255)
        verde = randint (0,255)
        azul = randint (0,255)
        imagen.line (a+b, (rojo, verde, azul))
        
        
        
# Funcion que usa turtle para dibujar un espiral
def dibujarEspiral():
    turtle.color("black")
    
    for i in range (5, 601, 10):  # Definir haste donde será el espiral
        turtle.forward (i)
        turtle.left (90)
        turtle.forward (i+5)
        turtle.left (90)
        turtle.forward (i+5)
        turtle.left (90)
        turtle.forward (i+10)
        turtle.left (90)
        
        turtle.speed(7)
   
   
# Función para dibujar red de dos colores   
def dibujarRed(imagen):
    
    for y in range (1, 1200, 20):
        a = (580-y, 0)
        b = (600, 20+y)
        imagen.line (a+b, "red")
        
    for y in range (1, 1200, 20):
        a = (20+y, 0)
        b = (0, 20+y)
        imagen.line (a+b, "blue")
        
        
# Funcion que calcula y regresa la cantidad de numeros de 4 digitos que son divisibles entre 17
def dividirNumeros():
    contador = 0
    
    for n in range (1000,10000): 
        if n%17 == 0:   #División que tiene 0 como residuo
            
            contador = contador + 1  # el contador saca los numeros con residuo 0
            
    #print ("Los números", n, "son divisibles entre 17")
    print ("En total, son ", contador, "números de cuatro digitos que se pueden dividir entre 17")

#Función para sacar la piramide de numeros y hace la operación
def calcularPiramide():
    a = 0
    for x in range (1, 10):       
        a = (a * 10) + x
        b = (a * 8) + x
        print (a,"* 8 +", x, "=", b)   
    print ("-----------------------------------")
    c = 0
    d = 0
    for x in range (1, 10):      
        c = (c * 10) + 1
        d = (d * 10) + 1
        e = c * d
        print (c, "*", d,"=", e)
    

# Define la función principal
def main():
    opcion = menu()
    
    while opcion !=0 :
        if opcion == 1:
            img = Image.new("RGB", (600, 600), "white")
            imagen = ImageDraw.Draw(img)
            dibujarCuadrosCirculos(imagen)
            img.show()
            
        elif opcion == 2:
            img = Image.new("RGB", (600, 600), "white")
            imagen = ImageDraw.Draw(img)
            dibujarEstrella(imagen)
            img.show()
            
        elif opcion == 3:
            dibujarEspiral()
            
        elif opcion == 4:
            img = Image.new("RGB", (600, 600), "white")
            imagen = ImageDraw.Draw(img)
            dibujarRed(imagen)
            img.show()
        
        elif opcion == 5:
            print("---------------------------------------------")
            cantidad = dividirNumeros()
            print("---------------------------------------------")
            
        elif opcion == 6:
            print("---------------------------------------------")
            calcularPiramide()
            print("---------------------------------------------")
        
        else:
            print("---------------------------------------------")
            print("ERROR: Favor de insertar un número del 0 al 6")
            print("---------------------------------------------")
        
        opcion = menu()
    

main()