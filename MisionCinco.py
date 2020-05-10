#Autor: Elena R.Tovar, A01376318
#Misión 5: Funciones de dibujo
from PIL import Image, ImageDraw
from random import randint
import turtle

def dibujarCuadrosCirculos():  #dibuja los cuadrados con circulos
    img=Image.new("RGB", (600,600), "white")
    canvas =ImageDraw.Draw(img)
    
    a=600
    for x in range (0,301,10):
        pa=(x,x)
        pb=(x+a, x+a)
        canvas.line(pa+(x+a,x)+pb+(x,x+a)+(x,x), "black")
        canvas.ellipse(pa+pb,"white", "black")
        a=a-20
        
    img.show()
    
def dibujarEstrella():   #dibuja la estrella
    imgEstrella= Image.new("RGB", (600,600), "white")
    canvas = ImageDraw.Draw(imgEstrella)
    for y in range (0,301,10):
        a=(300,y)
        b=(300+y, 300)
        c=(600-y,300)
        d=(300, 300+y)
        e=(300,600-y)
        f=(300-y, 300)
        g=(y,300)
        h=(300,300-y)
        rojo=randint(0,255)
        verde=randint(0,255)
        azul=randint(0,255)
        canvas.line(a+b,(rojo,verde,azul))
        canvas.line(c+d,(rojo,verde,azul))
        canvas.line(e+f,(rojo,verde,azul))
        canvas.line(g+h,(rojo,verde,azul))
    imgEstrella.show()
    
def dibujarEspiral():
    turtle.color("black")
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.right(90)
    for x in range(0,606,5):
        turtle.forward(x)
        turtle.left(90)
    
def dibujarRed():
    imgRed= Image.new("RGB", (600,600), "white")
    canvas = ImageDraw.Draw(imgRed)
    for x in range(20,601,20):
        a=(0,x)
        b=(x,0)
        c=(x,600)
        d=(600,x)
        canvas.line(a+b, "blue")
        canvas.line(c+d, "blue")
    for y in range(20,601,20):
        a=(0,600-y)
        b=(600-y,0)
        c=(600,y)
        d=(y,600)
        canvas.line(b+c,"red")
        canvas.line(a+d,"red")
    imgRed.show()
    
def calcDiv17():
    cont=0
    for x in range(1000, 10000):
        if (x%17)==0:
            cont=cont+1
    return cont

def numPiramides():
    cont=0
    for x in range (1,10):
        cont=(cont*10+x)
        calc=(cont*8+x)
        print("%d* 8 + %d =9%d" %(cont,cont,calc))
    print("""
        
        """)
    cant=1
    print("1*1=1")
    for x in range(1,10):
        cant=(cant*10+1)
        colc=(cant*cant)
        print("%d + %d = %d" %(cant, cant, colc))

def menu():
    print("""
        1.Dibujar Cuadros y Círculos
        2.Dibujar Parábolas
        3.Dibujar Espiral
        4.Dibujar Red
        5.Contar divisibles entre 17
        6.Imprimir pirámides de números
        0.Salir
        
        ¿Qué desea hacer?
    """)
    opcion=int(input("Teclea tu opción: "))
    return opcion

def main():
    opcion = menu()
    while opcion !=0:
        if opcion==1:
            dibujarCuadrosCirculos()
        elif opcion==2:
            dibujarEstrella()
        elif opcion==3:
            dibujarEspiral()
        elif opcion==4:
            dibujarRed()
        elif opcion==5:
            cont=calcDiv17()
            print("Existen %d números de 4 dígitos divisibles entre 17" %(cont))
        elif opcion==6:
            numPiramides()
        else:
            print("COMANDO NO VÁLIDO")
        opcion =menu()
    print("END")

main()