#Autor: Ana Fernanda Martinez Garcia
# Programa donde a partir de un menu se ejecutan las opciones

#Importar de PIL
import turtle
from PIL import Image, ImageDraw
from random import randint

#Defines la función de los cuadros y los círculos
def dibujarCuadradoCirc():
    img=Image.new("RGB", (600,600), "white")
    canvas =ImageDraw.Draw(img)
    
    a = 600
    for x in range (0,301,10):
        pa = (x,x)
        pb = (x+a, x+a)
        canvas.line (pa+(x+a,x) + pb +(x,x+a)+(x,x), "black")
        canvas.ellipse(pa+pb, "white", "black")
        a=a-20
        
    img.show()
    
#Defines la función de la estrella
def dibujarEstrella ():
    
    imgEs= Image.new("RGB", (600,600), "white")
    canvas = ImageDraw.Draw(imgEs)
    
    rojo= randint (0,255)
    verde= randint (0,255)
    azul= randint (0,255)

    for y in range(0, 301, 10):  
        a = (300, y)
        b = (300 + y, 300)
        canvas.line (a+b, (rojo,verde,azul))
        
    for y in range(0, 301, 10):  
        c = (300, y)
        d = (300 - y, 300)
        canvas.line (c+d, (rojo,verde,azul))
        
    for x in range(0, 301, 10):  
        e = (x, 300)
        f = (300, 300 + x)
        canvas.line (e+f, (rojo,verde,azul))
        
    for x in range(300, 601, 10):  
        g= (x,300)
        h= (300, 900 -x )
        canvas.line (g+h, (rojo,verde,azul))
        

    imgEs.show()
    
     
#Defines la función del espiral    

def dibujarEspiral():
    turtle.speed (5)
    turtle.color("black")
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.right(90)
    
    for x in range(0,701,10):
        turtle.forward(x)
        turtle.left(90)

        
#Defines la función dibujar Red

def dibujarRed():

    img= Image.new("RGB", (600,600), "white")
    canvas = ImageDraw.Draw(img)
    for x in range(20,602,20):
        a=(0,x)
        b=(x,0)
        c=(x,600)
        d=(600,x)
        canvas.line(a+b, "blue")
        canvas.line(c+d, "blue")
    for y in range(20,602,20):
        e=(0,600-y)
        f=(600-y,0)
        g=(600,y)
        h=(y,600)
        canvas.line(f+g,"red")
        canvas.line(e+h,"red")
    img.show()
    
# Funcion numeros divisibles entre 17
def numero17divisible():
    x=0
    for i in range (1000, 10000, 1):
        if i%17 == 0:
            x+= 1
            #print(i)
    print(x, "números son divisibles entre 17")

#Funcion donde se crea la piramide de numeros
def CrearPiramide():
    a = 1
    b = 1
    print(""" Pirámide 1: """)
    for i in range(9):
            print (a, "* 8 +", b, "=", (a * 8 + b))
            b = b + 1
            a = a * 10 + b
    x = 1
    print(""" Pirámide 2: """)
    for i in range(9):
        print(x, "*", x, "=", x*x)
        x = x * 10 +1

#Main Funcion

def main():
    imagen = Image.new ("RGB", (600, 600), "white")
    canvas = ImageDraw.Draw(imagen)

    a= 1
    while (a > 0):

        a = int(input("""
        1. dibujar cuadros y círculos
        2. Dibujar Estrella
        3. Dibujar Espiral
        4. Dibujar Red
        5. Contar divisibles entre 17
        6. Imprimir pirámides de números
        0. Salir
        Teclee el número deseado: """))
        if a == 1:
            dibujarCuadradoCirc()
        elif a == 2:
            dibujarEstrella()
        elif a == 3:
            dibujarEspiral()
        elif a == 4:
            dibujarRed()
        elif a == 5:
            numero17divisible()
        elif a == 6:
            CrearPiramide()
        elif (a>6):
            print ("Número no válido, vuelva a intentar.")
            
    print ("Programa termidado")

main()