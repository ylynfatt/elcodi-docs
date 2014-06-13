Cart
====

Entities
--------

Cart
~~~~

It is the main entity in the bundle. It is used by a project exploiting the CartBundle to store all the informations and elements needed to perform a purchase.

CartLine
~~~~~~~~

Represents a line of a ``Cart``. It holds a reference to the product being purchased as well as the quantity and other specific features, such as product customizations.

Events
------

cart_line.onadd
~~~~~~~~~~~~~~~

This event is triggered when a CartLine is added to a ``Cart``.

To subscribe to this event we will have to configure our event listener config file as follows:

.. code-block:: yaml

    my_event_listener:
        class: %my_event_listener_class%
        tags:
            - { name: kernel.event_listener, event: cart_line.onadd, method: onCartLineAdd }


The related EventListener class and method will be:

.. code-block:: php

    namespace Elcodi\CartBundle\Event\CartLineOnAddEvent;

    public function onCartLineAdd(CartLineOnAddEvent $event)
    {
        $cart = $event->getCart();
        $cartLine = $event->getCartLine();
    }

cart_line.onremove
~~~~~~~~~~~~~~~~~~

This event is fires whenever a CartLine is removed from a ``Cart``.

To subscribe to this event we will have to configure our event listener config file as follows:

.. code-block:: yaml

    my_event_listener:
        class: %my_event_listener_class%
        tags:
            - { name: kernel.event_listener, event: cart_line.onremove, method: onCartLineRemove }


The related EventListener class and method will be:

.. code-block:: php

    namespace Elcodi\CartBundle\Event\CartLineOnRemoveEvent;

    public function onCartLineRemove(CartLineOnRemoveEvent $event)
    {
        $cart = $event->getCart();
        $cartLine = $event->getCartLine();
    }


cart_line.onedit
~~~~~~~~~~~~~~~~

This event is fired when a CartLine is modified. A CartLine can be modified only if it was already stored in the persistence layer and belongs to a ``Cart``.

To subscribe to this event we will have to configure our event listener config file as follows:

.. code-block:: yaml

    my_event_listener:
        class: %my_event_listener_class%
        tags:
            - { name: kernel.event_listener, event: cart_line.onedit, method: onCartLineEdit }


The related EventListener class and method will be:

.. code-block:: php

    namespace Elcodi\CartBundle\Event\CartLineOnEditEvent;

    public function onCartLineEdit(CartLineOnEditEvent $event)
    {
        $cart = $event->getCart();
        $cartLine = $event->getCartLine();
    }


cart.onempty
~~~~~~~~~~~~

This event is triggered when a ``Cart`` is emptied.

To subscribe to this event we will have to configure our event listener config file as follows:

.. code-block:: yaml

    my_event_listener:
        class: %my_event_listener_class%
        tags:
            - { name: kernel.event_listener, event: cart.onempty, method: onCartEmpty }


The related EventListener class and method will be:

.. code-block:: php

    namespace Elcodi\CartBundle\Event\CartEmptyOnEvent;

    public function onCartEmpty(CartEmptyOnEvent $event)
    {
        $cart = $event->getCart();
    }


cart.preload
~~~~~~~~~~~~

This event attempts to bring a ``Cart`` to a valid and consistent state. A ``Cart`` is considered to be in a valid state when it can be converted to an Order with no further changes.

Listeners that are subscribed to this event *must not* perform doctrine ``persist`` or ``flush`` operations, since this is a task that should be done by ``cart.onload`` subscribers. This event must be used only to work with the passed ``Cart`` and its collaborators, with no need to worry about operations related to the persistence layer.

To subscribe to this event we will have to configure our event listener config file as follows:

.. code-block:: yaml

    my_event_listener:
        class: %my_event_listener_class%
        tags:
            - { name: kernel.event_listener, event: cart.preload, method: onCartPreLoad }


The related EventListener class and method will be:

.. code-block:: php

    namespace Elcodi\CartBundle\Event\CartPreLoadEvent;

    public function onCartPreLoad(CartPreLoadEvent $event)
    {
        $cart = $event->getCart();
    }


Actions triggered by this event
###############################

- ``CartEventListener::checkCartLine``: Check the lines of a given ``Cart``. For each CartLine, a consistency check is performed, making sure that there is no stock violation. **Priority: 0**


cart.onload
~~~~~~~~~~~

When this event is fired, the ``Cart`` must be in a valid and consistent state. It should be used only to notify listeners that recalculate ``Cart`` header information (such as iterating CartLines amounts and calculate their parent ``Cart`` grandtotal) and perform flush operations to the persistence layer.

To subscribe to this event we will have to configure our event listener config file as follows:

.. code-block:: yaml

    my_event_listener:
        class: %my_event_listener_class%
        tags:
            - { name: kernel.event_listener, event: cart.onload, method: onCartOnLoad }

The related EventListener class and method will be:

.. code-block:: php

    namespace Elcodi\CartBundle\Event\CartOnLoadEvent;

    public function onCartOnLoad(CartOnLoadEvent $event)
    {
        $cart = $event->getCart();
    }


Actions triggered by this event
###############################

- ``CartEventListener::loadCartPrices``: Given an associated Product, calculates prices for each CartLine as well as parent ``Cart`` grandtotals. **Priority: 16**
- ``CartEventListener::onCartLoadFlush``: Flushes the ``Cart`` and its associated managed entities to the persistence layer. This is where the ``Cart`` gets physically stored in the BBDD. **Priority: 0**

Since ``CartEventListener::onCartLoadFlush`` is responsible for physically storing changes, care should be taken when designing custom event listeners subscribing ``cart.onload``: if a listener has to perform changes to the ``Cart`` that need to be made persistent, it is important for this listener to have a **positive** (> 0) priority so that it gets called **before** ``CartEventListener::onCartLoadFlush``. 


cart.inconsistent
~~~~~~~~~~~~~~~~~

It is possible for a CartLine consistency check (triggered by a ``cart.preload`` event) to fail. A consistency check may fail if a product associated with a CartLine is not enabled, if the item quantity is less or equal to zero or is greater than the available stock for a given product. On such cases, for each inconsistent CartLine a ``cart.inconsistent`` event will be fired, so that it can be intercepted by custom logic performing additional operations, before being silently removed from its parent ``Cart``.

To subscribe to this event we will have to configure our event listener config file as follows:

.. code-block:: yaml

    my_event_listener:
        class: %my_event_listener_class%
        tags:
            - { name: kernel.event_listener, event: cart.inconsistent, method: onCartInconsistent }


The related EventListener class and method will be:

.. code-block:: php

    namespace Elcodi\CartBundle\Event\CartInconsistentEvent;

    public function onCartOnLoad(CartInconsistentEvent $event)
    {
        $cart = $event->getCart();
        $cartLine = $event->getCartLine();
    }


