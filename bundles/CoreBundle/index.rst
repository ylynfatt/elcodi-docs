CoreBundle
==========

CoreBundle is the main arbiter for the Elcodi suite. It defines base interfaces and abstract classes for entities, services, factories.

It does not expose any configuration.

.. toctree::
   :maxdepth: 1

   installation
   interfaces      
   services
   configuration

Entities
--------

Entities represent the base persistable classes in Elcodi model. They are mapped using an ORM layer (doctrine) and can contain domain logic. This implementation of the model layer can theoretically suffer from the `anemic domain model`_ syndrome. However, since Elcodi provides a base infrastructure aiming for extensibility and flexibility, developers can enrich the model by extending entities and services.

Classes
~~~~~~~

Entity classes reside in the ``Entity`` directory of each bundle.


Abstract classes
~~~~~~~~~~~~~~~~

Abstract classes should reside in the ``Entity/Abstracts`` directory of each bundle.

Traits
~~~~~~

Traits should reside in the ``Entity/Traits`` directory of each bundle. They have corresponding :ref:`interfaces <core-bundle-interfaces>`. Every time a trait is added, it should be mirrored by an interface.

.. _core-bundle-interfaces:

Interfaces
~~~~~~~~~~

Interfaces reside in the ``Entity/Interfaces`` directory of each bundle.

Aiming for a good interface segregation design, fine-grained interfaces help with composing specific entity behaviors by exploiting multiple inheritance in interfaces.

For example, this is the definition of ``ProductInterface``

.. code-block:: php

	interface ProductInterface extends PurchasableInterface, ProductPriceInterface, 
			  EnabledInterface, ETaggableInterface, MetaDataInterface, ImagesContainerInterface	



.. _`anemic domain model`: http://en.wikipedia.org/wiki/Anemic_domain_model