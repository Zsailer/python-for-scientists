"""
Histogram
=========

Example histogram
"""
import numpy as np
import pandas as pd

# Generate random normal data
x = np.random.normal(0, 0.1, 1000)
    

# Convert to pandas DataFrame
df = pd.DataFrame({
    'x': x
    })

# Plot histogram
hist = df.hist(bins=50)
