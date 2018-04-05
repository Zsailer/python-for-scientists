Things you need to know
=======================

pip
---

``pip`` is Python's recommended way of installing Python Packages. It is
a command line tool that easily pulls packages from PyPI, Python's Packaging Index.
Python's key scientific packages live on PyPI.

For example, you can install Jupyter Notebooks by typing this on the command line.

.. code-block::

  pip install jupyter


conda
-----

Miniconda comes with it's own mechanism for installing Python packages. It's
similar to ``pip``. Just replace it with conda

.. code-block::

  conda install jupyter

My honest opinion... I find ``conda`` packages often lag behind their PyPI counterparts. Thus,
recommend always trying ``pip install`` first.
