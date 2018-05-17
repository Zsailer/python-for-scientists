"""
Line Chart
=========

Example bar chart.
"""
import matplotlib.pyplot as plt
import seaborn as sns

# Initialize a figure and axes object
fig, ax = plt.subplots(figsize=(3,3))

# Data
x = [0, 1, 2, 3, 4, 5, 6]
y = [5, 3, 2, 1.5, 1, 0.5, 0.4]

# Add data as scatter points onto axes
ax.plot(x, y)

# Name axes
ax.set_xlabel('x')
ax.set_ylabel('y')

# Show figure.
fig.show()
