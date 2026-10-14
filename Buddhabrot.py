# The Buddhabrot is the spatial histogram over the trajectories of 
# points that escape the Mandelbrot fractal.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import PowerNorm
n = 1600
m = 1600
max_val_real = (-2.0,1.0)
max_val_imag = (-1.5,1.5)

real_len = max_val_real[1]- max_val_real[0]
imag_len = max_val_imag[1]- max_val_imag[0]
box_array = np.zeros((n,m)) #n is real, m is imaginary
ddx = real_len/n
ddy = imag_len/m

cnt = 10**6
iters = 20

for a in range(cnt):
    cr = np.random.uniform(*max_val_real)
    ci = np.random.uniform(*max_val_imag)
    zr = 0
    zi = 0
    car = np.empty((iters,2))
    escaped = False
    for x in range(iters):
        t =zr
        zr = zr**2 + cr - zi**2
        zi = 2*t*zi +ci
        car[x, 0] = zr
        car[x, 1] = zi  
        if(zr**2+zi**2>4):
            escaped = True
            break 
    if escaped:
        for c in car[:x+1]:
            xv = c[0] - max_val_real[0]
            yv = c[1] - max_val_imag[0]
            xv //=ddx
            yv //=ddy
            if 0 <= xv < n and 0 <= yv < m:
                box_array[int(xv), int(yv)] += 1

plt.imshow(np.rot90(box_array.T,1), cmap='inferno',norm=PowerNorm(gamma=0.815),extent=[*max_val_real, *max_val_imag],origin='lower', interpolation='nearest')
plt.colorbar(label="Cnt")
plt.show()