# Autor: Sharone Márquez, a01746940
# Escribir un programa con cuatro funciones para realizar distintas imágenes

import turtle
from PIL import Image, ImageDraw
from random import randint

#Función de la primera imagen
def dibujarCuadrosCirculos():
    imagenCC= Image.new("RGB", (600,600), "white")
    canvas= ImageDraw.Draw(imagenCC)
    
    a= 600
    for y in range(0, 301, 10):
        puntoA= (y, y)
        puntoB= (y+a, y+a)
        canvas.ellipse(puntoA + puntoB, ("white"), ("black"))
        canvas.line(puntoA+(y+a, y) + puntoB +(y, y+a) + (y, y), ("black"))
        a= a - 20
        
    imagenCC.show()
    
#Función de la segunda imagen
def dibujarEstrella():
    imagenE= Image.new("RGB", (600,600), "white")
    canvas= ImageDraw.Draw(imagenE)
    
    for y in range(0, 301, 10):
        a= (300, y)
        b= (300+y, 300)
        red= randint(0, 255)
        green= randint(0, 255)
        blue= randint(0, 255)
        canvas.line(a + b, (red, green, blue))
    
    for a in range(0, 301, 10):
        p= (300, a)
        q= (300-a, 300)
        red= randint(0, 255)
        green= randint(0, 255)
        blue= randint(0, 255)
        canvas.line(p + q, (red, green, blue))
        
    for x in range(0, 301, 10):
        a= (x, 300)
        b= (300, x+300)
        red= randint(0, 255)
        green= randint(0, 255)
        blue= randint(0, 255)
        canvas.line(a + b, (red, green, blue))
        
    for b in range(0, 301, 10):
        v= (300+b, 300)
        u= (300, 600-b)
        red= randint(0, 255)
        green= randint(0, 255)
        blue= randint(0, 255)
        canvas.line(v + u, (red, green, blue))
    
    imagenE.show()
    
#Función de la tercera imagen
def dibujarEspiral(turtle):
    turtle.shape("turtle")
    for x in range(0, 601, 10):
        turtle.forward(10)
        turtle.right(270)
        turtle.forward(10)
        turtle.forward(x)
        
#Función de la cuarta imagen
def dibujarRed():
    imagenR= Image.new("RGB", (600,600), "white")
    canvas= ImageDraw.Draw(imagenR)
    
    for y in range(0, 601, 20):
        canvas.line( [(0, y), (600, y+600)], "red")

    for x in range(0, 601, 20):
        canvas.line( [(x+600, 600), (x+0, 0)], "red")
    
    for a in range(0, 601, 20):
        canvas.line( [(a, 0), (a-600, 600)], "blue")

    for b in range(0, 601, 20):
        canvas.line( [(a-600, b+600), (a+0, b-0)], "blue")
        
    imagenR.show()
    
#Función de calcular la cantidad de no. divisibles entre 17
def calcularDivision():
    contador= 0
    for numero in range(1000, 10000):
         if numero%17 == 0:
            contador= contador + 1
            
    return contador


#Función de imrprimir operaciones en forma de pirámide
def calcularOperaciones():
    contador= 0
    acumulador= 0
    for factor in range(1,10): 
        contador= contador + 1
        acumulador= ((acumulador*10)+ contador)
        resultado= (acumulador*8) + factor
        
        print("%d x 8 + %d = %d" % (acumulador, factor, resultado))
        
    print(" ")
    
    c= 0
    a1= 0
    a2= 0
    for i in range(1,10): 
        c= c + 1
        a1= ((a1*10) + 1)
        a2= ((a2*10) + 1)
        r= (a1*a2)
        
        print("%d x %d = %d" % (a1, a2, r))

def menu():
    print(" ")
    print('''Misión 5. Seleccione qué quiere hacer.
1. Dibujar cuadros y círculos
2. Dibujar parábolas
3. Dibujar espiral
4. Dibujar red
5. Contar divisibles entre 17
6. Imprimir pirámides de número
0. Salir''')
    
    opcion= int(input("¿Qué desea hacer?: "))
    print(" ")
    return opcion


#Programa principal
def main():

    opcion= menu()
    while opcion != 0:
        if opcion == 1:
            dibujarCuadrosCirculos()

        elif opcion == 2:
            dibujarEstrella()

        elif opcion == 3:
            dibujarEspiral(turtle)
            
        elif opcion == 4:
            dibujarRed()
            
        elif opcion == 5:
            print("Los números divisibles entre 17 son: %d" % (calcularDivision()))
            
        elif opcion == 6:
            calcularOperaciones()
            
        else:
            print("Opción incorrecta. Teclea un número del 0 al 6")
            
        opcion= menu()
        
    print("El programa ha terminado")
    
    
            
main()