import pandas as pd
import numpy as np
from numpy.polynomial import polynomial as poly
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

datos = pd.read_excel('data.xlsx', sheet_name='P38').to_numpy()
x = datos[:, 0]
y = datos[:, 1]

x_samples = np.linspace(x.min(), x.max(), 200)
logx_samples = np.log10(x_samples)

def f(xv, y_0, m):
    return y_0 * xv**m

popt, pcov = curve_fit(f, x, y)

coeficientes = poly.polyfit(np.log10(x), np.log10(y), 1)
fity = poly.polyval(logx_samples, coeficientes)

fig, ax = plt.subplots(1, 2)

ax[1].set_xscale('log')
ax[1].set_yscale('log')

for i in range(len(ax)):
    ax[i].set_title('V vs t')
    ax[i].set_xlabel('t (s)')
    ax[i].set_ylabel('V (m/s)')
    ax[i].grid(True, 'both')
    ax[i].minorticks_on()

ax[0].errorbar(x, y, fmt='+')
ax[0].plot(x_samples, f(x_samples, *popt))
ax[1].errorbar(x, y, fmt='+')
ax[1].plot(x_samples, 10**fity)

plt.show()