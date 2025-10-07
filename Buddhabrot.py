# The Buddhabrot is the probability distribution over the trajectories of 
# points that escape the Mandelbrot fractal.

import numpy as np
import random
import math
import matplotlib.pyplot as plt
n = 600
m = 600
max_val_real = (-1,1)
max_val_imag = (-1,1)
# max_val_real = (-1.5,1.5)
# max_val_imag = (-1.5,1.5)
real_len = max_val_real[1]- max_val_real[0]
imag_len = max_val_imag[1]- max_val_imag[0]
box_array = np.zeros((n,m)) #n is real, m is imaginary
ddx = real_len/n
ddy = imag_len/m

cnt = 10**5
iters = 20
an = np.random.randint(1,n, size = cnt)
am = np.random.randint(1,m, size = cnt)
for a in range(cnt):
    nn = an[a]
    mm = am[a]
    cr = max_val_real[0] + real_len*(nn/n)
    ci = max_val_imag[0] + imag_len*(mm/m)
    zr = 0
    zi = 0
    car = np.zeros((iters,2))
    for x in range(iters):
        t =zr
        zr = zr**2 + cr - zi**2
        zi = 2*t*zi +ci
        car[x] = [zr, zi]
        if(zr**2+zi**2>2):
            car = np.array([])
            break
    if(not car.size ==0):
        for c in car:
            xv = c[0] - max_val_real[0]
            yv = c[1] - max_val_imag[0]
            xv //=ddx
            yv //=ddy
            if(xv < n and yv <m):
                box_array[int(xv), int(yv)] +=1
# print(box_array)
plt.imshow(box_array, cmap='gray',extent=[*max_val_real, *max_val_imag], interpolation='nearest')
plt.colorbar(label="Cnt")
plt.show()