import matplotlib.pyplot as plt
import numpy as np

# Función cuadrática.
def f(x):
    return (x +1)**(1/2)

def g(x):
    return (1+(1/2)*x)

def h(x):
    return (1+((1/2)*x)-((1/8)*(x**2)))

def j(x):
    return (1+((1/2)*x) - ((1/8)*(x**2)+ ((1/16)*(x**3))))
{}

# Valores del eje X que toma el gráfico.
x=np.linspace(-1, 10,100)

# Graficar ambas funciones.
plt.plot(x, f(x), label = "$\sqrt{x+1}$")
plt.plot(x,g(x), label=r"$1 + \frac{1}{2}x$")
plt.plot(x,h(x),  label=r"$1 + \frac{1}{2}x - \frac{1}{8}x^2$")
plt.plot(x,j(x),  label=r"$1 + \frac{1}{2}x - \frac{1}{8}x^2 + \frac{1}{16}x^3$")
plt.axhline(0, color="blue")
plt.axvline(0, color="black")
plt.xlim(-1, 10)
plt.ylim(-1, 5)
plt.savefig("output.png") # Guardar gráfico como imágen PNG.
# Mostrarlo.
plt.legend()
plt.show()