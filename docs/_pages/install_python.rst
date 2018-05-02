Setting up Scientific Python
============================

1. `Install Python using Miniconda`_
2. `Install Jupyter Notebooks`_
3. `Install key scientific packages`_
4. `Run you first Jupyter Notebook.`_

.. _`Install Python using Miniconda`:

1. Install Python using Miniconda
---------------------------------

.. image:: ../../_imgs/miniconda.png
  :scale: 10%
  :align: right

We recommend Miniconda_ (`even if you have Python already installed`_).

.. _Miniconda: https://conda.io/miniconda.html

Miniconda comes with Python and the Conda_ package manager. Installers_ exist
for Windows, Mac, and Linux. Download the installer that matches your operating
system and follow the directions to install on your computer.

Miniconda keeps everything contained in a single folder. If anything ever goes
wrong, you can always remove this folder and start over.

.. _Conda: https://conda.io/docs/
.. _Installers: https://conda.io/miniconda.html

Conda will be your main tool for installing Python packages. It installs
packages through a mechanism known as *conda-recipes*. (It's important to
note, it can do `many other`_ things as well.) Conda also manages package updates and creates virtual environments.

To use conda, call ``conda install some_package_name``. We'll use this command to install **pip**.

.. code-block:: bash

  conda install pip


*pip* is another tool for installing Python packages. If a conda-recipe does not exist for a package you are trying to install, you should trying installing using pip.


.. code-block:: bash

  pip install ..


.. _`Install Jupyter Notebooks`:

2. Install Jupyter Notebooks.
-----------------------------

Using our *conda* tool, install the Jupyter Notebook.


.. image:: ../../_imgs/notebook.png
  :scale: 25%
  :align: right

.. code-block:: bash

  conda install notebook



.. _`Install key scientific packages`:

3. Install key scientific packages
----------------------------------

Before we starting using the Jupyter notebooks, we likely want Python's plotting library, Matplotlib, and key scientific programming packages like Numpy and SciPy. For more scientific packages, see this list_.

.. code-block:: bash

  conda install numpy scipy matplotlib


.. _list: ../package_list

.. _`Run you first Jupyter Notebook.`:

4. Run you first Jupyter Notebook.
----------------------------------

Run you first Jupyter notebook

.. _`even if you have Python already installed`:


FAQ questions
-------------

**What if my operating system already comes with Python installed?**

It's best not to mess with the native Python on your machine. On Macs, for example, many programs depend on that native Python. If you break it, you can break your Mac.

**What is the difference between ``conda`` and ``pip``?**

Miniconda installs and manages Python (and it's packages) in a single folder on your computer. It's lightweight and easy to use. If anything goes wrong, you can always startover by uninstalling and reinstalling Miniconda. It's safe!

Download the install script from here_


.. _here
