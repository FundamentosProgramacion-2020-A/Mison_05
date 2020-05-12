# Autor: Patricio León
# Misión 5. El cíclo for y while (menu)

from PIL import Image, ImageDraw
from random import randint
import turtle     #Librería para dibujar tortugas


# a)
def dibujarCuadrosCirculos(imagen):
    imagen = Image.new("RGB",(600,600),"white")
    canvas = ImageDraw.Draw(imagen)
    a = 600
    for x in range(0,301,10):
        pa = (x,x)
        pb = (x+a, x+a)
    
        canvas.line(pa+(x+a,x)+pb+(x,x+a)+(x,x), "black")
        canvas.ellipse(pa+pb, "white", "black")
        a = a-20
    
    imagen.show()


# b)
def dibujarEstrella(imagen):
    imagen = Image.new("RGB",(600,600),"white")
    canvas = ImageDraw.Draw(imagen)
    for y in range(0, 301, 10):    #  [0, 10, 20,... 300]
        a = (300, y)
        b = (300+y, 300)
        # genera color aleatorio
        rojo = randint(0, 255)
        verde = randint(0, 255)
        azul = randint(0, 255)
        canvas.line(a + b, (rojo, verde, azul))
        
    for x in range(0, 301, 10):    #  [0, 10, 20,... 300]
        a = (x, 300)
        b = (300, 300+x)
        # genera color aleatorio
        rojo = randint(0, 255)
        verde = randint(0, 255)
        azul = randint(0, 255)
        canvas.line(a + b, (rojo, verde, azul))
        
    for y in range(0, 301, 10):    #  [0, 10, 20,... 300]
        a = (300, y)
        b = (300-y, 300)
        # genera color aleatorio
        rojo = randint(0, 255)
        verde = randint(0, 255)
        azul = randint(0, 255)
        canvas.line(a + b, (rojo, verde, azul))
        
    for x in range(300, 601, 10):    #  [0, 10, 20,... 300]
        a = (x, 300)
        b = (300, 900-x)
        # genera color aleatorio
        rojo = randint(0, 255)
        verde = randint(0, 255)
        azul = randint(0, 255)
        canvas.line(a + b, (rojo, verde, azul))
        
    imagen.show()
    
  
# c)  
def dibujarEspiral():
    x = turtle.xcor()
    y = turtle.ycor()
    
    turtle.penup()
    turtle.goto(x+0,y+0)
    turtle.pendown()
    
    for i in range(0,601,10):
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(10)
        turtle.forward(i)
        turtle.speed(10)
        

# d)
def dibujarReja (imagen):
    imagen = Image.new("RGB",(600,600),"white")
    canvas = ImageDraw.Draw(imagen)
    for y in range(-600, 901, 20):
        canvas.line( [(y,600), (600,y)], "blue")
    
    for x in range(0, 1201,20):
        canvas.line( [(x-500,0), (x,600)], "red")
    
    imagen.show()
        

#  2)
def divisibles():
    numero = 0
    for n in range (1000,10000):
        if  n%17 == 0:
            numero = 1+numero
    print("La cantidad de números divisibles es: ", numero)
    
    
# 3)    
def piramide():
    a = 0
    for i in range (1,10):
        a=a*10+i
        x=a*8+i
        print(a,"* 8 +",i,"=",x)
        
        
    a = 0
    x = 0
    for i in range (1,10):
        a=a*10+1
        x=x*10+1
        y=a*x
        print(a,"*", x, "=",y)


# 4)
def menu():
    print("Misión 5. Seleccipne qué quiere hacer.")
    print('''
        1. Dibujar cuadros y círculos
        2. Dibujar parábolas
        3. Dibujar espiral
        4. Dibujar red
        5. Contar divisibles entre 17
        6. Imprimir pirámides de números
        0. Salir
        ¿Qué desea hacer?
    ''')
    opcion = int(input("Teclea tu opción: "))
    return opcion
    
    
# e)
def main():
    
    imagen = Image.new("RGB",(600,600),"white")
    canvas = ImageDraw.Draw(imagen)
    
    opcion = menu()     # 1 - 2 -  opcion:
    while opcion != 0:
        if opcion == 1:
            dibujarCuadrosCirculos(imagen)
        elif opcion == 2:
            dibujarEstrella(imagen)
        elif opcion == 3:
            dibujarEspiral()
        elif opcion == 4:
            dibujarReja (imagen)
        elif opcion == 5:
            divisibles()
        elif opcion == 6:
            piramide()
        else:
            print("Opción incorrecta, debes teclear [1, 2, 3, 4, 5, 6]")
        
        opcion = menu()
        
    print("Termina")


main()