#Valeria Huerta Pedregal
#Misión 5, ciclo while y ciclo for

from PIL import Image, ImageDraw
import turtle
from random import randint

def dibujarCuadrosCirculos(imagen): #Dibuja cuadros y circulos
    a = 600
    for x in range (0, 301, 10):
        pa = (x,x)
        pb = (x+a, x+a)
        imagen.line(pa+(x+a,x)+pb+(x,x+a)+(x,x),"black")
        imagen.ellipse(pa+pb, "white","black") #el segundo parametro es el outline
        """canvas.rectangle(pa+pb, "White","black")"""
        a=a-20
    
def dibujarEstrella(imagen): #Dibuja estrella
    for y in range (0,301,10): 
        a = (300,y) 
        b = (300+y,300)
        rojo = randint (0,255)
        verde = randint (0,255)
        azul = randint (0,255)
        imagen.line(a+b, (rojo, verde, azul))
        c = (300,y) 
        d = (300-y,300)
        imagen.line(c+d, (rojo, verde, azul))
        
    for x in range (0,301,10):
        a = (x,300) 
        b = (300,300+x)
        rojo = randint (0,255)
        verde = randint (0,255)
        azul = randint (0,255)
        imagen.line(a+b, (rojo, verde, azul))
        
    for x in range (300,601,10):
        a = (x,300) 
        b = (300,900-x)
        rojo = randint (0,255)
        verde = randint (0,255)
        azul = randint (0,255)
        imagen.line(a+b, (rojo, verde, azul))
        
def dibujarEspiral(turtle): #Dibuja espiral con tortuga
    for i in range (0,601,10):
         turtle.forward(10)
         turtle.left(90)
         turtle.forward(10)
         turtle.forward(i)
        
def dibujarRed(imagen): #Dibuja red
    for x in range (-600,601,20):
        puntoAI = (x,0)
        puntoAD = (x+600,600)
        imagen.line (puntoAI+puntoAD, "red")
    
    for y in range (0,1201,20):
        puntoAI = (0,y)
        puntoAD = (600,y-600)
        imagen.line (puntoAI+puntoAD, "blue")
        
def calcularDivisibles(): #Calcula números de cuatro digitos divisibles entre 17
    a=0
    for i in range(1000,10000):
        if i % 17 == 0:
            a+=1
    return a
    
def calcularPiramide(): #Calcula dos piramides de ecuaciones
    a=0
    d=0
    for i in range (1,10):
        a=a*10+i
        c=a*8+i
        print("%d * 8 + %d = %d" % (a,i,c))

    print("")    
    for j in range (1,10):
        d=d*10+1
        b=d*d
        print("%d * %d = %d" % (d,d,b))


def main(): #Corre programa principal
    print('''Misión 5. Seleccione qué quiere hacer.
             1. Dibujar cuadros y círculos
             2. Dibujar parábolas
             3. Dibujar espiral
             4. Dibujar red
             5. Contar divisibles entre 17
             6. Imprimir pirámides de números
             0. Salir''')
    opcion = int(input("¿Qué desea hacer? "))
    
    while opcion > 0:
        if opcion == 1:
            imgCuadrosCirculos = Image.new ("RGB", (600,600), "white")
            canvas = ImageDraw.Draw (imgCuadrosCirculos)
            dibujarCuadrosCirculos(canvas)
            imgCuadrosCirculos.show()
            opcion = int(input("¿Qué más desea hacer? "))
            
        elif opcion == 2:
            imgEstrella = Image.new("RGB", (600,600), "white")
            canvas = ImageDraw.Draw(imgEstrella)
            dibujarEstrella(canvas)
            imgEstrella.show()
            opcion = int(input("¿Qué más desea hacer? "))
        
        elif opcion == 3:
            dibujarEspiral(turtle)
            opcion = int(input("¿Qué más desea hacer? "))
            
        elif opcion == 4:
            imgRed = Image.new("RGB", (600,600), "white")
            canvas = ImageDraw.Draw(imgRed)
            dibujarRed(canvas)
            imgRed.show()
            opcion = int(input("¿Qué más desea hacer? "))
            
        elif opcion == 5:
            a = calcularDivisibles()
            print(a, "números de cuatro digitos son divisibles entre 17")
            opcion = int(input("¿Qué más desea hacer? "))
            
        elif opcion == 6:
            calcularPiramide()
            opcion = int(input("¿Qué más desea hacer? "))
        
        else:
            print("Error, por favor selecciona una opción del 0-6")
            opcion = int(input("¿Qué desea hacer? "))
    
    print("Haz salido del menú.")
               
main()
