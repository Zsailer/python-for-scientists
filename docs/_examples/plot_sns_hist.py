"""
Histogram
=============

Example histogram
"""
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set()


# Initialize a figure and axes object
fig, ax = plt.subplots(figsize=(3,3))

# Data
x = np.random.normal(0, 0.1, 1000)

# Add data a scatter points onto axes
ax.hist(x)

# Name axes
ax.set_xlabel('x')

# Show figure.
fig.show()
