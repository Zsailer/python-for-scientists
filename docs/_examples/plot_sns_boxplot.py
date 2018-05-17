"""
Bar Chart
=========

Example bar chart.
"""

import seaborn as sns
import numpy as np

sns.set()

# Generate data
a = np.random.normal(0, 0.1, 1000)
b = np.random.normal(1, 0.1, 1000)

# Generate a boxplot
ax = sns.boxplot(data=(a,b))

# Name axes
ax.set_xlabel('Category')
ax.set_ylabel('Measurement')
