# Autor: Daniel Rojas, A01376572
# Dibujar una estrella 

from PIL import Image, ImageDraw
from random import randint
import turtle


def menu():  #Imprime las opciones que el usuario puede escoger
    print('''
Misión 5. Estas son las opciones:

1. Dibujar cuadros con círculos
2. Dibujar estrella
3. Dibujar espiral
4. Dibujar red
5. Calcular cuántos números de 4 dígitos son divisibles entre 17
6. Realizar una serie de operaciones curiosas
0. SALIR
''')
    opcion = int(input("Teclea el número de opción que quieres realizar: "))
    return opcion


def dibujarCuadrosCirculos(imagen):  #Dibuja cuadros y círculos
    a = 600
    for x in range(0,301,10):
        imagen.line((x,x)+(x+a,x)+(x+a,x+a)+(x,x+a)+(x,x),"black")
        imagen.ellipse((x,x)+(x+a,x+a),"white","black")
        a -= 20


def dibujarEstrella(imagen):  #Dibuja una estrella
    y1=0
    y2=0
    y3=0
    y4=0
    for i in range(30):
        a=(300,y1)
        b=(y1+300,300)
        rojo=randint(0,255)
        verde=randint(0,255)
        azul=randint(0,255)
        imagen.line(a+b,(rojo,verde,azul))
        y1=y1+10
    for i in range(30):
        a=(300,300+y2)
        b=(600-y2,300)
        rojo=randint(0,255)
        verde=randint(0,255)
        azul=randint(0,255)
        imagen.line(a+b,(rojo,verde,azul))
        y2=y2+10
    for i in range(30):
        a=(300-y3,300)
        b=(300,600-y3)
        rojo=randint(0,255)
        verde=randint(0,255)
        azul=randint(0,255)
        imagen.line(a+b,(rojo,verde,azul))
        y3=y3+10
    for i in range(30):
        a=(300,0+y4)
        b=(300-y4,300)
        rojo=randint(0,255)
        verde=randint(0,255)
        azul=randint(0,255)
        imagen.line(a+b,(rojo,verde,azul))
        y4=y4+10
    
    
def dibujarEspiral():   #Dibuja una espiral
    for a in range(5,606,5):
        turtle.forward(a)
        turtle.left(90)
    turtle.done()
    
    
def dibujarRed(imagen):  #Dibuja una red
    b = 20
    for a in range(580,-1,-20):
        imagen.line((0,a)+(b,600),"red")
        imagen.line((b,0)+(600,a),"red")
        imagen.line((0,b)+(b,0),"blue")
        imagen.line((a,600)+(600,a),"blue")
        b+=20
        
        
def calcularDivisibles():  #Calcula cuántos números de 4 dígitos son divisibles entre 17
    n = 0
    for a in range (1000,10000):
        b = a%17
        if b == 0:
            n += 1
    return n


def calcularOperaciones():  #Calcula operaciones 
    print("""
Operaciones curiosas:
""")
    a = 1
    c = 2
    for b in range(1,10):
        n1 = (a*8)+b
        print("%d * 8 + %d = %d" % (a,b,n1))
        a = (a*10)+c
        c += 1
    print(" ")
    x = 1
    for i in range(9):
        n2 = x*x
        print("%d * %d = %d" % (x,x,n2))
        x = (x*10)+1


def main():   #Función principal
    opcion = menu()
    while opcion != 0:
        if opcion == 1:
            img = Image.new("RGB",(600,600),"white")
            canvas = ImageDraw.Draw(img)
            dibujarCuadrosCirculos(canvas)
            img.show()
        elif opcion == 2:
            img = Image.new("RGB",(600,600),"white")
            canvas = ImageDraw.Draw(img)
            dibujarEstrella(canvas)
            img.show()
        elif opcion == 3:
            dibujarEspiral()
        elif opcion == 4:
            img = Image.new("RGB",(600,600),"white")
            canvas = ImageDraw.Draw(img)
            dibujarRed(canvas)
            img.show()
        elif opcion == 5:
            divisibles = calcularDivisibles()
            print("Hay", divisibles,"números de 4 dígitos que se pueden dividir entre 17")
        elif opcion == 6:
            calcularOperaciones()
        else:
            print("Opción incorrecta, debes teclear un número del 0 al 6")
        opcion = menu()
    print("""
- Eso ha sido todo, gracias por probar el programa -""")
    
    
main()