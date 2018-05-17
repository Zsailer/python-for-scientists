.. _`environments`:

Virtual Environments
====================

1. `Default Conda Environment`_
2. `Creating a Python 2.7 Environment`_
3. `Creating a TensorFlow Environment`_
4. `Creating and using a Development Environment`_

.. _`Default Conda Environment`:

1. Default Conda Environment
----------------------------

Here is a graphical representation of what you have when you start out using conda:

.. image:: ../_imgs/environments_folders-1.png
  :scale: 6 %


This is your default python environment.
It uses python 3.6 and has any packages that we've installed using either the
`pip` or `conda` commands.




.. _`Creating a Python 2.7 Environment`:

2. Creating a Python 2.7 Environment
------------------------------------


This is all well and good but what if you need to use python 2.7 for a particular
application or problem?
This is an excellent opportunity to use a **virtual environment**.
Virual environments creates a new . Then, you can add packages into this new environment without affecting your main conda environment.


.. image:: ../_imgs/environments_folders-2.png
  :scale: 4 %

.. raw:: html

    <div class="terminal-window">
      <div class="terminal-text">
        > conda create -n python2 python=2.7 matplotlib pandas
      </div>
    </div>

    <div style='clear:both'></div>


The field after `-n` is the name of your environment, the `python=` flag is
where you specify your python version, and you can add package names that you
already have installed in your default miniconda.


.. raw:: html

    <div style="width=100%; margin-bottom: 40px;">
      <text style="width:40%; float:left;"><b>Switch to an environment:</b></text>
      <text style="width:40%; float:left; margin-left: 20px;"><b>Leave an environment:</b></text>
    </div>

    <div style='clear:both'></div>


.. raw:: html


    <div class="terminal-window" style="height:35px;">
      <div class="terminal-text">
        > source activate python2
      </div>
    </div>

    <div class="terminal-window" style="height:35px;">
      <div class="terminal-text">
        > source deactivate
      </div>
    </div>

    <div style='clear:both'></div>


|
|


.. _`Creating a TensorFlow Environment`:

3. Creating a TensorFlow Environment
------------------------------------


Now say that you want to install TensorFlow but you don't want to accidentally
kill your default python by installing it or you want to make sure that you can
easily uninstall it later. A virtual environment is great for this too.

::

  conda create -n Tensorflow python=3.6 numpy

Now activate the environment

::

  conda activate Tensorflow

Then install tensorflow

::

  pip install tensorflow

Now you're available environments will look like this:

.. image:: ../_imgs/environments_folders-3.png
  :scale: 8 %
  :align: left

.. _`Creating and using a Development Environment`:

4. Creating and using a Development Environment
-----------------------------------------------

One more reason that you might want a virtual environment is for developing your
own packages. Say you've got a package called test that you want to test out as
you develop it. Make a virtual environment with the packages you need and then
install your package with pip in editable mode.

::

  # Create the environment
  conda create -n Test python=3.6 pandas matplotlib

  # Activate this new environment
  conda activate Test

  # Then install your local package
  pip install -e /path/to/your/package/test

Now your available environments will include your test development environment.

.. image:: ../_imgs/environments_folders-4.png
  :scale: 8 %
  :align: left
