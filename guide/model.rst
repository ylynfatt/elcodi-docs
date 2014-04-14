Model
=====

Model definition is self contained in a single bundle. 

Ideally its definition should adhere to the domain modeling, leaving out dependencies that are not at the very core of the domain.

The proposed structure of the bundles can be summarized with:

* Entities must implement interfaces with significant methods
* ORM Model definition through yml files. (Avoid use of annotation due to metadata coupling with class definitions)
* ORM association mapping must use ``Interfaces`` as ``targetEntity``
* Factories should be used in order to create object in a consistent state

Base model hierarchy
--------------------

* ``Abstracts``
* ``Interfaces``
* ``Traits``

.. _entity-override:

Entity override
---------------

