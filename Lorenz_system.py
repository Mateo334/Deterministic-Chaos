import numpy as np
import math
import matplotlib.pyplot as plt
starting_point_a, starting_point_b = [0.1,0.5,0.1],[0.1,0.51,0.1] # Two starting points close to orbit
def Lorenz_sys(points, sigma, rho, beta):
    """Returns the equations of the Lorenz system"""
    x, y, z = points
    return np.array([sigma*(y-x), x*(rho -z)-y, x*y-beta*z])
def Rossler_sys(points, sigma, rho, beta):
    """Returns the equations of the Rossler system"""
    x, y, z = points
    return np.array([-(y+z), x+ sigma*y, rho+z*(x-beta)])
dt = 0.01 #Timestamp
def Iterate(start_Point,type, timer):
    """Iterates the system. a is the starting point, type is either Rossler, or Lorenz, and timer is the number of iterations.
    """
    point = start_Point
    data = []
    match type:
        case "Lorenz":
            f = Lorenz_sys
            rho, beta, sigma = 28,  8/3, 10 #values for a chaotic version of the Lorenz system
        case "Rossler":
            f = Rossler_sys
            rho,sigma, beta = 0.2,  0.2, 5.7 #values for a chaotic version of the Rossler system
    for t in np.linspace(0.001, 1, timer):
        point += f(point, sigma, rho, beta)*dt
        data.append([point[0],point[1],point[2]])
    return data   

def Iterate_double(point_a,point_b, type, timer): # Useful for showing sensitive dependence on initial conditions
    """Iterates the system at two points a, b. type is either Rossler, or Lorenz, and timer is the number of iterations.
    """
    points_a, points_b = point_a,point_b
    data_a = []
    data_b = []
    match type:
        case "Lorenz":
            f = Lorenz_sys
            rho, beta, sigma = 16,  8/3, 10 #values for Lorenz system
        case "Rossler":
            f = Rossler_sys
            rho,sigma, beta = 0.2,  0.2, 5.7 #values for Rossler system
    for t in np.linspace(0.001, 1, timer):
        points_a += f(points_a, sigma, rho, beta)*dt
        points_b += f(points_b, sigma, rho, beta)*dt
        data_a.append([points_a[0],points_a[1],points_a[2]])
        data_b.append([points_b[0],points_b[1],points_b[2]])
    return data_a, data_b

def Plotting_sys(iters):
    """Plots the first iterations of a given system
    """
    data_a, data_b = Iterate_double(starting_point_a,starting_point_b, "Lorenz", iters)
    ax = plt.figure().add_subplot(projection='3d')
    data_a = np.array(data_a)
    data_b = np.array(data_b)
    ax.plot(*data_a.T, lw=0.8, label = "point A")
    ax.plot(*data_b.T, lw=0.8, label = "point B")
    plt.tight_layout()
    plt.legend()
    plt.show()
# Plotting_sys(iters = 5000)
def Plotting_single(iters):
    """Plots the first iterations of a given system
    """
    data_a = Iterate(starting_point_a, "Lorenz", iters)
    ax = plt.figure().add_subplot(projection='3d')
    data_a = np.array(data_a)
    ax.plot(*data_a.T, lw=0.8, label = "point A")
    plt.tight_layout()
    plt.legend()
    plt.show()
Plotting_single(iters = 5000)


def largest_Lyap(n, rho, beta, sigma, Plot):
    """Calculates the Largest Lyapunov exponent of the Lorenz system. n is the number of iterations - the more, the better precision. 
    """
    dists = np.zeros(n) # This is our list of distances between points
    point_1 = [0,0.2,0.1]# Initialization
    for i in range(400): #Iterating, until the point is on the Attractor
        point_1+=Lorenz_sys(point_1, sigma, rho, beta)*dt
    point_2 = np.array(point_1)+ np.array([0,0,0.00001]) # Setting the second point
    init_dist = math.dist(point_1, point_2)
    def Readjust(point_to_adjust, secondpoint,  init): # Moving one point closer to the other on a straight line using Sprott's method
        return np.array(secondpoint) + init*(np.array(point_to_adjust)-np.array(secondpoint))/math.dist(secondpoint, point_to_adjust)
    for i in range(n):
        point_1 += Lorenz_sys(point_1, sigma, rho, beta)*dt #transformation
        point_2 += Lorenz_sys(point_2, sigma, rho, beta)*dt
        dists[i] = (math.dist(point_1, point_2)) 
        point_2 = Readjust(point_2, point_1, init_dist) # Moving the points
    if(Plot): # If we want to plot the list of distances
        plt.plot(dists)
        plt.show()
    dists = np.log(dists/init_dist)
    print("Lyapunov exponent: ", (sum(dists))/len(dists)/dt)
    print("Initial distance: ", init_dist)
# largest_Lyap(2000,28,  8/3, 10, False)