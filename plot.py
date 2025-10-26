"""
    This script plots the 2D orbit around a Earth mass using Newtonian gravity and
    the 
    
"""

#import libraries

import numpy as np
import matplotlib.pyplot as plt
from simulation import generate_data

#Generate data from simulation
position, acceleration = generate_data()
r_mag = np.linalg.norm(position, axis=1).reshape(-1,1)
a_mag = np.linalg.norm(acceleration, axis=1).reshape(-1,1)

#Plot the acceleration magnitude with respect to position
'''This plot is taken with the below settings:
a. Run over steps for both loops in simulation.py
b. steps*1050 in the inner loop 
c. Takes r and a instead of mid_r and avg_a
d. dt = 0.1
'''
# plt.figure(figsize=(10,8))
# scatter = plt.scatter(position[:,0], position[:,1], c=np.linalg.norm(acceleration, axis=1), cmap='viridis', s=1)
# plt.colorbar(scatter, label='Acceleration Magnitude (m/s²)')
# plt.xlabel('x (m) from center of Mass')
# plt.ylabel('y (m) from center of Mass')
# plt.title('Magnitude of Acceleration w.r.t Position away from Center of Earth Mass')
# plt.show()

plt.figure(figsize=(4,4))
plt.plot(r_mag, a_mag, '.', markersize=1)
plt.xlabel('Distance from center of Mass (m)')
plt.ylabel('Acceleration Magnitude (m/s²)')
plt.title('Acceleration as a function of Distance from Center of Earth Mass')
plt.show()