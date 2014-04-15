.. Elcodi documentation master file, created by
   sphinx-quickstart on Mon Apr  7 19:59:18 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Elcodi Documentation
====================

Hello World!
------------

`Elcodi`_ is a suite of e-commerce components developed for
`Symfony2 Framework`_.

It aims to promote `SOLID`_ principles, efficient `code reutilization`_, `separation of concerns`_ as effective building blocks for the development of e-commerce applications or components with the `Symfony PHP Framework`_

Rather than provide a single, monolithic application, the codebase is splitted in `various projects`_, each with its own subtree-splitted repositories, so that dependencies can be controlled and fine-tuned by the enveloping Symfony application utilizing Elcodi components.

Elcodi is now in an early development stage and provides a reference implementation for the basic :doc:`core components <bundles/index>` found in e-commerce web projects.

Don't worry! We have plenty of material to polish and sort out. Commits will be frequent. 


.. note::

    This documentation assumes that you have a fairly good knowledge of the 
    Symfony2 full stack framework and at least some experience with the `Symfony Standard Edition`_ distribution. 
    If you don't, please jump to the `Quick Tour`_ on the Symfony documentation repository.

Quickstart
----------

Quickly setup a working environment to test `Elcodi` bundles

.. toctree::
   :hidden:

   quickstart/index

.. include:: /quickstart/map.rst.inc

The Developer Guide
-------------------

Dive into the developer documentation to see how things work

.. toctree::
   :hidden:

   guide/index

.. include:: /guide/map.rst.inc

Bundles
-------

Documentation of all Elcodi bundles.

.. toctree::
   :hidden:
   
   bundles/index

.. include:: /bundles/map.rst.inc

The Recipes
-----------

Common problems found in the real world and their solutions

.. toctree::
   :hidden:

   recipes/index

.. include:: /recipes/map.rst.inc


Contributing
------------

A guide to contribute to Elcodi.

.. toctree::
   :hidden:

   contributing/index

.. include:: /contributing/map.rst.inc

.. _Elcodi: http://elcodi.io
.. _SOLID: http://en.wikipedia.org/wiki/SOLID_(object-oriented_design)
.. _`code reutilization`: http://en.wikipedia.org/wiki/Code_reuse
.. _`separation of concerns`: http://en.wikipedia.org/wiki/Separation_of_concerns
.. _`various projects`: https://github.com/elcodi/
.. _`Symfony PHP Framework`: http://symfony.com/
.. _`Symfony2 Framework`: http://symfony.com
.. _`Quick Tour`: http://symfony.com/doc/current/quick_tour
.. _`Symfony Standard Edition`: http://symfony.com/download
