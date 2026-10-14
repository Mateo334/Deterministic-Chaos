# This is the vectorized version of the Buddhabrot

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
iters = 200

zr = np.zeros(cnt, dtype=np.float32)
zi = np.zeros(cnt, dtype=np.float32)
cr = np.random.uniform(*max_val_real, cnt).astype(np.float32)
ci = np.random.uniform(*max_val_imag, cnt).astype(np.float32)
car = np.empty((iters, cnt, 2), dtype=np.float32)
escaped = np.zeros(cnt, dtype=bool)
active = np.ones(cnt, dtype=bool)
escape_step = np.full(cnt, iters, dtype=int)
for x in range(iters): # Iterates the steps
    t = zr[active].copy()
    zr[active] = t**2 - zi[active]**2 + cr[active]
    zi[active] = 2*t*zi[active] + ci[active]
    car[x, active, 0] = zr[active]
    car[x, active, 1] = zi[active]
    escaped_cur = active&(zr**2+zi**2>4)
    active = active&~escaped_cur
    escaped = escaped|escaped_cur
    escape_step[escaped_cur] = x + 1

car = car[:, escaped, :] #Keeps only escaped trajectories
steps = escape_step[escaped] #Number of steps it took to escape
valid = np.arange(iters)[:, None] < steps[None, :]  #Keep only trajectories up to the escape step
points = car[valid] # An n by 2 matrix of valid points
box_array, _, _ = np.histogram2d(points[:, 0],points[:, 1],bins=(n, m),range=[max_val_real, max_val_imag])

plt.imshow(np.rot90(box_array.T,1), cmap='inferno',norm=PowerNorm(gamma=0.815),extent=[*max_val_real, *max_val_imag],origin='lower', interpolation='nearest')
plt.colorbar(label="Cnt")
plt.show()