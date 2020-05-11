# Mariana Ponce Gonzàlez
# Mision 5

from PIL import Image, ImageDraw
from random import randint
import turtle

#1
#a)
#imag es ImageDraw (canvas)
def cuadrocirculo(canvas):
    a = 600
    for x in range(0, 301, 10):
        pa = (x,x)
        pb = (x+a, x+a)
        canvas.line(pa+(x+a,x)+pb+(x,x+a)+(x,x),"black")
        canvas.ellipse(pa+pb, "white", "black")
        a = a-20

#b)
#imag es ImageDraw (canvas)
def dibujarestrella(imagen):
    #Lado 1
    for y in range(0, 301, 10):  #de 0 a 300
        a = (300, y)
        b = (300+y,300)
        #generar colores aleatorias
        rojo = randint(0,255)
        verde = randint(0,255)
        azul = randint(0,255)
        imagen.line(a + b, (rojo, verde, azul))
        
    #Lado 2
    for y1 in range(0, 301, 10):  #de 0 a 300
        a = (300, y1)
        b = (300-y1,300)
        #generar colores aleatorias
        rojo = randint(0,255)
        verde = randint(0,255)
        azul = randint(0,255)
        imagen.line(a + b, (rojo, verde, azul))
        
    #Lado 3
    for y2 in range(300, 601, 10):  
        a = (300, y2)
        b = (900-y2,300)
        #generar colores aleatorias
        rojo = randint(0,255)
        verde = randint(0,255)
        azul = randint(0,255)
        imagen.line(a + b, (rojo, verde, azul))
        
    #Lado 4
    for y3 in range(300, 601, 10):  
        a = (300, y3)
        b = (y3-300,300)
        #generar colores aleatorias
        rojo = randint(0,255)
        verde = randint(0,255)
        azul = randint(0,255)
        imagen.line(a + b, (rojo, verde, azul))

#c)
def dibujarespiral():
    #Rango
    for i in range(0, 600, 10):
    #Giros 
        turtle.forward(i)
        turtle.right(90)
        
    turtle.done()

#d)
def debujRed(imagen):
    #rango Rojo
    for y in range(10, 1201, 20): 
        a = (0, y)
        b = (y, 0)
        imagen.line(a + b, ("red"))
     
    #rango azul 
    for x in range(10, 1201, 20):
        a = (x-620, 0)
        b = (12000, x+12000)
        imagen.line(a + b, ("blue"))

#2
def divisible17():
    divisibles = 0
    #Rango de 4 digitos
    for t in range(1000,10000):
        if t % 17 == 0:
            divisibles += 1
        
    return divisibles

#3
def ejericio1():
    a = 0
    #Rango de las operaciones
    for i in range(0,9):
        #Piramide de numeros
        c = i+1
        a = (a*10+c)
        b = 8
        r = a * 8 + c
        print(a, "*", b, "+", c, "=", r)
        
def ejericio2():
    a = 0
    b = 0
    #Rango de las operaciones
    for i in range(0,9):
        #Piramide de numeros
        a = (a*10+1)
        b = (b*10+1)
        r = (a*b)
        print(a, "*", b, "=", r)      

def menu():
    #Opciones
    print('''
         Misiòn 5. Sleccione què quiere hacer,
         1. Dibujar cuadros y cìrculos
         2. Dicujar paràbolar
         3. Dibujar espiral
         4. Dibujar red
         5. Contar divisibles entre 17
         6. Imprimir piràmides de nùmeros
         0. Salir
         ¿Què desea hacer?
    ''')
    opcion = int(input("Teclea tu opciòn: "))
    return opcion

def main():
    
    opcion = menu()
    #Actividad a realizar dependiendo de las opciones 
    while opcion != 0:
        if opcion ==1:
            img = Image.new("RGB", (600, 600), "white")
            canvas = ImageDraw.Draw(img)
            cuadrocirculo(canvas)
            img.show()
        elif opcion == 2:
            img = Image.new("RGB", (600, 600), "white")
            canvas = ImageDraw.Draw(img)
            dibujarestrella(canvas)
            img.show()
        elif opcion == 3:
            turtle.shape("turtle")
            dibujarespiral()
        elif opcion == 4:
            img = Image.new("RGB", (600, 600), "white")
            canvas = ImageDraw.Draw(img)
            debujRed(canvas)
            img.show()
        elif opcion == 5:
            m = divisible17()
            print("La cantidad de divisibles de 17 son %d " % (m))
        elif opcion == 6:
            ejericio1()
            print("\n")
            ejericio2()
        else:
            print("Opciòn incorrecta, debe teclear [1,6]")
           
        opcion = menu()
           
    print("Salir")
main()