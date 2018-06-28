"""
Line Plot
=========

Example line plot
"""
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set()

# Initialize a figure and axes object
fig, ax = plt.subplots(figsize=(3,3))

# Data
x = np.linspace(0,100,100)
y = np.linspace(0,100,100)

# Add data a scatter points onto axes
ax.plot(x, y)

# Name axes
ax.set_xlabel('x');
ax.set_ylabel('y');
