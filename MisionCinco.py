#Autor: Andy Dino Martíenz Hernández, A01376720
#Ejemplo de misión 5

from PIL import Image, ImageDraw
from random import randint
import turtle

#Función del menú
def menu():
    print ('''
            1.- Dibujar circulo con cuadrado
            2.- Dibuja una estrella
            3.- Dibuja una espiral con tortuga
            4.- Dibuja una red
            5.- Contar divisibles entre 17
            6.- Imprimir pirámide de números
            0.- Salir
    ''')
    opcion= int (input("Teclea tu opción: "))
    
    return opcion


#Función del círculo y el cuadrado
def dibujarCuadrosCirculos(imagen):
    a= 600
    for x in range (0,301,10):
        posA= (x,x)
        posB= (x+a,x+a)
        imagen.line(posA+(x+a,x)+posB+(x,x+a)+(x,x), "black")
        #canvas.rectangle (pa+pb, "white", "black")
        imagen.ellipse(posA+posB,"white", "black")
        a=a-20


#Función para hacer la estrella
def dibujarEstrella(imagen):
    for y in range (0,301,10):   #[0,10,20...300]
        a=(300, y)
        b=(300+y,300)
        c=(300,y)
        d=(300-y,300)
        
        e=(300,600-y)
        f=(300+y,300)
        g=(300,600-y)
        h=(300-y,300)
        
        #generar color aleatorio
        rojo= randint (0,255)
        verde= randint (0,255)
        azul= randint (0,255)
        
        imagen.line (a+b, (rojo,verde,azul))
        imagen.line (c+d, (rojo,verde,azul))
        imagen.line (e+f, (rojo,verde,azul))
        imagen.line (g+h, (rojo,verde,azul))
        
            
    

#Función de la espiral con la tortuga
def dibujarEspiral():
    
    turtle.penup()
    turtle.goto (0,0)
    turtle.pendown()
    
    for x in range (0,300,10):
        turtle.color ("black")
        
        turtle.forward (x)
        turtle.right (90)
        

#Función de la red con colores
def dibujarRed(imagen):
    for x in range (600, -600,-20):
        a= (x,0 )
        b= (x+600, 600)
        
        imagen.line (a+b, "blue")
    
    for x in range (-300,600,20):
        a= (x,600)
        b= (x+600,-600)
        
        imagen.line (a+b, "red")


#Función para calcular los divisibles
def dividirNumeros():
    cuenta=0
    for x in range (1000,10001):
        if (x%17)==0:
            cuenta=cuenta+1
    return cuenta
            

#Función para hacer la pirámide
def hacerPiramide():
    cont= 0
    for x in range (1,10):
        cont=(cont*10+x)
        calc=(cont*8+x)
        print ("%d* 8+ %d = 9%d" %(cont,cont,calc))
    
    print("""

        """)    
    cont=1
    for x in range (1,10):
        cont=(cont*10+1)
        calc=(cont*cont)
        print ("%d+ %d = %d" % (cont,cont,calc))
        


#Función main
def main():
    
    opcion= menu()  #imprime opciones 1,2, opción guarda esa respuesta
    #Ahora para hacer el canvas
    img= Image.new ("RGB", (600,600), "white")
    canvas = ImageDraw.Draw (img)
    
    divisible=dividirNumeros()
    
    
    while opcion != 0:
        if opcion ==1:
            dibujarCuadrosCirculos(canvas)
            img.show()
        elif opcion ==2:
            dibujarEstrella(canvas)
            img.show()
        elif opcion ==3:
            dibujarEspiral()
        elif opcion==4:
            dibujarRed(canvas)
            img.show()
        elif opcion==5:
            print (divisible)
        elif opcion==6:
            hacerPiramide()
        else:
            print ("Opción incorrecta, debes teclear los números especificados")
        
        
        opcion = menu()
    
    print ("Termina")

main()