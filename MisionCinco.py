# Mariana Mejía Béjar
# Misión 5. El ciclo for y while (menu)


import turtle 
from PIL import Image, ImageDraw
from random import randint


# Define el menú que le muestra al usuario las opciones a elegir de aquelo que puede realizar el programa
def menu():
    print("Misión 5. Seleccione qué quiere hacer.")
    print("1. Dibujar cuadros y círculos")
    print("2. Dibujar parábolas en forma de estrella")
    print("3. Dibujar espiral")
    print("4. Dibujar red")
    print("5. Contar divisibles entre 17")
    print("6. Imprimir pirámides de números")
    print("0. Salir")
    opcion = int(input("Qué desea hacer?: "))
    return opcion


# Define la función que dibuja los cuadrados y los círculos
def dibujarCuadrosCirculos(imagen):
    a = 600                         
    for figura in range(0, 301, 10):        #(0, 10, 20, 30, 40... 300(
        puntoa = (figura,figura)
        puntob = (figura+a, figura+a)
        imagen.line(puntoa + (figura+a,figura) + puntob + (figura, figura+a) + (figura,figura), "black")
        imagen.ellipse(puntoa+puntob, "white", "black")
        a = a-20            #Cada vez que corre el for, le resta 20 al 600 (580...)
        
    
# Define la función que dibuja la estrella
def dibujarEstrella(imagen):
    for y in range(0, 301, 10):        #(0, 10, 20...300)
        a = (300, y)
        b = (300+y, 300)
        # generar color aleatorio
        rojo = randint(0,255)
        verde = randint(0,255)
        azul = randint(0,255)
        imagen.line(a+b, (rojo, verde, azul))
        
    for x in range(0, 301, 10):         #(0, 10, 20...300)
        c = (x, 300)
        d = (300, 300+x)
        # generar color aleatorio
        rojo = randint(0,255)
        verde = randint(0,255)
        azul = randint(0,255)
        imagen.line(c+d, (rojo, verde, azul))
        
    for y in range(0, 301, 10):          #(0, 10, 20...300)
        e = (300, y)
        f = (300-y, 300)
        # generar color aleatorio
        rojo = randint(0,255)
        verde = randint(0,255)
        azul = randint(0,255)
        imagen.line(e+f, (rojo, verde, azul))
        
    for x in range(300, 601, 10):         #(300, 310, 320...600)
        g = (x, 300) 
        h = (300, 900-x)
        # generar color aleatorio
        rojo = randint(0,255)
        verde = randint(0,255)
        azul = randint(0,255)
        imagen.line(g+h, (rojo, verde, azul))
        
        
# Define la función que por medio de la tortuga dibujará un espiral
def dibujarEspiral():
    turtle.color("black")
    
    for t in range (5, 601, 10):         #(5, 15, 25... 600)
        turtle.forward (t)
        turtle.left (90)
        turtle.forward (t+5)
        turtle.left (90)
        turtle.forward (t+5)
        turtle.left (90)
        turtle.forward (t+10)
        turtle.left (90)
        
        turtle.speed(7)
   
   
# Define la función que va a dibujar la red   
def dibujarRed(imagen):
    for linearojo in range(0,601,20):       #(0, 20, 30, 40... 600)
        la=(0,600-linearojo)
        lb=(linearojo,600)
        lc=(600,linearojo)
        ld=(600-linearojo,0)
        imagen.line(la+lb,"red")
        imagen.line(lc+ld,"red")
        
    for lineaazul in range(0,601,20):       #(0, 20, 30, 40... 600)
        le=(0,lineaazul)
        lf=(lineaazul,0)
        lg=(lineaazul,600)
        lh=(600,lineaazul )
        imagen.line(le+lf, "blue")
        imagen.line(lg+lh, "blue")
        
        
# Define la función que dice cuántos números son divisibles entre 17
def dividirNumeros():
    cantidad = 0
    
    for numero in range (1000,10000,1): #Empieza desde el 1000 porque se piden números de 4 dígitos. Se pone hasta el 10000 para que se incluya el 9999 (1000, 1001, 1002, 1003, 1004... 9999). 
        if numero%17 == 0: 
            '''print (numero, "es divisible entre 17")'''
            
            #El contador va sumando 1 al número previo cada vez que encuentra un número divisible netre 17
            cantidad = cantidad+1
    print (cantidad, "números de 4 dígitos se pueden dividir entre 17.") #El contador nos dice cuantos número detectó que se pueden dividir exactamente entre 17
    
    
# Define la función que se encarga de realizar las pirámides de números
def calcularPiramide():
    a = 0
    for x in range (1, 10, 1):       #Rango de 9. (1, 2, 3... 9)
        a = (a * 10) + x
        b = (a * 8) + x
        print (a,"* 8 +", x, "=", b)   
    print (" ")
    c = 0
    d = 0
    for x in range (1, 10, 1):       #Rango de 9. (1, 2, 3... 9)
        c = (c * 10) + 1
        d = (d * 10) + 1
        e = b * d
        print (c, "*", d,"=", e)
    

# Define la función principal
def main():
    opcion = menu()
    
    while opcion !=0 :
        if opcion == 1:
            img = Image.new("RGB", (600, 600), "white")
            imagen = ImageDraw.Draw(img)
            dibujarCuadrosCirculos(imagen)
            img.show()
            
        elif opcion == 2:
            img = Image.new("RGB", (600, 600), "white")
            imagen = ImageDraw.Draw(img)
            dibujarEstrella(imagen)
            img.show()
            
        elif opcion == 3:
            dibujarEspiral()
            
        elif opcion == 4:
            img = Image.new("RGB", (600, 600), "white")
            imagen = ImageDraw.Draw(img)
            dibujarRed(imagen)
            img.show()
        
        elif opcion == 5:
            print(" ")
            cantidad = dividirNumeros()
            print(" ")
            
        elif opcion == 6:
            print(" ")
            calcularPiramide()
            print(" ")
        
        else:
            print(" ")
            print("ERROR: Favor de insertar un número del 0 al 6")
            print(" ")
        
        opcion = menu()
    

main()

