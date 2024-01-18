========================================
Welcome to Carnival Automated tests!
========================================

Here you are going to be testing the user story #1 and #2.

First, let's create a venv

.. code::

    python3 -m venv venv
    source venv/bin/activate

Let's update pip

.. code::

    pip install -U pip

Now, let's install the libraries we will be using

.. code::

    pip install -r requirements.txt

Now, let's run the tests

.. code::

    pytest -vvs --random-order tests

Enjoy :D