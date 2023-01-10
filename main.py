#%%

import matplotlib.pyplot as plt
import math

from src.diagram_type import DiagramType
from src.grid_block import GridBlock

# Diagram Dimentions
a = 0.5
b = 2
c = 3

# Grid size
y_max = 100
x_max = 100

grid_squares = 10
square_size = x_max/grid_squares
low_percentage = 0
high_percentage = 100
target = 0
max_distance = 0

def get_raw_y(x, diagram_type = DiagramType.Default):
    if (diagram_type == DiagramType.Default):
        return x*(math.sqrt(2)) # Diagonal Line
    elif (diagram_type == DiagramType.Curve):
        return (a * x**2) + (b * x) + c # ? Curve suggested by GPT
        
    else:
        raise ValueError(f"Diagram type of [{diagram_type}] have not been implimented yet")    
    
    ## Mass Enery Relationship y=m*(c**2)
    # return a*(x**2)    
    
    ## Exponential [y=a.e**(b*x)]
    # return a*(c**(b*x))
    
    ## General power-law function [y=a*(b**x)]
    # return a*(b**x)   
    
def get_y(x, diagram_type = DiagramType.Default):        
    y_highest = get_raw_y(x_max, diagram_type)        
    return (get_raw_y(x, diagram_type)/y_highest)*100

def display_diagram(diagram_type = DiagramType.Default):
    x = range(x_max)
    y = [get_y(i, diagram_type) for i in x]

    plt.plot(x, y)
    plt.show()
    
def create_matrix():
    count = 1    
    x_distance = 0
    matrix = [[None for x in range(grid_squares)] for y in range(grid_squares)] 
    
    for i in range(grid_squares):
        y_distance = 0     
        
        for n in range(grid_squares):
            distance = x_distance + y_distance
            grid_block = GridBlock((i*square_size)+1, (i+1)*square_size, (n*square_size)+1, (n+1)*square_size, distance)
            
            print(f'[{count} - x({grid_block.x_min}-{grid_block.x_max}) y({grid_block.y_min}-{grid_block.y_max}) d={grid_block.distance}] ')
            matrix[i][n] = grid_block
            
            count += 1
            y_distance += 1
            
            # Largest distance in set (upper boundry)
            if (distance > max_distance):
                max_distance = distance
        
        x_distance += 1   
       

    
def get_percentage(x, y):    
    # get grid position
    # get grid percentage adjusted by distance form the curve
    pass
        
    
display_diagram(DiagramType.Default)
matrix = create_matrix()



    
    












'''

import matplotlib.pyplot as plt

a = 0.5
b = 1
c = 2

y_max = 100
x_max = 100
y_highest = None

def get_raw_y_curve(x):
    return (a * x**2) + (b * x) + c

def get_y_curve(x):        
    y_highest = get_raw_y_curve(x_max)        
    return (get_raw_y_curve(x)/y_highest)*100

x = range(x_max)
y = [get_y_curve(i) for i in x]

plt.plot(x, y)
plt.show()
'''

'''

x = range(0, 100)
y = range(0, 100)

a = 8
b = 9
c = 10

curve = [(a * x**2) + (b * x) + c for x in x]

plt.plot(x, curve)

plt.show()
'''

'''

import matplotlib.pyplot as plt

# Define the variables that will determine the shape of the curve
a = 7
b = 3
c = 9

# Generate the x values for the curve
x = range(0, 100)

# Calculate the y values for the curve using the variables and x values
y = [a*x_val**2 + b*x_val + c for x_val in x]

#plt.xlim(0, 1000)
#plt.ylim(0, 20000)

# Plot the curve
plt.plot(x, y)

# Add labels and title to the plot
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Curve Plot')

# Show the plot
plt.show()

'''

'''

import numpy as np
import matplotlib.pyplot as plt

# Set the range of the curve
start = 0
stop = 10

# Generate the x and y values for the curve
x = np.linspace(start, stop, 100)
y = np.exp(x)

# Create the plot
fig, ax = plt.subplots()
ax.plot(x, y)

# Set the plot limits
ax.set_xlim(start, stop)
ax.set_ylim(0, np.exp(stop))

# Show the plot
plt.show()

'''
'''
# Powers of 10
a = [10**i for i in range(15)]
# Plotting the graph
plt.plot(a, color='blue', lw=2)
# Setting a logarithmic scale for y-axis
plt.yscale('log')
plt.show()
'''

'''
x=np.arange(0,10,0.3)
y= np.exp(x)
plt.scatter(x,y)
plt.rcParams.update({'figure.figsize':(10,8), 'figure.dpi':100})
plt.title('Exponential Relation dataset')
plt.show()

'''



# %%
