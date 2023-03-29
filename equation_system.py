import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Definir la función que representa el sistema de ecuaciones diferenciales
# d2y/dt2 = f(y, t)
def f(u, t, params):
    theta, omega = u
    g, l = params
    dudt = [omega, -(g/l) * np.sin(theta)]
    return dudt

# Condiciones iniciales

# Ángulo inicial en radianes
theta0 = np.pi / 4
# Velocidad angular inicial  
omega0 = 0.0        
u0 = [theta0, omega0]

# Parámetros del péndulo

 # Aceleración de la gravedad (m/s^2)
g = 9.81
# Longitud del péndulo (m)
l = 1.0
params = [g, l]

# Definir el intervalo de tiempo
t = np.linspace(0, 10, 500)

# Resolver el sistema de ecuaciones diferenciales
sol = odeint(f, u0, t, args=(params,))

# Graficar la solución
plt.plot(t, sol[:, 0], label='Theta(t)')
plt.plot(t, sol[:, 1], label='Omega(t)')
plt.xlabel('Tiempo')
plt.ylabel('Solución')
plt.title('--Movimiento Armónico Simple de un Péndulo--')
plt.legend(loc='best')
plt.show()
