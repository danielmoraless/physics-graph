import pandas as pd
import numpy as np
from numpy.polynomial import polynomial as poly
from matplotlib import pyplot as plt

datos = pd.read_excel('data.xlsx', sheet_name='P31').to_numpy()
x = datos[:, 0]
y = datos[:, 1]

x_sample = np.linspace(x.min(), x.max(), 200)

coeficientes = poly.polyfit(x, y, 1)
fity = poly.polyval(x_sample, coeficientes)

fig, ax = plt.subplots()
ax.set_title('V vs t')
ax.set_xlabel('t (s)')
ax.set_ylabel('V (m/s)')
ax.grid(True, 'both')
ax.minorticks_on()

ax.errorbar(x, y, fmt='+')
ax.plot(x_sample, fity)

plt.show()