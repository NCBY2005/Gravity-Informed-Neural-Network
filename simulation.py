"""
    This script simulates a 2D orbit around a Earth mass using Newtonian gravity.
    
    Returns:
        positions: np.ndarray of shape (steps, 2)
        accelerations: np.ndarray of shape (steps, 2)
"""
import numpy as np

def generate_data(steps=100000,dt=0.1):

    # Constants
    G = 6.674e-11  # Gravitational constant in m^3 kg^-1 s^-2
    M = 5.972e24  # Mass of Earth in kg

    # Initial conditions 
    r = np.array([7e6, 0.0])      # initial position (m)
    v = np.array([0.0, 7500.0])   # initial velocity (m/s)

    positions = []
    accelerations = []

    for _ in range(steps):
        # Calculate gravitational acceleration
        r_mag = np.linalg.norm(r)
        a = -G * M / r_mag**3 * r

        # Record position and acceleration
        positions.append(r.copy())
        accelerations.append(a.copy())

        # Update velocity and position using Euler's method
        v += a * dt
        r += v * dt

    return np.array(positions), np.array(accelerations)

if __name__ == "__main__":
    # Example: generate and save data
    pos, acc = generate_data()
    np.savez("orbit_data.npz", positions=pos, accelerations=acc)
    print("Data saved to orbit_data.npz")