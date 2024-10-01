from math import * #* importe todas la funciones de la libreria
import numpy as np #trabaja con arregos o vectores

#Definimos nuestra funcion
def f(x):
    return x**3 - x -1
   


# Ingreso datos de entrada para los diferentes métodos a trabajar
a = int(input("Ingresa el intervalo a: "))
b = int(input("Ingresa el intervalo b: "))

#guarda valor inicial y del número de iteraciones
x = float(input("Ingrese una aproximacion inicial:"))
tol = float(input("Ingrese el valor de la tolerancia: "))

# Funcion de derivada
def derivada(x,h):
    return (f(x+h) - f(x))/h

#Funcion del error
def error(pn,x):
    return abs(pn-x)

#Funcion de newton
def newton(x,tol):
    i = 0
    dx = -f(x)/derivada(x,tol)
    pn = x + dx
    print("# i\t\t x\t\t f(x) \t\t derivada(x,tol)\t pn\t\t error\t\t tolerancia")
    #Nuestro ciclo iterativo
    while (abs(dx) >= tol ) and i<=100:
        x = x + dx
        dx = -f(x)/ derivada(x,tol)
        i+=1
        error(pn,x)
        pn = x + dx
        print("{0} \t\t {1:6.6f} \t {2:6.6f} \t  {3:6.6f} \t\t {4:6.6f} \t{5:6.6f} \t{6:6.6f}".format(i, x, f(x),derivada(x,tol),pn,error(pn,x), tol ))
    return x

x = newton(x,tol)
print(f"El valor de x, tal que f(x) = 0, es: {x}") 
print(f"En el intervalo: {[a,b]}")




