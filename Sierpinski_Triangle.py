from matplotlib import pyplot as plt
import math
import random
def is_Inside_Triangle(A, B, C, P):
    """Checking whether a point is inside a given triangle."""
    denominator = ((B[1] - C[1]) * (A[0] - C[0]) +
                   (C[0] - B[0]) * (A[1] - C[1]))
    a = ((B[1] - C[1]) * (P[0] - C[0]) +
         (C[0] - B[0]) * (P[1] - C[1])) / denominator
    b = ((C[1] - A[1]) * (P[0] - C[0]) +
         (A[0] - C[0]) * (P[1] - C[1])) / denominator
    c = 1 - a - b
    if a >= 0 and b >= 0 and c >= 0:
        return True
    else:
        return False

# Setting the corner points
A = (0, 0)
B = (1, 0)
C = (0.5, math.sqrt(3)/2)


def Sierpinski_triangle():
    """Gathering points based on the Chaos game modification for the Sierpinski Triangle."""
    import time as tr
    x = []
    y = []
    x.append(0); x.append(1); x.append(0.5)
    y.append(0); y.append(0); y.append(0.8)
    plt.scatter(x,y, s =5)
    while(1):
            new_point = [0.5+ random.uniform(-1,1),0.4+random.uniform(-1,1)] # Finding the new point location
            if(is_Inside_Triangle(A,B,C,new_point)):break
    abs_start = tr.time()
    while(1):
        starting_t = tr.time()
        t = random.randint(0,2)
        new_point = [(new_point[0]+x[t])/2, (new_point[1]+y[t])/2]
        x.append(new_point[0])
        y.append(new_point[1])
        if(starting_t - abs_start > 0.3): print(len(x)); break # Gathering only to a given time stop
    return x, y
x, y = Sierpinski_triangle()
import plotly.express as px
import plotly.io as pio
pio.renderers.default = "browser"
fig = px.scatter(x=x, y=y)
fig.update_traces(marker={'size': 0.1})
fig.write_html('Sierpinski_Triangle.html', auto_open=False)