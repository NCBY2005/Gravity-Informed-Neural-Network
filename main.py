"""
    This script prepares data and trains the physics-informed neural network (PINN)

    Versions:
    1.0 - Oct 25 2025: Initial version (Nicholas)

"""

#import libraries
from simulation import generate_data
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

"""
   ======================================================================================================================
    ## Fetch & Prepare Data
   ======================================================================================================================
"""

#Generate data from simulation
position, acceleration = generate_data()

#Compute magnitudes
r_mag = np.linalg.norm(position, axis=1).reshape(-1,1)
a_mag = np.linalg.norm(acceleration, axis=1).reshape(-1,1)

#Normalize data
r_mag_norm = r_mag / np.max(r_mag)
a_mag_norm = a_mag / np.max(a_mag)

#Train-test split
r_train, r_test, a_train, a_test = train_test_split(r_mag_norm, a_mag_norm, test_size=0.2, random_state=22)

"""
   ======================================================================================================================
    ## Define Model
   ======================================================================================================================
"""

model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1)
])
model.compile(optimizer='adam', loss='mse')

"""
   ======================================================================================================================
    ## Train Model
   ======================================================================================================================
"""

model.fit(r_train, a_train, epochs=100, batch_size=32, validation_data=(r_test, a_test), verbose=0)
model.save("Gravity_Informed_NN_Model_25Oct2025.keras")

"""
   ======================================================================================================================
    ## Evaluate and Plot Results
   ======================================================================================================================
"""

r_test_sorted = np.sort(r_test.flatten())
a_pred = model.predict(r_test_sorted)

plt.scatter(r_test, a_test, label='True', s=10)
plt.plot(r_test_sorted, a_pred, 'r', label='Predicted')
plt.xlabel('Normalized distance r')
plt.ylabel('Normalized acceleration |a|')
plt.legend()
plt.title('Neural Network Learning the Inverse-Square Law')
plt.show()