import numpy as np
import matplotlib.pyplot as plt
def Menger_Sponge(matrix, size):
    """Returns the Menger Sponge variation of a given matrix."""
    quotient, remainder = divmod(size, 3)
    if remainder == 0: # If size argument is a multiple of 3 / need to delete points
        for x in np.arange(0, size, quotient):
            for y in np.arange(0, size, quotient):
                for z in np.arange(0, size, quotient):
                    slice = matrix[x:x + quotient, y:y + quotient, z:z + quotient] # Gathering the current part of the matrix
                    if ((x // quotient) % 3 == 1 and (y // quotient) % 3 == 1 ): # If at least two coords are mod 3 equal to 1 / delete point
                        slice *= 0
                    if ((x // quotient) % 3 == 1 and (z // quotient) % 3 == 1 ):
                        slice *= 0
                    if ((y // quotient) % 3 == 1 and (z // quotient) % 3 == 1 ):
                        slice *= 0
                    Menger_Sponge(slice, quotient)

size = 9 # Number of side points / Has to be multiple of 3
matrix = np.ones((size, size,size))
Menger_Sponge(matrix, size)

def Plot_html():
    """Plotting the matrix of points using plotly as .html file."""
    import plotly.graph_objects as go
    my_data = np.where(matrix==1) # Fixing only the leftover points
    marker_data = go.Scatter3d(
        x=my_data[0], 
        y=my_data[1], 
        z=my_data[2], 
        marker=go.scatter3d.Marker(size=5, symbol='square'), 
        opacity=0.8, 
        mode='markers'
    )
    fig=go.Figure(data=marker_data)
    fig.write_html('Menger_Sponge.html', auto_open=False)
Num_of_points = len(sum(np.where(matrix==1))) #Summing all points drawn
print("Number of drawn points: ",  Num_of_points)
print("Shape of matrix: ", matrix.shape)
print("Number of points in normal matrix: ", matrix.size)
Plot_html() 