#Kathia Alejandra Cervantes López
#Este programa te da una serie de opciones para reproducir

#Librerias que se necesitan
from PIL import ImageDraw, Image
from random import randint
import turtle


#Función del menú
def menu ():
    print ('''
        1. Dibujar cuadros y círuclos
        2. Dibujar parábolas
        3. Dibujar espiral
        4. Dibujar red
        5. Contar divisibles entre 17
        6. Imprimir pirámides de números
        0. Salir
    ''')
    opcion = int(input("Teclea tu opción: "))
    return opcion


#Función para hacer los círculos y cuadrados
def dibujarCuadrosCirculos ():
    #Delimitar el espacio de dibujo
    img = Image.new("RGB", (600,600), "white")
    canvas = ImageDraw.Draw(img)
    
    #Empieza en a = 600
    a=600
    for x in range (0, 301, 10):
        pa= (x,x)
        pb = (x + a, x + a)
        canvas.line(pa +(x + a,x)+pb+(x,x + a)+(x,x),"black")
        canvas.ellipse(pa + pb, "white", "black")
        #-20 para que llegue a 300
        a = a-20
        
    img.show()
    
    
def dibujarEstrella (imagen):
    
    #Lado a
    for  y in range (0, 301, 10):
        a = (300, y)
        b = (300 + y, 300)
        #Generador de color
        rojo = randint (0,255)
        verde = randint (0,255)
        azul = randint (0,255)
        imagen.line(a + b,(rojo, verde, azul))
        
    #Lado b
    for  y in range (0, 301, 10):
        a = (300, y)
        b = (300 - y, 300)
        #Generador de color
        rojo = randint (0,255)
        verde = randint (0,255)
        azul = randint (0,255)
        imagen.line(a + b,(rojo, verde, azul))
        
    #Lado c
    for x in range (0, 301, 10):
        a = (x, 300)
        b = (300, 300 + x)
        #Generador color aleatorio
        rojo = randint (0,255)
        verde = randint (0,255)
        azul = randint (0,255)
        imagen.line(a + b,(rojo, verde, azul))
        
    #Lado d
    for x in range (300, 601, 10):
        a = (x, 300)
        b = (300, 900 - x)
        #Generador color aleatorio
        rojo = randint (0,255)
        verde = randint (0,255)
        azul = randint (0,255)
        imagen.line(a + b,(rojo, verde, azul))
        

#Función para hacer el espiral
def dibujarEspiral ():
    
    #Delimitar el espacio de dibujo
    img = Image.new("RGB", (600,600), "white")
    canvas = ImageDraw.Draw(img)
    #Rango para definir cada cuando volteará
    for e in range (0,701,10):
        turtle.forward(e)
        turtle.left(90)
        
#Función para delimitar espacio y poner medidas para hacer las líneas
def dibujarRed ():
    #Felimitar espacio de trabajo
    imagen = Image.new("RGB", (600,600), "white")
    
    #Linea roja
    canvas = ImageDraw.Draw(imagen)
    for y in range (-601,601,20):
        canvas.line( [(0,y), (600,y + 600)], "red")
    
    #Linea azul
    for x in range (601, -601, -20):
        canvas.line( [(x + 300,0), (x,600)], "blue")
                     
    imagen.show()


#Función para los números de 4 digitos divisibles entre 17
def dividirNumero ():
    n = 0
    for d in range (1000, 10000):
        if d%17 == 0:
            n = 1 + n
            total = n
    print ("El total de numeros divisibles entre 17 es %2d" % (total))
    
            
#Función para poner los acumuladores y fórmulas para hacer las pirámides
def ponerPiramides ():
    #Pirámide uno
    n = 0
    for n2 in range (1,10):
        n = n * 10 + n2
        b = n * 8 + n2
        
        print ( n, "*", "8", "+", n2, "=", b)
    
    #Separación entre pirámiedes
    print ("\n")
    
    
    #Pirámide dos
    n = 0
    b = 0
    for n3 in range (1,10):
        n = n * 10 + 1
        b = b * 10 + 1
        x = n * b
         
        print (n, "*", b, "=", x)
        

#Función principal
def main ():
    
    opcion = menu () # Menu es una función que se guardará en la variable opcion
    #Ciclo para producir el programa dependiendo lo que el usuario teclee
    while opcion != 0:
        if opcion == 1:
            dibujarCuadrosCirculos()
        elif opcion == 2:
            imgEstrella = Image.new ("RGB", (600,600), "white") #Tamaño del fondo
            canvas = ImageDraw.Draw (imgEstrella)
            dibujarEstrella (canvas)
            imgEstrella.show()
        elif opcion == 3:
            dibujarEspiral ()
        elif opcion == 4:
            dibujarRed ()
        elif opcion == 5:
            dividirNumero ()
        elif opcion == 6:
            ponerPiramides()
        else:
            print ("Opción incorrecta, debes teclear un número entre [0 - 6]")
        opcion = menu ()
        
    print ("Termina")
    
    
main ()