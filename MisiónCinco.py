#Autor: Brandon Julien Celaya Torres
#Descripción: Menú con while

from PIL import Image, ImageDraw
from random import randint
import turtle

def menu ():
    print ("""
           1. Dibujar cuadros y círculos
           2. Dibujar parábolas
           3. Dibujar espiral
           4. Dibujar red
           5. Contar divisibles entre 17
           6. Imprimir pirámides de números
           0. Salir 
           """)
    opcion = int(input("Teclea tu opción: "))
    return opcion


def dibujarCuadrosCirculos(imagen):
    for r in range (0, 301, 10):
        imagen.rectangle ((r, r) + (599-r, 599-r), "white", "black")
        imagen.ellipse ((r, r) + (599-r, 599-r), "white", "black")
    
def dibujarEstrella (imagen):
    for y in range (0, 301, 10):   # [0, 10, 20, ..., 300]
        a = (300, y)
        b = (300+y, 300)
        #genera color aleatorio
        rojo = randint(0,255)
        verde = randint (0,255)
        azul = randint (0,255)
        imagen.line (a + b, (rojo, verde, azul))
    for x in range (0, 301, 10):   
        a = (x, 300)
        b = (300, 300+x)
        rojo = randint(0,255)
        verde = randint (0,255)
        azul = randint (0,255)
        imagen.line (a + b, (rojo, verde, azul))
    for y in range (0, 301, 10):   
        a = (300, y)
        b = (300-y, 300)
        rojo = randint(0,255)
        verde = randint (0,255)
        azul = randint (0,255)
        imagen.line (a+b, (rojo, verde, azul))
    for x in range (0, 301, 10):   
        a = (300+x, 300)
        b = (300, 600-x)
        rojo = randint(0,255)
        verde = randint (0,255)
        azul = randint (0,255)
        imagen.line (a + b, (rojo, verde, azul))

def espiral ():
    t = turtle.Turtle()
    side = 10
    for i in range(100):
        t.forward(side)
        t.right(90) 
        side = side - 5
        
        

def dibujarRed (canvas):
    
    for i in range (0,601, 20):
        canvas.line ((0, i) + (i, 0), "blue")
        canvas.line ((600,i) + (i, 600), "blue")
        
        canvas.line ((i, 600) + (0, 600-i), "red")
        canvas.line ((600-i, 0) + (600, i), "red")
        
        
def calculoNumeros ():
    a = 0 
    for i in range (1000, 10000, 1):
       if i%17 == 0:
            print ("Número divisible entre 17: ", i)
            a = a+1

    print ("La cántidad de números de 4 dígitos divisbles entre 17 es: %d" % (a))


def piramideUno ():
    
    n=1
    S=1
    R=0
    for i in range(1,10):
            
            R=S*8+n
        
            print("%i*8+%i=%i"%(S,n,R))
            
            n=n+1
            S=10*S+n
            
            R=0
            
            
def piramideDos ():
    
    S=1
    R=0
    for i in range(1,10):
            
            R=S*S
        
            print("%i*%i=%i"%(S,S,R))
          
            S=10*S+1
            
            R=0


def main ():
    
    opcion = menu()      #imprimir opciones (1-2-3-4---)
    
    while opcion != 0:
        if opcion == 1:
            
            imgCuadros = Image.new ("RGB", (600, 600), "white")
            canvas = ImageDraw.Draw(imgCuadros)
            dibujarCuadrosCirculos(canvas)
            imgCuadros.show()
            
        elif opcion == 2:
            imgEstrella = Image.new ("RGB", (600, 600), "white")
            canvas = ImageDraw.Draw(imgEstrella)
            dibujarEstrella(canvas)
            imgEstrella.show()
            
        elif opcion == 3:
            espiral()
        
        elif opcion == 4:
            imgRed = Image.new ("RGB", (600, 600), "white")
            canvas = ImageDraw.Draw(imgRed)
            dibujarRed(canvas)
            imgRed.show()
            
            
        elif opcion == 5:
            calculoNumeros()
            
            
            
            
        elif opcion == 6:
            
            piramideUno()
            piramideDos()
            
            
            
            
            
            
        else:
            print ("Opción incorrecta, debes teclear 1 ó 2")
            
        opcion = menu()
        
    print ("Termina")
    
    
    
main()