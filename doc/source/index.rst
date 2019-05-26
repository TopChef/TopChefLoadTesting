.. TopChef Load Testing documentation master file, created by
   sphinx-quickstart on Wed Jan 10 12:36:26 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to TopChef Load Testing's documentation!
================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


LocustFile
----------

The purpose of the locustfile is to describe locusts. A locust is an object
containing a set of tasks that need to be performed. Each locust corresponds
to a single TopChef user. :mod:`locust` is then responsible for creating
instances of each locust and running tests en masse to gauge response times.

Task Sets
---------

.. automodule:: task_sets
   :members:
   :undoc-members:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
