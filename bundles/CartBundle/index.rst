CartBundle
==========

The cart bundle is the base component that holds all the domain logic for creating and storing Orders and Carts.

A ``Cart`` represents the transitient state of a purchase before it is committed.  It is a mutable and changable entity. At any time more products can be added or removed from it until it is converted to an ``Order``. 

An ``Order`` can be see as a persisted snapshot of a ``Cart`` in a certain moment, whose only mutable attribute is its current ``state``. See the :ref:`states <order-states>` section in :doc:`order` documentation for more details about statuses.

A rich set of events was designed so that every significant transition or CRUD event occurring within collaborating objects can be hooked by customizable logic.

.. toctree::
   :maxdepth: 1

   installation   
   cart
   order
   services
   configuration
