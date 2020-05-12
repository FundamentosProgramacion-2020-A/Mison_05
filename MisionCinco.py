#Paulina Mendoza Iglesias
#Programa que arroja un menú para resolver distintas funciones

from PIL import Image, ImageDraw
from random import randint
import turtle

def dibujarCuadradosCirculos(): #función que dibuja círculos y cuadrados
    img = Image.new("RGB", (600,600), "white")
    canvas = ImageDraw.Draw (img)
    
    a=600
    for x in range (0, 301, 10):
        pa = (x,x)
        pb = (x+a, x+a)
        canvas.line(pa+(x+a, x) + pb + (x,x+a)+(x+x), "black")
        canvas.ellipse (pa+pb, "white", "black")
        a = a - 20
        
    
    img.show()
    
def dibujarEstrella(): #función que dibuja la figura estrella
    imgEstrella = Image.new ("RGB", (600,600), "white")
    canvas = ImageDraw.Draw(imgEstrella)
    
    for y in range (0, 301, 10):
        a = (300, y)
        b = (300+y, 300)
        verde = randint (0, 255)
        azul = randint (0,255)
        rojo = randint (0, 255)
        imagen.line (a + b (rojo, verde, azul))
        
    for y in range (0, 301, 10):
        a = (300, y)
        b = (300-y, 300)
        verde = randint (0, 255)
        azul = randint (0,255)
        rojo = randint (0, 255)
        imagen.line (a + b (rojo, verde, azul))
        
    for y in range (0, 301, 10):
        a = (x, 300)
        b = (300, 300+x)
        verde = randint (0, 255)
        azul = randint (0,255)
        rojo = randint (0, 255)
        imagen.line (a + b (rojo, verde, azul))
        
    for y in range (0, 301, 10):
        a = (300+x, 300)
        b = (300, 600-x)
        verde = randint (0, 255)
        azul = randint (0,255)
        rojo = randint (0, 255)
        imagen.line (a + b (rojo, verde, azul))
        
        
def dibujarEspiral():
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.right(90)
    for x in range (0, 606, 5):
        turtle.forward(x)
        turtle.left(90)
        
def dibujarRed():
    imgRed = Image.new("RGB", (600,600), "white")
    canvas = ImageDraw.Draw (imgRed)
    for x in range (20,601,20):
        a = (0,x)
        b = (x,0)
        c = (x, 600)
        d = (600, x)
        canvas.line (a+b, "blue")
        canvas.line(c+d, "blue")
        
    for y in range (20, 601, 20):
        a = (0, 600-y)
        b = (600-y, 0)
        c = (600, y)
        d = (y,600)
        canvas.line (b+c, "red")
        canvas.line (a+d, "red")
    
    imgRed.show()
    

def calcularDivision17 ():
    contador = 0
    for x in range (1000, 10000):
        if x%17 == 0:
            contador = contador + 1
            
        return contador
    
    
def operacionesPiramide ():
    
    contador = 0
    for x in range (1, 10):
        contador = (contador * 10 + x)
        calculo = (contador*8 + x)
        print ("%d * 8 + %d = 9%d" % (contador, contador, calculo))
        print (" ")
        
        cantidad = 1
        print ("1*1 = 1")
        for x in range (1, 10):
            cantidad = (cantidad * 10+1)
            y = (cantidad * cantidad)
            print ("%d + %d = %d" % (cantidad, cantidad, y))
            
            
def menu ():
    print (" 1. Dibujar cuadros y círculos")
    print (" 2. Dibujar parábolas")
    print (" 3. Dibujar espiral")
    print (" 4. Dibujar red")
    print (" 5. Contar divisibles entre 17")
    print (" 6. Imprimir pirámides de números")
    print (" 0. Salir")
    
opcion = int (input ("Teclea tu opción: "))
return opcion

def main():
    opcion = menu()
    while opcion !=0:
        if ocpion == 1:
            dibujarCuadrosCirculos()
        elif opcion == 2:
            dibujarEstrella()
        elif opcion == 3:
            dibujarEspiral()
        elif opcion == 4:
            dibujarRed()
        elif opcion == 5:
            contador = calcularDivision17()
        elif opcion == 6:
            operacionesPiramide()
        else:
            print ("Error")
        opcion = menu()
    print ("Terminado")
    
main()
        
        
        
            
        