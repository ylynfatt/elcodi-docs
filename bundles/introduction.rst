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

``getConfigFiles`` just returns a list of configuration files. By putting them here, you won't need to manually load them using a ``FileLoader`` in your extension ``load`` method. Currently only ``yml`` files are supported.

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
    

``getEntitiesOverrides`` maps a class, usually an ``Interface`` to a container parameter who represents another class. This is used for configuring the ``ResolveTargetEntityListener`` doctrine listener and can be used to `override doctrine relationships`_.


.. _bundle-events:

Events
------

Generally each bundle defines a sets of ``events`` that will be emitted when certain conditions occur. 

As you know, the `Symfony Event Dispatcher`_ uses the :method:`Symfony\\Component\\EventDispatcher\\EventDispatcher::dispatch` method to notify observers for a given event. The parameters for this method are the event *name* and the :class:`Symfony\\Component\\EventDispatcher\\Event` *instance*.

In Elcodi bundles, events taxonomy and names are defined as string ``const`` inside a class residing in the bundle root directory. This class has to be named ``ElcodiBundlenameEvents``, so if we are defining event names for the ``CartBundle``, the class name will be `ElcodiCartEvents`_. No big mystery, it just follows Symfony's bundle `naming best practices`_.

Event class definitions are located inside the ``Event`` directory and obviously their implementation varies according to what you want to wrap inside the message passed to the listeners. Sticking with ``CartBundle`` as an implementation reference, it is important to define fine-grained domain events for the objects we are observing: ``Cart`` and ``Order`` shape the innermost part of any transactional commerce application, so we want to know when something changes their state, when they are pristine, when they are loaded.

Thus we see events such as ``CartPreLoadEvent``, ``CartOnLoadEvent``, ``CartPostLoadEvent``, ``OrderOnCreatedEvent`` and so on. Refer to ``CartBundle`` :doc:`documentation </bundles/CartBundle/index>` for more details.



As a rule of thumb, actions changing states of entities or other domain objects are implemented in ``Services``.

.. _bundle-factory:

Factory
-------

Factories allows the creation of entities in a consistent state. Instead of clobbering object constructors with tricky initializations, which can be tedious when composition or aggregation is involved, we just delegate this task to specific services. Factories are passed along services that rely upon having pristine entities injected, they provide another level of abstraction and can help design a loose coupled model. An trivial yet enlighting example can be a doctrine ``Collection`` initialization: no more ``$this->children = new ArrayCollection();`` in your ``__construct()``.

Factories reside inside the ``Factory`` directory, located at the root of the bundle. They are defined as Symfony services in the ``factories.yml`` config file inside the ``Resources/config`` directory.

Resources
---------

As with any proper Symfony component, the ``Resources`` directory houses frontend views, assets and the containing bundle's configuration files in the ``config`` subdirectory.

Configuration files for Elcodi bundles should be written in the `YAML`_ format.

The naming policy for configuration parameters follow a pseudo-hierarchy in the form of ``vendor.bundle_name.configuration_target`` where ``configuration_target`` can be ``entity``, ``services``, ``event_listeners``, ``factory``. This normalized base name convention avoids the obnoxious proliferation of hard-to-remember container parameters. 

Thus, for the ``CartBundle`` component, we will end up with this parameters:

    ``elcodi.core.cart`` as a *basename* for our configuration parameters

    ``elcodi.core.cart.entity.<entityname>.class`` for ``<entityname>`` class parameters

    ``elcodi.core.cart.services.<servicename>`` to define the ``<servicename>`` service

    ``elcodi.core.cart.services.<servicename>.class`` to define ``<servicename>`` class parameter

    ``elcodi.core.cart.event_listeners.<eventlistener>`` to define the ``<eventlistener>`` observer

    ``elcodi.core.cart.event_listeners.<eventlistener>.class`` to define the ``<eventlistener>`` class parameter

And so on


Configuration files
~~~~~~~~~~~~~~~~~~~

Configuration files for Elcodi bundles are loaded from the bundle Extension class as seen in the :ref:`dependencyinjection` section. These are the common files that a bundle will rely upon:

* ``classes.yml`` defines container parameters associated to class names. As you know parametrized class names is the base for `services customization`_. 
* ``eventListeners.yml`` holds event listener definitions, as seen in `Symfony Event Dispatcher`_. Event names to be passed to the ``kernel.event_listener`` tag must be defined in the :ref:`bundle-events` classes.
* ``factories.yml`` defines :ref:`factory services <bundle-factory>` 
* ``services.yml`` plain old `services`_ definition. 
* ``doctrine/MyEntity.orm.yml`` doctrine `mapping configuration`_. 

If you have been using `doctrine annotations`_ it may look odd to switch back to a heavier, more structured mapping configuration. However, remember that we try to avoid tight coupling and we don't want our entities to depend on Doctrine.


Using individual bundles
------------------------ 

Obviously each bundle comes with its own ``composer.json``. This makes it easier to use individual bundles, which know their own dependencies.

Refer to the specific bundle :doc:`documentation </bundles/index>` to see how to install them separately as a dependency of your Symfony application.

.. _`best practices`: http://symfony.com/doc/current/cookbook/bundles/best_practices.html
.. _`ElcodiCartExtension`: https://github.com/elcodi/elcodi/blob/master/src/Elcodi/CartBundle/DependencyInjection/ElcodiCartExtension.php
.. _`override doctrine relationships`: http://symfony.com/doc/current/cookbook/doctrine/resolve_target_entity.html
.. _`Symfony Event Dispatcher`: http://symfony.com/doc/current/components/event_dispatcher/introduction.html
.. _`ElcodiCartEvents`: https://github.com/elcodi/elcodi/blob/master/src/Elcodi/CartBundle/ElcodiCartEvents.php
.. _`naming best practices`: http://symfony.com/doc/current/cookbook/bundles/best_practices.html
.. _`YAML`: http://symfony.com/doc/current/components/yaml/yaml_format.html
.. _`services customization`: http://symfony.com/doc/current/book/service_container.html#book-service-container-parameters
.. _`services`: http://symfony.com/doc/current/book/service_container.html#what-is-a-service
.. _`mapping configuration`: http://symfony.com/doc/current/book/doctrine.html#book-doctrine-adding-mapping
.. _`doctrine annotations`: http://docs.doctrine-project.org/projects/doctrine-common/en/latest/reference/annotations.html
