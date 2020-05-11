#Autor: Michelle Ojeda Manjarrez
#Dibujar diferentes figuras

#Importas la librería PIL, la tortuga y randint
from PIL import Image, ImageDraw
from random import randint
import turtle


#Defines la función de los cuadros y los círculos
def dibujarCuadrosCirculos (imagen):
    
    imagen = Image.new ("RGB", (600, 600), "white")
    canvas = ImageDraw.Draw(imagen)
    a = 600
    for x in range (0,301,10):
        pa = (x,x)
        pb = (x+a, x+a)
        canvas.line (pa+(x+a,x) + pb +(x, x+a)+(x,x), "black")
        canvas.ellipse(pa+pb, "white", "black")
        a = a-20
        
    imagen.show()
    
#Defines la función de la estrella
def dibujarEstrella (imagen):
    
    imagen = Image.new ("RGB", (600, 600), "white")
    canvas = ImageDraw.Draw(imagen)
    
    for y in range(0, 301, 10):  #[0,10,20...300]
        a = (300, y)
        b = (300 + y, 300)
        #genera color aleatorio
        rojo = randint (0, 255)
        verde = randint (0, 255)
        azul = randint (0, 255)
        canvas.line (a+b, (rojo,verde,azul))
        
    for y in range(0, 301, 10):  #[0,10,20...300]
        a = (300, y)
        b = (300 - y, 300)
        #genera color aleatorio
        rojo = randint (0, 255)
        verde = randint (0, 255)
        azul = randint (0, 255)
        canvas.line (a+b, (rojo,verde,azul))
        
    for x in range(0, 301, 10):  
        a = (x, 300)
        b = (300, 300 + x)
        #genera color aleatorio
        rojo = randint (0, 255)
        verde = randint (0, 255)
        azul = randint (0, 255)
        canvas.line (a+b, (rojo,verde,azul))
        
    for x in range(300, 601, 10):  
        a = (x,300)
        b = (300, 900 -x )
        #genera color aleatorio
        rojo = randint (0, 255)
        verde = randint (0, 255)
        azul = randint (0, 255)
        canvas.line (a+b, (rojo,verde,azul))
        
    imagen.show()
     
     
#Defines la función del espiral     
def dibujarEspiral (imagen):
    
    imagen = Image.new ("RGB", (600, 600), "white")
    canvas = ImageDraw.Draw(imagen)
    
    x = turtle.xcor ()
    y = turtle.ycor ()
    
    turtle.penup()
    turtle.goto(x+0, y+0)
    turtle.pendown()
    
    for i in range (0, 701, 10):
        turtle.forward (10)
        turtle.left(90)
        turtle.forward (10)
        turtle.forward(i)
        
        turtle.speed(10)
        
        
#Defines la función dibujar Red
def dibujarRed (imagen):
    
    imagen = Image.new ("RGB", (600, 600), "white")
    canvas = ImageDraw.Draw(imagen)
    
    for y in range (-600, 901, 20):
        canvas.line ([(y,600), (600,y)], "blue")
        
    for x in range (0, 1201, 20):
        canvas.line ([(x-500, 0), (x,600)], "red")
        
    imagen.show()
        
#Defines la función para imprimir pirámides        
def imprimirPiramides ():
    
    a = 0
    for i in range (1, 10):
        
        a = a * 10 + i
        x = a * 8 + i
        
        print (a, "*", "8", "+", i, "=", x)
    print ("------------\n")
         
    a = 0
    b = 0
    for i in range (1, 10):
        
        a = a *10 + 1
        b = b * 10 +1
        x = a * b
        
        print (a, "*", b,"=", x)
        
        
#Defines la función  de calcular los números divisibles entre 17
def calcularDivisibles ():
    x = 0
    
    for i in range (1000,10000):
        numero = i % 17
       
        if numero == 0:
            x = x + 1
        
    print (x, "números se pueden dividir entre 17")
    
        
#Defines la función para hacer el menú       
def menu ():
    print ('''
        Misión 5. Seleccione qué quiere hacer.
        1. Dibujar cuadros y círculos
        2. Dibujar parábolas
        3. Dibujar espiral
        4. Dibujar red
        5. Contar divisibles entre 17
        6. Imprimir pirámides de números
        0. Salir
        ''')
    
    opcion = int (input ("¿Qué desea hacer?: "))
    return opcion

        
def main ():
    
    imagen = Image.new ("RGB", (600, 600), "white")
    canvas = ImageDraw.Draw(imagen)
    
    
    opcion = menu ()      
    
    while opcion != 0:
        if opcion ==1:
            dibujarCuadrosCirculos (imagen)
        elif opcion ==2:
            dibujarEstrella (imagen)
        elif opcion ==3:
            dibujarEspiral(imagen)
        elif opcion == 4:
            dibujarRed (imagen)
        elif opcion ==5:
            calcularDivisibles ()
        elif opcion == 6:
            imprimirPiramides ()
        else:
            print ("Opcion incorrecta, debes teclear [1,2,3,4]")
            
        opcion = menu ()
    
    print ("Termina")
    
    
    
main ()