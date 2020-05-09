#Autor: Anayansi Alexia Tafoya Soto, a01746781
# Dibujo de figuras geométricas


from PIL import Image, ImageDraw
from random import randint
import turtle

#imagen es ImageDraw (canvas)
def dibujarEstrella (imagen):
    for y in range (0, 301, 10):   #[0, 10, 20, ..., 300]
        a = (300, y)
        b = (300 + y, 300)
        
        #genera color aleatorio
        rojo = randint (0,255)
        verde = randint (0,255)
        azul = randint (0, 255)
        
        imagen.line ( a+b, (rojo, verde, azul))
        
      
        a = (300, y)
        b = (300-y, 300)
        
        #genera color aleatorio
        rojo = randint (0,255)
        verde = randint (0,255)
        azul = randint (0, 255)
        
        imagen.line ( a+b, (rojo, verde, azul))
        
        
        a = (300, 600-y)
        b = (300+y, 300)
        
        #genera color aleatorio
        rojo = randint (0,255)
        verde = randint (0,255)
        azul = randint (0, 255)
        
        imagen.line ( a+b, (rojo, verde, azul))
        
        a = (300, 600-y)
        b = (300-y, 300)
        
        #genera color aleatorio
        rojo = randint (0,255)
        verde = randint (0,255)
        azul = randint (0, 255)
        
        imagen.line ( a+b, (rojo, verde, azul))


def dibujarCuadrosCirculos(canvas):
    a = 600
    for x in range (0,301,10):
        pa = (x,x)
        pb = (x+a, x+a)
        canvas.line (pa+(x+a,x) + pb + (x, x+a) + (x,x),"black")
        canvas.ellipse (pa+pb, "white", "black")
        a = a-20


def dibujarEspiral():
     for x in range (0, 600, 10):
        turtle.forward (x)
        turtle.left (90)
        turtle.forward (x+5)
        turtle.left (90)
        turtle.forward (x+5)
        turtle.left (90)
        turtle.forward (x+10)
        turtle.left (90)


def dibujarRed(imagen):
    for x in range (0, 600, 20):
        a = (20+x, 0)
        b = (0, 20+x)
        imagen.line (a+b, "blue")
       
    for x in range (0, 600, 20):  
        a = (x-20, 600)
        b = (600, x-20)
        imagen.line (a+b, "blue")
        
    for x in range (0, 600, 20):
        a = (0+x, 0)
        b = (600, 600-x)
        imagen.line (a+b, "red")
        
    for x in range (0, 600, 20):
        a = (0+x, 600)
        b = (0, 600-x)
        imagen.line (a+b, "red")
        
        
def calcularDivisibles():
    c =0
    for x in range (1000, 10000):
        if  x %17 == 0:
            c = c+1
                
    return c


def calcularOperaciones ():
    b = 0
    for x in range (1, 10):
        b  = b * 10 + x   # 0 * 10 +1
        a = b * 8 + x     # 1 * 8 + 1
        print ( b, " * 8 + ", x, "=", a)
        
        
def calcularPiramide ():
    x = 0   # numeros 1
    y = 0   # contador
    for y in range (1, 10):
        y = y +1
        if y<11:
            x = x * 10 +1
            z = x * x
        print (x, "*", x, "=", z)      
        
        
def menu():
    print  ('''
        Misión 05, Seleccione una opción: 
        1. Dibujar cuadros y circulos
        2. Dibujo parábolas
        3. Dibujo espiral
        4. Dibujo red
        5. Contar divisibles entre 17
        6. Imprimir pirámides de números
        0. Salir
        ¿Qué desea hacer?
    ''')
    opcion = int (input ("Teclea el número de la imagen que deseas ver: "))
    return opcion


def main():
    img = Image.new ("RGB", (600,600), "white")
    canvas = ImageDraw.Draw (img)
    
    opcion = menu()      # 1 -2 - opcion:
    while opcion !=0 :
        if opcion==1:
            imgCuadrosCirculos = Image.new ("RGB", (600,600), "white")
            canvas = ImageDraw.Draw (imgCuadrosCirculos)
            dibujarCuadrosCirculos (canvas)
            imgCuadrosCirculos.show()   
            
            
        elif opcion==2:
            imgEstrella = Image.new ("RGB", (600,600), "white")
            canvas = ImageDraw.Draw (imgEstrella)
            dibujarEstrella (canvas)
            imgEstrella.show()
    
        elif opcion==3:
            dibujarEspiral()
            
        elif opcion ==4:
            imgRed =Image.new ("RGB", (600,600), "white")
            imagen = ImageDraw.Draw (imgRed)
            dibujarRed (imagen)
            imgRed.show()
            
        elif opcion ==5:
            numeros = calcularDivisibles()
            print ("La cantidad de números con 4 dígitos divisibles entre 17 son: ",numeros)
            
        elif opcion ==6:
            calcularOperaciones()
            print ("""    """)
            calcularPiramide()
            
        else:
            print ("Opción incorrecta, debes teclear [1, 2]")
            
        opcion = menu()
        
    print ("Termina")
          
main()