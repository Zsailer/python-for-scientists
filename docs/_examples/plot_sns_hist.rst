.. _sphx_glr__examples_plot_sns_hist.py:


Histogram
=============

Example histogram




.. image:: /_examples/images/sphx_glr_plot_sns_hist_001.png
    :align: center





.. code-block:: python

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

