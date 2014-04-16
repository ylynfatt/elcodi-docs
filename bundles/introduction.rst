Introduction
============

Elcodi bundle structure in generally straightforward and complies with Symfony `best practices`_.

You might want to read the section :doc:`/guide/bundle_structure` for a brief overview.

.. _dependencyinjection:

DependencyInjection
-------------------

Core Elcodi bundle extension classes usually extend ``AbstractExtension`` and implement the ``EntitiesOverridableExtensionInterface`` interface.
This class hierarchy helps with project parameter definition and :ref:`entity override <entity-override>`.

A typical extension class, such as `ElcodiCartExtension`_, will override these methods:

``getConfigFiles``

``getParametrizationValues``

``getEntitiesOverrides``


Let's stick with ``ElcodiCartExtension`` and look at the code (for the sake of readability some methods were removed):

.. code-block:: php
		
	

    /**
     * Config files to load
     *
     * @return array Config files
     */
    public function getConfigFiles()
    {
        return [
            'classes',
            'eventListeners',
            'services',
            'factories',
        ];
    }

``getConfigFiles`` just return a list of configuration files. By putting them here, you won't need to manually load them using a ``FileLoader`` in your extension ``load`` method. Currently only ``yml`` files are supported.

The configuration file directory can be specified by returning it, as a ``string``, from the ``getConfigFilesLocation`` method.

.. code-block:: php

    /**
     * Load Parametrization definition
     *
     * return array(
     *      'parameter1' => $config['parameter1'],
     *      'parameter2' => $config['parameter2'],
     *      ...
     * );
     *
     * @param array $config Bundles config values
     *
     * @return array Parametrization values
     */
    protected function getParametrizationValues(array $config)
    {
        return [
            'elcodi.core.cart.order_states' => $config['order']['states'],
            'elcodi.core.cart.order_initial_state' => $config['order']['initial_state']
        ];
    }

``getParametrizationValues`` is used to instruct the Extension to copy the specified configuration values to container parameters.


.. code-block:: php

    /**
     * Get entities overrides.
     *
     * Result must be an array with:
     * index: Original Interface
     * value: Parameter where class is defined.
     *
     * @return array Overrides definition
     */
    public function getEntitiesOverrides()
    {
        return [
            'Elcodi\CartBundle\Entity\Interfaces\CartInterface' => 'elcodi.core.cart.entity.cart.class',
            'Elcodi\CartBundle\Entity\Interfaces\OrderInterface' => 'elcodi.core.cart.entity.order.class',
            'Elcodi\CartBundle\Entity\Interfaces\CartLineInterface' => 'elcodi.core.cart.entity.cart_line.class',
            'Elcodi\CartBundle\Entity\Interfaces\OrderLineInterface' => 'elcodi.core.cart.entity.order_line.class',
            'Elcodi\CartBundle\Entity\Interfaces\OrderHistoryInterface' => 'elcodi.core.cart.entity.order_history.class',
            'Elcodi\CartBundle\Entity\Interfaces\OrderLineHistoryInterface' => 'elcodi.core.cart.entity.order_line_history.class',
        ];
    }
	

``getEntitiesOverrides`` maps a class, usually an ``Interface`` to a container parameter who represent another class. This is used for configuring the ``ResolveTargetEntityListener`` doctrine listener and can be used to `override doctrine relationships`_.


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
.. _`override doctrine relationships`: http://symfony.com/doc/current/cookbook/doctrine/resolve_target_entity.html
