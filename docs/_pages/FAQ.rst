Frequently Asked Questions
==========================


How do I upgrade a python package that is already installed?
------------------------------------------------------------

Sometimes you need to upgrade to a new version of a package that is already installed in your python environment.

To upgrade a package in your python environment, just use conda! For example, to upgrade the scipy package library run the following:

::

    conda update scipy

.. _`Should I install Python 2 or 3`:

Should I install Python 2 or 3?
-------------------------------

Python 3. Most scientific Python libraries now support Python 3 and it's a better language overall. Do not install Python 2 unless you absolutely must use it for some core dependency in your daily work.

.. _faq1:

What if my operating system already comes with Python installed?
----------------------------------------------------------------

It's best not to mess with the native Python on your machine. On Macs, many programs depend on that native Python. If you break it, you can break your Mac.

What is the difference between conda and pip?
---------------------------------------------

**conda**--- is command line tool that downloads conda-recipes from a repository hosted by `Continuum Analytics`_. One strength is that conda-recipes can be written for any programming language (not just Python). This is extremely useful for projects like Jupyter who weave Javascript tools with Python backends. Conda is quickly becoming a widely used installer for this reason. Further, developers at Continuum are working out ways to make **pip** and **conda** work together seamlessly.

.. _`Continuum Analytics`: https://www.anaconda.com/

**pip**--- a command line tool that downloads Python packages from PyPI, Python's Packaging Index. It is designed to manage Python packages only.

conda is a younger than pip, so many Python packages don't have conda-recipes but exist on PyPI.

.. _`why do I need to to launch Jupyter from a command line`:

Why do I need to launch Jupyter from the command line?
------------------------------------------------------

The answer is a bit complicated. Jupyter is web application frontend (written in Javascript) that executes code from a Python server backend. The command line is used to launch the server backend and open internet ports for the frontend. This frontend is rendered using a browser (like Google Chrome or Firefox). The command line interface makes this process transparent. You see the server start, then a browser window opens. The command line also provides flexibility for advanced users.

If you'd like a Jupyter-like Desktop application, it exists. It's called **nteract**. You can open Jupyter notebooks without the command-line. `It can be found here`_!

.. _`It can be found here`: https://nteract.io/


.. _`faq matplotlib`:

Why is Matplotlib a source of friction among computational scientists?
----------------------------------------------------------------------
