import numpy as np
import math
import matplotlib.pyplot as plt
from numba import njit, jit
import time as t
timestart = t.time()
@jit
def calculation_index(x,y):
    a = complex(0,0)
    c = complex(x,y)
    for i in range(100):
        # a = a**2 + c
        a = a**15 + c
        if(abs(a)> 2):
            return i   
    return 100  
with open('output.txt', 'w') as f:
    for x in np.linspace(-1,1,1000):
        for y in np.linspace(-2,2, 1000):
            f.write(str(f"{x:.3f}" + " ")+str(f"{y:.3f}"+ " ")+str(f"{calculation_index(x,y):.1f}")+str("\n"))
    
print(t.time() - timestart)
# print("pomoc")