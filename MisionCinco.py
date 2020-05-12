#Roberto Sobrado
#Dibujar con ciclos for con menu para diferentes ocpiones.

from PIL import Image, ImageDraw #importamos libreria pil.
from random import randint #importamos libreria para numeros aleatorios.
import turtle #importamos turtle para dibujar.

def dibujarCuadrosCirculos(): #función para dibujar cuadrados y circulos cambiando el tamaño.
    imagenCuadros = Image.new("RGB", (600,600),"white")
    canvas = ImageDraw.Draw(imagenCuadros)
    
    a = 600
    
    for x in range (0,301,10):
        pa = (x,x)
        pb = (x+a,x+a)
        #canvas.rectangle(pa+pb, "White", "Red")
        canvas.line(pa+(x+a,x)+pb+(x,x+a)+(x,x), "black")
        canvas.ellipse(pa+pb, "White", "black")
        a = a-20
        
    imagenCuadros.show()
    
    
def dibujarEstrella(canvas): #Función para dibujar una estrella con lineas y parábolas.

    #lado superior derecho
    for y in range (0, 301, 10):
        a = (300, y)
        b = (300+y, 300)
        
        rojo = randint (0,255)
        verde = randint (0,255)
        azul = randint (0,255)
        canvas.line(a+b, (rojo, verde, azul))
    
    #lado superior izquierdo
    for y in range (0, 301, 10):
        a = (300, y)
        b = (300-y, 300)
        
        rojo = randint (0,255)
        verde = randint (0,255)
        azul = randint (0,255)
        canvas.line(a+b, (rojo, verde, azul))
        
    #lado inferior derecho
    for x in range (300, 601, 10):
        a = (x, 300)
        b = (300, 900 - x)
        
        rojo = randint (0,255)
        verde = randint (0,255)
        azul = randint (0,255)
        canvas.line(a+b, (rojo, verde, azul))

    #lado inferior izquierdo
    for x in range (0, 301, 10):
        a = (x, 300)
        b = (300, 300 + x)
        
        rojo = randint (0,255)
        verde = randint (0,255)
        azul = randint (0,255)
        canvas.line(a+b, (rojo, verde, azul))
        
        
def dibujarEspiral(): #Función para dibujar una espiral con tortuga.
    
    for i in range (0, 601, 5):
        turtle.forward(i)
        turtle.left(90)
    #turtle.done()
    #turtule.exitonclick()
    #window.bye()
    #Me salía un error al cerrar la ventana y busque en internet pero no di con la respues :(    .
    
    
def dibujarRed(): #Función para dibujar una red con lineas.
    imagenRed = Image.new("RGB", (600,600),"white")
    canvas = ImageDraw.Draw(imagenRed)
    
    for x in range (601, -601, -20):
        canvas.line(((x+500,0),(x,600)), "blue")
        
    for y in range (-601,601, 20):
        canvas.line(((0,y), (600,y+500)), "red")
    
    imagenRed.show()
        
        
def calcularDivisibles(): #Función para contar todos los nueros divisibles entre 17 de 4 dígitos.
    a = 0
    for i in range (1000,10000):
        if i%17 == 0:
            a = a + 1
            total = a
    
    return total
    
    
def calcularPiramide(): #Funcion para imprimir una piramide matemática.
    x = 0
    f = 8
    for a in range (1,10):
        x = x * 10 + a
        y = x * f + a
        
        print ("%d * %d + %d = %d" % (x,f,a,y))
        
    print ("    ")
       
    x = 0
    y = 0
    for a in range (1,10):
        x = x * 10 + 1
        y = y * 10 + 1
        z = x * y
        
        print ("%d * %d = %d" % (x,y,z))
        
    
def minuta():  #Función para mostrar el menú principal de programa.
    
    print('''
        Misión 5, seleccione una opción.
        
        1. Dibujar cuadros y círculos.
        2. Dibujar parábolas.
        3. Dibujar espiral.
        4. Dibujar red.
        5. Contar divisibles entre 17.
        6. Imprimir pirámides de números.
        0. Salir.
        
        ¿Qué desea hacer?
    ''')
    opcion = int(input("Teclea tu opción: "))
    return opcion
    
    
def main(): #Función para el programa principal.

    menu = minuta()
    while menu != 0:
        if menu == 1:
            dibujarCuadrosCirculos()
        elif menu == 2:    
            imagenEstrella = Image.new("RGB", (600,600), "white")
            canvas = ImageDraw.Draw(imagenEstrella)
            dibujarEstrella(canvas)
            imagenEstrella.show()
        elif menu == 3:
            dibujarEspiral()
        elif menu == 4:
            dibujarRed()
        elif menu == 5:
            div = calcularDivisibles()
            print ("El total de números divisibles entre 17, que tengan 4 dígitos es de %d." % div)
        elif menu == 6:
            calcularPiramide()
        else:
            print ("Error, esa opción no existe")
    
        menu = minuta()
        print ("   ")
        
    print ("  ")
    print ("Programa terminado.")
  
    
main () #Programa principal.