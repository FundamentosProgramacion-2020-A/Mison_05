# Autor: Fernando Pérez González, A01376508
# Misión 5, dibujar, calcular un número divisible entre 17,
# hacer pirámides de números y realizar menú 


from PIL import Image, ImageDraw
from random import randint


#1
def dibujarCuadrosCirculos(canvas):    #Imagen c, dibuja cuadros y círculos
    
    img = Image.new("RGB", (600,600), "white")
    canvas = ImageDraw.Draw(img)
    
    a = 600
    for x in range(0,301,10):
        b = (x,x)
        c = (x+a, x+a)
        canvas.line(b+(x+a,x)+c+(x,x+a)+(x,x), "black")
        canvas.ellipse(b+c, "white", "black")
        a = a-20
        
    img.show()
        

def dibujarEstrella(canvas):    #Imagen b, dibuja una estrella con colores aleatorios

    img = Image.new("RGB", (600,600), "white")
    canvas = ImageDraw.Draw(img)
    
    for y in range (0,301,10):  #va a subir de 10 en 10 del 0-300
        a = (300, y)
        b = (300 + y, 300)
        c = (300 -y,300)
        d = (300, 600 - y)
        #lo de abajo genera un color aleatorio
        rojo = randint(0,255)
        verde = randint(0,255)
        azul = randint(0,255)
        canvas.line(a + b, (rojo, verde, azul)) #cuadrante arriba derecha
        canvas.line(a + c, (rojo, verde, azul)) #cuadrante arriba izquierda
        canvas.line(b + d, (rojo, verde, azul)) #cuadrante abajo derecha
        canvas.line(d + c, (rojo, verde, azul)) #cuadrante abajo izquierda
        
    img.show()

        
def dibujarEspiral(canvas): #Imagen c, dibuja la espiral en negro
    
    img = Image.new("RGB", (600,600), "white")
    canvas = ImageDraw.Draw(img)
    
    for x in range (10, 301, 10): #va a subir de 10 en 10 del 10-300
        a = (600-x, 600-x)
        b = (x,600-x)
        c = (x,x)
        d = (600-x-10,x)
        e = (600-10-x, 600-10-x)
        canvas.line(a + b, "black")
        canvas.line(c + d, "black")
        canvas.line(b + c, "black")
        canvas.line(d + e, "black")
        
    img.show()

        
def dibujarRed(canvas): #Imagen d, dibuja una red azul y roja
    
    img = Image.new("RGB", (600,600), "white")
    canvas = ImageDraw.Draw(img)
    
    for r in range (20, 601, 20):  #va a subir de 20 en 20 del 20-600
        a = (r, 0)
        b = (0, r)
        c = (600, 600-r)
        d = (600-r,600)
        e = (600-r, 0)
        f = (600, r)
        g = (0, 600-r)
        h = (r, 600)
        canvas.line(a + b, "blue")
        canvas.line(c + d, "blue")
        canvas.line(e + f, "red")
        canvas.line(g + h, "red")

    img.show()


def menu(): #le permite al usuario imprimir cualquiera de las imagenes anteriores, o los ejercicios posteriores
    print('''
        Misión 5. Seleccione que quiere hacer.
        1. Dibujar cuadros y círculos
        2. Dibujar parábolas
        3. Dibujar espiral
        4. Dibujar red
        5. Contar divisibles entre 17
        6. Imprimir pirámides de números
        0. Salir
        ¿Qué desea hacer?
    ''')
    opcion = int(input("Teclea únicamente el número tu opción: "))
    return opcion


#2

def calcularRegresar(): #calcula el total de números de 4 dígitos divisibles entre 17
    
    n = 0
    divisibles = 0
    for n in range (1000, 10000):
        if n%17 == 0:
            divisibles += 1
        
    return divisibles


def calcularImprimir(): #calcula e imprime 2 piramides de números
    
    a = 0
    for n in range (1, 10): #crea la primer pirámide
        a = a * 10 + n
        x = a * 8 + n
        print("%d * 8 + %d = %d" % (a,n,x))
    print ("\n")

    y = 0
    for d in range (9): #crea la segunda pirámide
        y = y * 10 + 1
        y2 = y        
        t = y * y2
        print("%d * %d = %d" % (y, y2, t))
    

def main():

    canvas = ImageDraw.Draw

    opcion = menu()
    while opcion != 0:
        if opcion == 1:
            dibujarCuadrosCirculos(canvas)
        elif opcion == 2:
            dibujarEstrella(canvas)
        elif opcion == 3:
            dibujarEspiral(canvas)
        elif opcion == 4:
            dibujarRed(canvas)
        elif opcion == 5:
            a = calcularRegresar()
            print("Encontre %d divisores" % a)
        elif opcion == 6:
            calcularImprimir()
            print("Aquí están las dos pirámides de números")

        else:
            print("Opción incorrecta, debes teclear un número entre 1-6")
            
        opcion = menu()
    print("\n")    
    print("Termina")
    
    
main()
        
