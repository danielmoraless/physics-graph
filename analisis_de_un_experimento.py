import pandas as pd
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
from numpy.polynomial import polynomial as poly
import numpy as np

def potf(xv, y_0, m):
    return y_0 * xv**m

d_analisis = pd.read_excel('data.xlsx', sheet_name='analisis').to_numpy()
rho_values = [0.7, 1.5, 2.1, 3.2]
x = d_analisis[:, 0]
x_samples = np.linspace(x.min(), x.max(), 200)
logx_samples = np.log10(np.linspace(1, x.max(), 200))


fig, ax = plt.subplots(1, 2)
# -- CONFIGURACIONES GENERALES --
for i in range(len(ax)):
    ax[i].set_title("Q vs d")   # Título de los gráficos
    ax[i].grid(True, 'both')    # Habilita las líneas de divisiones de escala
    ax[i].minorticks_on()       # Habilita las líneas de subdivisiones de escala
    ax[i].set_xlabel('d (cm)')  # Título del eje x
    ax[i].set_ylabel(r'Q ($cm^{3}/s$)')   # Título del eje y

ax[1].set_xscale('log')
ax[1].set_yscale('log')

for i in range(1, d_analisis.shape[0]+1):
    y = d_analisis[:, i]
    popt, pcov = curve_fit(potf, x, y)

    ax[0].errorbar(x, y, fmt='+')
    # Cada recta o curva promedio corresponde a un valor constante de rho
    label_status = rf'$\rho = {rho_values[i-1]}$'
    ax[0].plot(x_samples, potf(x_samples, *popt), label=label_status)

    # SEGUNDO GRÁFICO
    ax[1].errorbar(x, y, fmt='+')

    coeficientes = poly.polyfit(np.log10(x), np.log10(y), 1)
    logy = poly.polyval(logx_samples, coeficientes)

    ax[1].plot(10**logx_samples, 10**logy, label=label_status)

ax[0].legend()
ax[1].legend()
plt.show()
