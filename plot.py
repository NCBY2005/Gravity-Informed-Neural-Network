"""
    This script plots the 2D orbit around a Earth mass using Newtonian gravity and
    the 
    
"""

#import libraries

import numpy as np
import matplotlib.pyplot as plt
from simulation import generate_data

#Generate data from simulation
position, acceleration = generate_data(steps=100000)
r_mag = np.linalg.norm(position, axis=1).reshape(-1,1)
a_mag = np.linalg.norm(acceleration, axis=1).reshape(-1,1)

#Plot the orbit
plt.figure(figsize=(5,4))
scatter = plt.scatter(position[:,0], position[:,1], c=np.linalg.norm(acceleration, axis=1), cmap='viridis', s=1)
plt.colorbar(scatter, label='Acceleration Magnitude (m/s²)')
plt.xlabel('x (m) from center of Mass')
plt.ylabel('y (m) from center of Mass')
plt.title('Data Generated from 2D Orbit Simulation')
plt.show()