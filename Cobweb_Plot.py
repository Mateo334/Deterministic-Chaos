from matplotlib import pyplot as plt
import time as t
import numpy as np
from matplotlib.animation import FuncAnimation
plt.style.use('fast')

def chaotic_Function(x):
    """Returns the function of which we need the cobweb plot"""
    r = 3.8 #Chaotic version of the Logistic map
    return r*x*(1-x)
fig = plt.figure()
ax = plt.axes(xlim=(0, 1), ylim=(0, 1)) # Setting the picture limit size of the animation
line, = ax.plot([], [], lw=1)
Frames = 5 #Number of frames to draw
def init(): # Initialization function for matplotlib animation
    line.set_data([], [])
    return line,
def animate(f): # Animation function for matplotlib animation
    xstart = f/Frames + 0.01 #Starting point of x value
    ystart = 0
    x = np.zeros(100) #Number of iterations of the cobweb line
    y = np.zeros(100)
    iterate = 0
    size = len(x)-1 
    while(1): # Iterating the cobweb plot
        for i in np.linspace(ystart, chaotic_Function(xstart), 2):
            x[iterate] = xstart
            y[iterate] = i
            iterate+=1
            if(iterate>size):break
        ystart =chaotic_Function(xstart)
        if(iterate>size):break
        xstart = chaotic_Function(xstart)
    line.set_data(x, y)
    return line,
Interval = np.linspace(0,1,50)
plt.plot(Interval,Interval, color = 'black', ls = 'dashed')
plt.plot(Interval,chaotic_Function(Interval), color = 'black')

anim = FuncAnimation(fig, animate, init_func=init, frames=Frames, interval=500, blit=False)

anim.save('Cobweb_Plot.gif', writer='Pillow')