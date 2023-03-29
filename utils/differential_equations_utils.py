import numpy as np
from scipy.integrate import odeint

# Primer orden
def dydt(f, y0, t, *args):
    """
    Resuelve una ecuación diferencial de primer orden.

    Args:
        f: Función que representa la ecuación diferencial.
        y0: Condición inicial.
        t: Array de puntos de tiempo.
        *args: Parámetros adicionales para la función f.

    Returns:
        Array con la solución de la ecuación diferencial.
    """
    return odeint(f, y0, t, args=args)

# Sistema de ecuaciones
def dudt(f, u0, t, params):
    """
    Resuelve un sistema de ecuaciones diferenciales.

    Args:
        f: Función que representa el sistema de ecuaciones diferenciales.
        u0: Array con condiciones iniciales.
        t: Array de puntos de tiempo.
        params: Parámetros adicionales para la función f.

    Returns:
        Array con la solución del sistema de ecuaciones diferenciales.
    """
    return odeint(f, u0, t, args=(params,))

# Punto tiempo
def create_time_array(start, stop, num_points):
    """
    Crea un array de puntos de tiempo.

    Args:
        start: Tiempo inicial.
        stop: Tiempo final.
        num_points: Número de puntos en el array.

    Returns:
        Array de puntos de tiempo.
    """
    return np.linspace(start, stop, num_points)
