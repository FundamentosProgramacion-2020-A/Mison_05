#Autor: Alondra Miranda Aguilera A01746742
#Misión 5: Menú

from PIL import Image, ImageDraw
from random import randint
import turtle

def menu():
    print('''
    1. Dibujar Cuadros y Círculos
    2. Dibujar Estrella
    3. Dibujar Espiral
    4. Dibujar Red
    5. Contar divisibles entre 17
    6. Pirámides de Números
    0. Salir
    ''')
    o = int(input("Hola Profe, eliga la opción que guste: "))
    return o


#-------------------------CUADROS CÍRCULOS-----------------------
def cuaCir(canvas):
    a=600
    for x in range (0,601,10):
        pa=(x,x)
        pb=(x+a,x+a)
        canvas.line(pa+(x+a,x)+pb+(x,x+a)+(x,x), "white")
        canvas.ellipse(pa+pb, "black", "white")
        a = a-20


#---------------------------------ESTRELLA----------------------
def dibujarEstrella(imagen):
    for y in range (0, 301, 10):
        a = 300,y
        b = 300+y,300
        rojo = randint(0,255)
        verde = randint(0,255)
        azul = randint(0,255)
        imagen.line(a+b, (rojo, verde, azul))
        
        a = 300,y
        b = 300-y, 300
        rojo = randint(0,255)
        verde = randint(0,255)
        azul = randint(0,255)
        imagen.line(a+b, (rojo, verde, azul))
        
        a = 300,600-y
        b= 300+y,300
        rojo = randint(0,255)
        verde = randint(0,255)
        azul = randint(0,255)
        imagen.line(a+b, (rojo, verde, azul))
        
        a = 300,600-y
        b= 300-y,300
        rojo = randint(0,255)
        verde = randint(0,255)
        azul = randint(0,255)
        imagen.line(a+b, (rojo, verde, azul))


#---------------------------------ESPIRAL----------------------
def dibujarEspiral():
    for x in range (5,500, 20):
        turtle.forward(x)
        turtle.left(90)
        turtle.forward(x+10)
        turtle.left(90)
        turtle.forward(x+10)
        turtle.left(90)
        turtle.forward(x+20)
        turtle.left(90)


#------------------------------------RED------------------------
def dibujarRed(imagen):
    for y in range (0, 600, 20):
        a = 20+y, 0
        b = 0, 20+y
        imagen.line(a+b, "blue")
        
    for y in range (0, 600, 20):
        a = y-20, 600
        b = 600, y-20
        imagen.line(a+b, "blue")
    
    for y in range (0, 600, 20):
        a = 0+y, 0
        b = 600, 600-y
        imagen.line(a+b, "red")
        
    for y in range (0, 600, 20):
        a = 0+y, 600
        b = 0, 600-y
        imagen.line(a+b, "red")


#---------------------------------DIVISIBLES-------------------------
def calcularDivisibles():
    cont= 0
    for x in range (1000,10000):
        if x %17 == 0:
            cont=cont+1
    return cont


#--------------------------------------PIRÁMIDES--------------------
def piramideUno():
    b=0
    for x in range (1,10):
        b = b*10+x
        a=b*8+x
        print(b, "* 8 +", x,"=", a)
        
def piramideDos():
    c=0
    x=0
    for x in range (1,11):
        x=x+1
        if x<11:
            c= c*10+1
            d= c*c
            print (c ,"*", c, "=", d)



#--------------------------------------------------------------------
def main():
    img = Image.new("RGB", (600,600), "black")
    canvas=ImageDraw.Draw(img)
    
    o = menu()
    
    while o != 0:
        
        if o == 1: #Cuadros Círculos
            img = Image.new("RGB", (600,600), "black")
            canvas=ImageDraw.Draw(img)
            cuaCir(canvas)
            img.show()
            
        elif o == 2: #Estrella
                imgEstrella = Image.new("RGB", (600,600), "black")
                canvas = ImageDraw.Draw(imgEstrella)
                dibujarEstrella(canvas)
                imgEstrella.show()
                
        elif o == 3: #Espiral
                dibujarEspiral()
                
        elif o == 4: #Red
                imgRed = Image.new("RGB", (600,600), "black")
                canvas = ImageDraw.Draw(imgRed)
                dibujarRed(canvas)
                imgRed.show()
                
        elif o == 5: #Divisibles
                divisibles = calcularDivisibles()
                print(divisibles)
                
        elif o == 6: #Pirámides
                piramideUno()
                piramideDos()
        
        else:
            print("Ese número no es válido, ponga otro")
            
        o = menu()
        
    print("Si saqué 100 verdad profe? :D ")
    
main()