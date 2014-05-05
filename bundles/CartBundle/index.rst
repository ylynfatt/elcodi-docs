CartBundle
==========

The cart bundle is the base component that holds all the domain logic for creating and storing Orders and Carts.

``Order`` and ``Cart`` entities share a common ``Price`` trait, which is used to define the basic amounts that an order should have.

In reality, an ``Order`` can be see as a persisted snapshot of a ``Cart`` in a certain moment, whose only mutable attribute is its current ``status``. See the `statuses`_ section in :doc:`order` documentation for more details about statuses.

A ``Cart`` on the other hand, is a mutable and changable entity. At any time more products can be added or removed from it until it is converted to an ``Order``. A Cart is stored to the persistence layer the first time a ``cart.onload`` event is fired. 

.. image:: cartbundle-classdiagram.svg

.. image:: cartbundle-historyclassdiagram.svg

.. toctree::
   :maxdepth: 1
   :numbered:

   installation   
   cart
   order
   services
   configuration