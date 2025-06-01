import pandas as pd
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
from numpy.polynomial import polynomial as poly
import numpy as np

# Importamos los datos del archivo Excel
datos = pd.read_excel('data.xlsx', sheet_name='pendulo').to_numpy()
x = datos[:, 0] # La primera colummna del Excel corresponde a los valores de x
y = datos[:, 1] # La segunda colummna del Excel corresponde a los valores de y

# Calculamos la desviación típica del tiempo
st_y = y.std()/np.sqrt(y.shape[0])

# Generamos valores en x para suavizar la curva promedio
x_samples = np.linspace(x.min(), x.max(), 200)

# Generamos valores en x para suavizar la línea promedio
logx_samples = np.log10(np.linspace(1, x.max(), 200))

# La función f representa a la forma general de la función potencial y = y_0 * x**m
#
# Esta función se utiliza para obtener los valores que le corresponden a los valores
# generados para suavizar la curva promedio.
# O sea, y = f(x, y_0, m) = y_0 * x**m
def f(xv, y_0, m):
    return y_0 * (xv**m)

# curve_fit utiliza los cuadrados mínimos no lineales para ajustar
# la función dada (f) a los datos.
# En este caso, popt son los valores de ajuste:
#   - Constante de proporcionalidad y_0
#   - Pendiente m
popt, pcov = curve_fit(f, x, y)

# polyfit hace un ajuste de mínimos cuadrados de
# un polinomio de grado 1 a los datos.
coeficientes = poly.polyfit(np.log10(x), np.log10(y), 1)

# Dados los coefientes del ajuste de los datos originales,
# polyval evalúa el polinomio en los valores de x que
# suavizarán la recta.
logy = poly.polyval(logx_samples, coeficientes)

# Genera una figura que contendrá dos gráficos
# Cada gráfico se encuentra, en orden, según índices:
# ax[0], ax[1], ..., ax[n]
fig, ax = plt.subplots(1, 2)

# -- CONFIGURACIONES GENERALES --
for i in range(len(ax)):
    ax[i].set_title("t vs L")   # Título de los gráficos
    ax[i].grid(True, 'both')    # Habilita las líneas de divisiones de escala
    ax[i].minorticks_on()       # Habilita las líneas de subdivisiones de escala
    ax[i].set_xlabel('L (cm)')  # Título del eje x
    ax[i].set_ylabel('t (s)')   # Título del eje y

# -- PRIMER GRÁFICO --
# Grafica los puntos con sus respectivas barras de error
ax[0].errorbar(x, y, st_y, 0.5, fmt='o')
# Grafica la curva promedio
ax[0].plot(x_samples, f(x_samples, *popt))

# -- SEGUNDO GRÁFICO --]
# Configura la escala a loglog
ax[1].set_xscale('log')
ax[1].set_yscale('log')
#Grafica las barras de error
ax[1].errorbar(x, y, st_y, 0.5, fmt='o')
# Grafica la recta promedio
ax[1].plot(10**logx_samples, 10**logy)

# Muestra la figura que contiene los gráficos
plt.show()

