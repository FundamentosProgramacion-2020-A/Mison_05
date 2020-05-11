#Autor José Manuel Rivera Sosapavón
#Misión 05

from PIL import Image, ImageDraw
from random import randint

def menu():
    print ("1. Dibujar cuadrados y circulos")
    print ("2. Dibujar parabolas")
    print ("3. Dibujar espiral")
    print ("4. Dibujar red")
    print ("5. Contar divisores entre 17")
    print ("6. Imprimir piramides de numeros")
    print ("0. Salir")
    opcion =int(input("Teclea tu opción: "))
    return opcion

def dibujarCuadradosCirculos(imagen):
    a= 600
    for x in range (0,301,10):
        pa = (x,x)
        pb = (x+a, x+a)
        imagen.line(pa+(x+a,x)+pb+(x,x+a)+(x,x), "black")
        imagen.ellipse(pa+pb, "white", "black")
        a = a-20
        
        
def dibujarEstrella(imagen):
    for y in range(0,301,10):
        pA = (300,y)
        pB = (300-y, 300)
        pC = (300,y)
        pD = (300+y,300)
        pE =(y,300)
        pF =(300,y+300)
        pG =(600-y,300)
        rojo = randint(0,255)
        verde = randint(0, 255)
        azul = randint (0,255)
        imagen.line(pA+pB+pC+pD+pE+pF+pG,(rojo,verde,azul))
    
            
def dibujarEspiral(imagen):
    for x in range (10, 301, 10): #va a subir de 10 en 10 del 10-300
        pA= (600-x, 600-x)
        pB = (x,600-x)
        pC = (x,x)
        pD = (600-x-10,x)
        pE = (600-10-x, 600-10-x)
        imagen.line(pA+pB+pC+pD+pE, "black")
    
        
def dibujarRed (imagen):
    for y in range (0,1201,20):
        imagen.line(((600,y-600),(0,y)),"blue")
    for x in range (0,1201,20):
        imagen.line(((x-600,0),(x,600)),"red")
        
def dividirDivisores():
    x=0
    for y in range (1000,10000):
        if y%17==0:
            x=x+1
    print ("Hay %d numeros de 4 digitos divisibles a 17" %(x))
        
def calcularPiramide():
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
    
    
        
def main():
    opcion = menu()
    while opcion !=0:
        if opcion ==1:
            imgCirculo = Image.new("RGB",(600,600),"white")
            canvas = ImageDraw.Draw(imgCirculo)
            dibujarCuadradosCirculos(canvas)
            
            imgCirculo.show()
            
    
        elif opcion ==2:
            imgEstrella = Image.new("RGB",(600,600),"white")
            canvas = ImageDraw.Draw(imgEstrella)
            dibujarEstrella(canvas)
            
            imgEstrella.show()
        
        elif opcion ==3:
            imgEspiral = Image.new("RGB",(600,600),"white")
            canvas = ImageDraw.Draw(imgEspiral)
            dibujarEspiral(canvas)
            
            imgEspiral.show()
    
    
        elif opcion ==4:
            imgRed = Image.new("RGB",(600,600),"white")
            canvas = ImageDraw.Draw(imgRed)
            dibujarRed(canvas)
            
            imgRed.show()
            
        elif opcion==5:
            dividirDivisores()
        
        elif opcion==6:
            calcularPiramide()
            
        elif opcion > 6:
            print ("ERROR, elige una opción valida.")
            
        opcion=menu()
        
    print ("Usted ha salido del menú.")
        
        
            
    
    
main()
    
    