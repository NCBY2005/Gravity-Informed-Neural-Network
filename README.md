# Gravity-Informed Neural Network

A physics-informed machine learning project that teaches a neural network to learn the inverse-square law of gravitation from simulated orbital data.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [License](#license)

## Overview
This project demonstrates how a simple neural network can learn fundamental physics laws using simulated orbital data. The network predicts the magnitude of gravitational acceleration based on the distance from the central mass, learning the inverse-square law \(a \propto 1/r^2\).

## Features
- Generate orbital data in 2D using Newton's Law of Universal Gravitation.
- Normalize and preprocess data for neural network training.
- Fully connected neural network (2 Dense layers with ReLU activations).
- Save model.
- Visualize predicted vs true acceleration.


## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/Gravity-Informed-NN.git
```

2. pip install -r requirements.txt

## Usage
1. Generate training data from:
```python
from simulate import generate_orbit_data
positions, accelerations = generate_orbit_data()
```

2. Train Neural Network from:
```python
python main.py
```

## Results
1. The simulated data is shown by: !("plots/Generated_Data.png")


where the color bar show the magnitude at corresponding x,y meters away from the center of gravity.

2. The model provided here gives the below results: !("plots/25Oct2025Result.png")

## License
MIT License

