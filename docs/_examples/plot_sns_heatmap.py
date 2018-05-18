"""
Heatmap
=========

Example heatmap
"""
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

np.random.seed(0)
sns.set()

# Data for plot
uniform_data = np.random.rand(10, 12)

# Plot heatmap
ax = sns.heatmap(uniform_data)
