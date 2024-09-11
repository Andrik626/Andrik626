import matplotlib.pyplot as plt
import numpy as np
import sympy  as spy
#pip install sympy

# Función cuadrática.
x = spy.symbols('x')
g = spy.exp(x/2)*spy.sin(x/3)

#Calcular la primera derivada
f_1 = spy.diff(g,x)
print(g)
print(f_1)

#Calcular la segunda derivada
f_2 = spy.diff(f_1,x)
print(f_2)

#Calcular la tercera derivada
f_3 = spy.diff(f_2,x)
print(f_3)

#Calcula la cuarta derivada
f_4 = spy.diff(f_3,x)
print(f_4)

def f(x):
    return np.exp(x/2)*np.sin(x/3)

{}

# Valores del eje X que toma el gráfico.
x=np.linspace(-10, 10,400)

#Calcular los valores de la funcion
y=f(x)

# Graficar la funcion.
plt.figure(figsize=(8,6))
plt.plot(x, f(x))
plt.title('Grafica del polinomio de Maclaurin')
plt.axhline(0, color="blue")
plt.axvline(0, color="black")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)


plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()