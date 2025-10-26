"""
    This script simulates a 2D orbit around a Earth mass using Newtonian gravity.
    
    Returns:
        positions: np.ndarray of shape (steps, 2)
        accelerations: np.ndarray of shape (steps, 2)
"""
import numpy as np

def generate_data(steps=10000, dr = 1e4, dt=0.1):
    #step: number of iterations
    #stepsr: range of initial positions (in multiples of dr)
    #dr: distance increment for initial position (m)
    #dt: time step for simulation (s)
    #ADVICE: Keep range of initial positions within two magnitude 

    # Constants
    G = 6.674e-11  # Gravitational constant in m^3 kg^-1 s^-2
    M = 5.972e24  # Mass of Earth in kg

    # Initialize arrays
    positions = []
    accelerations = []

    for _ in range(steps):
        # Initial conditions 
        r = np.array([7e6 + _*dr, 0.0])      # initial position (m)
        v = np.array([0.0, 7500.0])   # initial velocity (m/s)
        sum_acc = np.array([0.0, 0.0]) # sum of accelerations
        mid_r = r.copy()

        for _ in range(50): # We don't need to run through the whole orbit, just a few steps to get acceleration data
            # Calculate gravitational acceleration
            r_mag = np.linalg.norm(r)
            a = -G * M / r_mag**3 * r

            # Update velocity and position using Euler's method
            v += a * dt
            r += v * dt
            sum_acc += a

            # Take mid position
            if _ == 24:
                mid_r = r.copy()


        # # Record position and acceleration
        positions.append(mid_r)
        accelerations.append(sum_acc / 50)  # average acceleration over the steps

    return np.array(positions), np.array(accelerations)

if __name__ == "__main__":
    # Example: generate and save data
    pos, acc = generate_data()
    np.savez("orbit_data.npz", positions=pos, accelerations=acc)
    print("Data saved to orbit_data.npz")