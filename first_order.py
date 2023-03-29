import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# dy/dt = f(y, t)
def f(y, t):
    k = -0.3
    dydt = k * y
    return dydt

# Condiciones iniciales
y0 = 5

# Definir el intervalo de tiempo
t = np.linspace(0, 20, 100)

# Resolver la ecuación diferencial
y = odeint(f, y0, t)

# Graficar la solución
plt.plot(t, y)
plt.xlabel('Tiempo -')
plt.ylabel('y(t)')
plt.title('Solución de la Ecuación Diferencial')
plt.show()