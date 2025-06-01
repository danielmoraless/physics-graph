import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from numpy.polynomial import polynomial as poly

datos = pd.read_excel('data.xlsx', sheet_name='resorte').to_numpy()
x = datos[:, 0]
y = datos[:, 1]

st_x = x.std()/np.sqrt(x.shape[0])

x_samples = np.linspace(x.min(), x.max(), 200)

coeficientes = poly.polyfit(x, y, 1)
av_y = poly.polyval(x_samples, coeficientes)

fig, ax = plt.subplots()

ax.set_title('d vs W')
ax.set_xlabel('W (g)')
ax.set_ylabel('d (cm)')
ax.grid(True, 'both')
ax.minorticks_on()

ax.errorbar(x, y, 0.5, st_x, fmt=',')
ax.plot(x_samples, av_y)

plt.show()
