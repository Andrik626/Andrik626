from math import * #* importe todas la funciones de la libreria
import numpy as np #trabaja con arregos o vectores
import matplotlib . pyplot as plt #permite graficar

def funcion1(x):
    return x**3 + 4*x**2 - 10.0


x=np.linspace(0, 5,100)

plt.plot(x, funcion1(x))
plt.axhline(0, color="blue")
plt.axvline(0, color="black")

F1 = funcion1(1)
print(F1)
F2 = funcion1(2)
print(F2)

plt.show()

# Ingreso datos de entrada para los diferentes métodos a trabajar
a = 1
b = 2

# guarda valores iniciales
a0 = a
b0 = b

#guarda valores iniciales del error y del número de iteraciones
tol = 0.000001 #float(input("Ingrese el valor de la tolerancia: "))
nmax = 100 #float(input("Ingrese el número máximo de iteraciones: "))
error = 100
niter = 0

# Método de Bisección

# evaluo primer valor medio
m = a + (b - a)/2

#Evaluacion de la función en los puntos a, b y m
fa = funcion1(a)
fb = funcion1(b)
fm = funcion1(m)

print("# iter\t\t a \t\t f(a) \t\t b \t\t f(b) \t\t m \t\t f(m) \t\t error")
print("{0} \t\t {1:6.4f} \t {2:6.4f} \t {3:6.4f} \t {4:6.4f} \t {5:6.4f} \t {6:6.4f} \t {7:6.4f}".format(niter, a0, fa, b0, fb, m, fm, error ))

# ciclo iterativo
while error > tol and niter < nmax:
    m = a + (b - a) / 2
    if np.sign(fa) == np.sign(fm):
        a = m
        fa = funcion1(a)
    else:
        b = m
        fb = funcion1(b)
    
    m = a + (b - a)/2
    fm = funcion1(m)
    error = abs(b - a)
    niter += 1
    print("{0} \t\t {1:6.6f} \t {2:6.6f} \t {3:6.6f} \t {4:6.6f} \t {5:6.6f} \t {6:6.6f} \t {7:6.6f}".format(niter, a, fa, b, fb, m, fm, error ))

print("La raíz de la función dada en el intervalo [{0:6.4f},{1:6.4f}] es {2:6.7f}".format(a0,b0,m))