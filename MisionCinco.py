#Autor: Samara Andrea Vega
#Realiza trazos de 600x600 usando la librería PIL/turtle


from PIL import Image, ImageDraw
from random import randint

def dibujarCuadrosCirculos(canvas):
    a = 600
    for i in range(0, 301, 10):
        puntoX = (i, i)
        puntoY = (i+a, i+a)
        canvas.line(puntoX+(i+a, i) + puntoY+(i,i+a) + (i,i), "black")
        canvas.ellipse(puntoX+puntoY, "white", "black")
        a = a - 20
    
def dibujarEstrella(imagen):
    for y in range(0,301, 10):
        a = (300, y)
        b = (300+y, 300)
        rojo = randint(0, 255)
        verde = randint(0, 255)
        azul = randint(0, 255)
        imagen.line(a + b, (rojo, verde, azul))
        
    for y in range(0,301, 10):
        a = (300, y)
        b = (300-y, 300)
        rojo = randint(0, 255)
        verde = randint(0, 255)
        azul = randint(0, 255)
        imagen.line(a + b, (rojo, verde, azul))
        
    for y in range(300, 601, 10):
        a = (300, y)
        b = (-300+y, 300)
        rojo = randint(0, 255)
        verde = randint(0, 255)
        azul = randint(0, 255)
        imagen.line(a + b, (rojo, verde, azul))

    for y in range(0, 301, 10):
        a = (300, 600-y)
        b = (300+y, 300)
        rojo = randint(0, 255)
        verde = randint(0, 255)
        azul = randint(0, 255)
        imagen.line(a + b, (rojo, verde, azul))
        
def dibujarEspiral(canvas):
    a= 600
    for x in range (0, 301, 10):
        puntoA = (x, x)
        puntoB = (x+a, x+a)
        canvas.rectangle(puntoA+ puntoB, "white", "black")
        a = a - 20
    
def dibujarRed(canvas):
    for x in range (0, 601, 20):
        puntoA = (0, x)
        puntoB = (x, 0)
        puntoC = (600, x)
        puntoD = (x, 600)
        canvas.line(puntoA+puntoB, "blue")
        canvas.line(puntoC+puntoD, "blue")

    for x in range (0, 601, 20):
        puntoA = (x, 600)
        puntoB = (0, 600-x)
        puntoC = (600-x, 0)
        puntoD = (600, x)
        canvas.line(puntoA+puntoB, "red")
        canvas.line(puntoC+puntoD, "red")
        
def calcularDivisibles():
    a = 0 
    for n in range (1000, 10000, 1):
       if n%17 == 0:
           a = a + 1
    return a
    
def imprimirPiramide():
    a= 1
    b= 1
    print("Pirámide 1")
    for n in range(1, 10):
            print (a, "* 8 +", b, "=", (a * 8 + b))
            b = b + 1
            a = a * 10 + b

def imprimirPiramideDos():
    a = 1
    print("Pirámide 2")
    for n in range(1, 10):
        print(a, "*", a, "=", a*a)
        a = a * 10 +1

def menu():
    print('''Misión 5. Seleccione qué quiere hacer.
    1. Dibujar cuadros y círculos
    2. Dibujar parábolas
    3. Dibujar espiral
    4. Dibujar red
    5. Contar divisibles entre 17
    6. Imprimir pirámides de números
    0. Salir
    ''')
    elegir = int(input("¿Qué desea hacer? "))
    return elegir

def main():
    
    opcion = menu()
    while opcion != 0:
        if opcion == 1:
            imagen = Image.new("RGB", (600,600), "white")
            canvas = ImageDraw.Draw(imagen)
            dibujarCuadrosCirculos(canvas)
            imagen.show()
            
        elif opcion == 2:
            imagen = Image.new("RGB", (600,600), "white")
            canvas = ImageDraw.Draw(imagen)
            dibujarEstrella(canvas)
            imagen.show()
            
        elif opcion == 3:
            imagen = Image.new("RGB", (600,600), "white")
            canvas = ImageDraw.Draw(imagen)
            dibujarEspiral(canvas)
            imagen.show()
            
        elif opcion == 4:
            imagen = Image.new("RGB", (600,600), "white")
            canvas = ImageDraw.Draw(imagen)
            dibujarRed(canvas)
            imagen.show()
            
        elif opcion == 5:
            divisibles = calcularDivisibles()
            print ("El total de números divisibles entre 17 es: ", divisibles)
            
        elif opcion == 6:
            imprimirPiramide()
            imprimirPiramideDos()
            
        else:
            print("ERROR, solo puedes teclear 1, 2, 3, 4, 5 o 6 como opciones")

        opcion = menu()
        
    print("Termina")
    
main()