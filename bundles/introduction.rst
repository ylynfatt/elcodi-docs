Introduction
============

Elcodi bundle structure in generally straightforward and complies with Symfony `best practices`_.

There are a few directories worth to taking a look:

DependencyInjection
-------------------

Core Elcodi bundle extension class usually extend ``AbstractExtension`` and implement the ``EntitiesOverridableExtensionInterface`` interface.
This class hierarchy helps with project parameter definition and :ref:`entity override <entity-override>`.

A typical extension class, such as `ElcodiCartExtension`_, will override these methods:

``getConfigFiles``

``getParametrizationValues``

``getEntitiesOverrides``


Events
------

Factory
-------

Resources
---------


Using individual bundles
------------------------ 


.. _`best practices`: http://symfony.com/doc/current/cookbook/bundles/best_practices.html
.. _`ElcodiCartExtension`: https://github.com/elcodi/elcodi/blob/master/src/Elcodi/CartBundle/DependencyInjection/ElcodiCartExtension.php
