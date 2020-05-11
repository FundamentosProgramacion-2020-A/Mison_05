# Miguel Castillo Ordaz - Grupo 2 - a01746128
# Programa en conjunto que corre cuatro programas para dibujar figuras
# al igual que corre los números divisibles entre 17, y la pirámide
# de números

from PIL import Image,ImageDraw
import turtle
import math

#PROGRAMA 1: Realiza la operación para imprimir cuadros con círculos.

def dibujarCuadrosCirculos():
    img = Image.new("RGB",(600,600),"white")
    canvas = ImageDraw.Draw(img)
    
    a = 600
    for x in range(0,301,10):
        pa = (x,x)
        pb = (x+a, x+a)
        canvas.line(pa+(x+a,x) + pb + (x, x+a) + (x,x),"black")
        canvas.ellipse(pa+pb, "white","black")
        a= a-20
        
    img.show()
    
#PROGRAMA 2: Realiza la operación para dibujar una estrella.            


def dibujarEstrella():

    t = turtle.Turtle()
    t.speed(0)
    t.color("green")

    for i in range(0,11):
        xFrom = 0
        yFrom = (10-i) * 41
        xTo = i * 48
        yTo = 0
        t.penup()
        t.goto(xFrom,yFrom)
        t.pendown()
        t.goto(xTo,yTo)
        
    for i in range(0,11):
        xFrom = 0
        yFrom = (10-i) * -41
        xTo = i * 48
        yTo = -0
        t.penup()
        t.goto(xFrom,yFrom)
        t.pendown()
        t.goto(xTo,yTo)
        
    for i in range(0,11):
        xFrom = 0
        yFrom = (10-i) * 41
        xTo = i * -48
        yTo = 0
        t.penup()
        t.goto(xFrom,yFrom)
        t.pendown()
        t.goto(xTo,yTo)

    for i in range(0,11):
        xFrom = 0
        yFrom = (10-i) * -41
        xTo = i * -48
        yTo = 0
        t.penup()
        t.goto(xFrom,yFrom)
        t.pendown()
        t.goto(xTo,yTo)
        
        
#PROGRAMA 3: Realiza la operación para dibujar la figura concírculos.
# No se pudo hacer desaparecer a la tortuga al terminar el programa.            


def dibujarElipse():

        t = turtle.Turtle()
        t.speed(0)

        for x in range(0, 12):
            for y in range(0, 12):
                t.circle(150)
                t.left(30)
            t.left(30)

#PROGRAMA 4: Realiza la operación para crear una espiral en forma de laberinto.
# La figura dibujada no salió exáctamente igual en la parte del principio y
# al final.
# Este programa no deja seguir dibujando o haciendo operaciones por alguna razón,
# pero funciona bien para dibujar la figura.

def dibujarEspiral():

    t = turtle.Turtle()
    t.speed(0)

    def halfSquare(t, length):
        t.down()
        for i in (0, 1):
            t.forward(length)
            t.left(90)

    def halfSquares(t, initial, increment, reps):
        length = initial
        for i in range(92):
            halfSquare(t, length)
            length += increment

    halfSquares(t, 10, 10, 10)


    turtle.mainloop()
    
#PROGRAMA 5: Realiza operación de cálculo con números enteros.
# Se intentó hacer un aproximado a la operación de la tarea, aunque
# no estoy seguro si estoy en lo correcto.
# No acepta decimales.


def funcionPi():

        n= int( input("Ingresa un número entero positivo: "))
        if n > 0:
            
            
            pi = 0
            for x in range(1,n+1):
                pi += (1/x)
            print("El resultado de la aproximación es: ", pi)
        else:
            print("El número negativo es incorrecto. Inténtalo nuevamente")
        

#PROGRAMA 6: Realiza operación de cálculo con números de cuatro dígitos
#            divisibles entre 19.


def calcularDivisiblesEnElRango():
        
        for x in range(1000,10000):
            numero = x % 19
            
            if numero == 0:
                print(x,":Es divisible entre 19")


#PROGRAMA 7: Realiza operación que permite imprimir columnas de números.


def imprimirPiramides():
        
        valorA=0
        for valorI in range(1,10):
            valorA=valorA*10+valorI
            valorX=valorA*8+valorI
            
            print(valorA,"*","8","+",valorI,"=",valorX)
        print("--------------------------------\n")
        
        valorA=0
        valorB=0
        for i in range(1,10):
            valorA=valorA*10+1
            valorB=valorB*10+1
            valorX=valorA*valorB
            print(valorA,"*",valorB,"=",valorX)


#PROGRAMA JEFE: Programa que realiza un menú para correr todos los
#               programas.

# No están en el orden del PDF de la tarea.

        
def menu():
        print('''
             Mision 5. Seleccione qué quiere hacer.
             
             1. Dibujar cuadros y círculos
             2. Dibujar estrella
             3. Dibujar circulos
             4. Dibujar espiral
             5. Función pi
             6. Contar divisibles entre 17
             7. Imprimir pirámides de números
             0.Salir
             
             ¿Qué desea realizar?
        ''')
        
        opcion = int(input("Teclea tu opción: "))
        return opcion

        
def main():
        

        opcion = menu()
        
        while opcion != 0:
            if opcion ==1:
                dibujarCuadrosCirculos()
            elif opcion==2:
                dibujarEstrella()
            elif opcion==3:
                dibujarElipse()
            elif opcion==4:
                dibujarEspiral()
            elif opcion==5:
                funcionPi()
            elif opcion==6:
                calcularDivisiblesEnElRango()
            elif opcion==7:
                imprimirPiramides()
            else:
                print("Opción incorrecta, debes teclear [0,1,2,3,4,5,6,7]")
                
            opcion = menu()
            
        print("¡Has terminado de participar!")
        
main()
