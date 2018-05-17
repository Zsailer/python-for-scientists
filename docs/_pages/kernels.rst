Environments and Kernels
========================

Setting up a new virtual environment using ``conda``
----------------------------------------------------

::

   conda create -n myenv python=3 package-name1 package-name2

   # To activate or enter your new virtual environment
   source activate myenv

   # And to leave your virtual environment
   source deactivate myenv

As an example I want to make an environment called "master-blaster" that uses
python 3.6 and has ``numpy``, ``pandas``, and ``matplotlib`` preinstalled::

   conda create -n master-blaster python=3.6 numpy pandas matplotlib ipykernel

Why did I add ``ipykernel`` to
:ref:`Why all the negativity around Matplotlib? <faq matplotlib>`the package list? That's so we can make an
ipython kernel in the next step!

Making an ipython kernel
------------------------

::

   source activate master-blaster
   python -m ipykernel install --user --name master-blaster --display-name "Python 3 (master-blaster)"


Now this kernel can be used in a Jupyter notebook without having to activate the
associated virtual environment.

What is a virtual environment?
------------------------------
A virtual environment is a self-contained version of Python and specified
packages. When you switch to a different virtual environment conda points to
that python installation and installed packages. A package installed globally
but not in that virtual environment won't show up.

What is a kernel?
-----------------
A kernel is the engine that actually runs your code. Using Jupyter you can have
a kernel for each virtual environment and even kernels for languages other than
Python.

Why would you want a virtual environment?
-----------------------------------------
Virtual environments are a good way to protect yourself. Say you accidentally
install or delete something, if you're in a virtual environment you can delete
it and start over without reinstalling Python.
