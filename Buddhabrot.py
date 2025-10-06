# The Buddhabrot is the probability distribution over the trajectories of 
# points that escape the Mandelbrot fractal.

import numpy as np
import random
import math
import matplotlib.pyplot as plt
n = 2000
m = 2000
max_val_real = (-1.5,1.5)
max_val_imag = (-1.5,1.5)
real_len = max_val_real[1]- max_val_real[0]
imag_len = max_val_imag[1]- max_val_imag[0]

box_array = np.zeros((n,m)) #n is real, m is imaginary
cnt = 10**5
iters = 50
escape_val = 2
for a in range(cnt):
    nn =random.randrange(1,n)
    mm =random.randrange(1,m)
    cr = max_val_real[0] + real_len*(nn/n)
    ci = max_val_imag[0] + imag_len*(mm/m)
    zr = 0
    zi = 0
    for x in range(iters):
        t =zr
        zr = zr**2 + cr - zi**2
        zi = 2*t*zi +ci
        if(zr**2+zi**2>escape_val):
            break
    if(x==iters-1):
        box_array[nn-1][mm-1] +=1
print(box_array)
plt.imshow(box_array, cmap='hot',extent=[*max_val_real, *max_val_imag], interpolation='nearest')
plt.colorbar(label="Cnt")
plt.show()
        
        
        

    

# print(box_array)
