import pandas as pd
import numpy as np
from numpy.polynomial import polynomial as poly
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

datos = pd.read_excel('data.xlsx', sheet_name='P56').to_numpy()
x = datos[:, 0]
y = datos[:, 1]

x_samples = np.linspace(x.min(), x.max(), 200)

def f(xv, y_0, m):
    return y_0 * np.exp(-m*xv)

popt, pcov = curve_fit(f, x, y)

coeficientes = poly.polyfit(x, np.log10(y), 1)
fity = poly.polyval(x_samples, coeficientes)

fig, ax = plt.subplots(1, 2)

ax[1].set_yscale('log')

for i in range(len(ax)):
    ax[i].set_title('Q vs t')
    ax[i].set_xlabel('t (s)')
    ax[i].set_ylabel('Q (mC)')
    ax[i].grid(True, 'both')
    ax[i].minorticks_on()

ax[0].errorbar(x, y, fmt='+')
ax[0].plot(x_samples, f(x_samples, *popt))
ax[1].errorbar(x, y, fmt='+')
ax[1].plot(x_samples, 10**fity)

plt.show()