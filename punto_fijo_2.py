from math import * # importe todas la funciones de la libreria
import numpy as np #trabaja con arregos o vectores

#Polinomios
def fx(x):
    return (x+1)**(1/3)

def gx(x):
    return (x+1)**(1/3)

#Ingreso de datos de entrada
tol = float(input("Ingrese la toleracia: "))
p0 = float(input("Ingrese la aproximacion inicial: "))
error = abs(gx(p0)-p0)
i = 0

#Ciclos de iteracion
while error <= tol and i <= 100:
    i += 1 
    print(i, 'p0=',p0, 'f(x)=', fx(p0), 'gx(x)=',gx(p0), 'Error=',error)
    if i >0:
        error = np.abs(gx(p0)-p0)
        p0 = gx(p0)
        i +=1
    else:
        print(f"El metodo fallo despues de: {p0}")

print("# i\t\t  p0 \t\t  f(x)   \t\tgx(x)\t    error")
while error > tol and i < 100:
    p0 = gx(p0)
    p = fx(p0)
    error = np.abs(gx(p0)-p0)
    i +=1
    print("{0} \t\t  {1:6.6f} \t  {2:6.6f} \t    {3:6.6f}   \t   {4:6.6f}".format(i, p0, fx(p0), gx(p0) , error ))  
    

print(f"El valor de x, tal que f(x) = 0 es: {p0}") 




