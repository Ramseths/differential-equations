# sir_model.py
import matplotlib.pyplot as plt
import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if base_dir not in sys.path:
    sys.path.append(base_dir)

from utils.differential_equations_utils import dudt, create_time_array

def sir_eq(u, t, params):
    S, I, R = u
    beta, gamma = params
    dSdt = -beta * S * I
    dIdt = beta * S * I - gamma * I
    dRdt = gamma * I
    return [dSdt, dIdt, dRdt]

# Condiciones iniciales
S0 = 0.99
I0 = 0.01
R0 = 0.0
u0 = [S0, I0, R0]

# Parámetros del modelo SIR
beta = 0.4  # Tasa de infección
gamma = 0.1  # Tasa de recuperación
params = [beta, gamma]

# Definir el intervalo de tiempo
t = create_time_array(0, 100, 1000)

# Resolver el sistema de ecuaciones diferenciales
sol = dudt(sir_eq, u0, t, params)

# Graficar la solución
plt.plot(t, sol[:, 0], label='Susceptibles')
plt.plot(t, sol[:, 1], label='Infectados')
plt.plot(t, sol[:, 2], label='Recuperados')
plt.xlabel('Tiempo (días)')
plt.ylabel('Fracción de la población')
plt.title('Modelo SIR de Enfermedad Infecciosa')
plt.legend(loc='best')
plt.show()
