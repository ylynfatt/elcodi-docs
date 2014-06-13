Order
=====

Entities
--------

Order
~~~~~

It is the persistent transformation of a ``Cart``. A ``Cart`` is converted to an Order so that the purchase can finalize by applying a payment process. An Order yields a plain copy of the information stored in the originating ``Cart`` so that there is no need to depend on the persistence layer. It also enforces consistency with the information coming from collaborating entities that can change their state (such as the price of a Product)

OrderLine
~~~~~~~~~

Represents a line of an Order. It relates to Order in the same way a ``CartLine`` relates to a ``Cart``: it is a persistent transformation of a CartLine. Like an Order, it yields a copy of the content stored in a CartLine.

Changes on an OrderLine can trigger actions that can change the state of its parent Order.

OrderHistory
~~~~~~~~~~~~

Each OrderHistory represents a point-in-time snapshot of the state of an order. Each change of state in an Order triggers the creation of an OrderHistory. When an Order is created, it is assigned an initial state. Meaningful and valid state transitions are driven by a customizable state workflow that can be defined at project level.

OrderLineHistory
~~~~~~~~~~~~~~~~

Like OrderHistory, this entity represent each and every state that an OrderLine has passed through. When an OrderLine is created, it is assigned an initial state. Meaningful and valid state transitions are driven by a customizable state workflow that can be defined at project level.


Events
------

order.precreated
~~~~~~~~~~~~~~~~

This event is fired right before a ``Cart`` gets converted to an Order. At this stage the Order object has not been created yet, so it is possible to attach custom logic and make decisions by analyzing the provided ``Cart`` instance. 


To subscribe to this event we will have to configure our event listener config file as follows:

.. code-block:: yaml

    my_event_listener:
        class: %my_event_listener_class%
        tags:
            - { name: kernel.event_listener, event: order.precreated, method: onOrderPreCreated }


The related EventListener class and method will be:

.. code-block:: php

    namespace Elcodi\CartBundle\Event\OrderPreCreatedEvent;

    public function onOrderPreCreated(OrderPreCreatedEvent $event)
    {
        $cart = $event->getCart();
    }


order.oncreated
~~~~~~~~~~~~~~~

This event is fired when a new Order has been created given a ``Cart``. At this stage the Order is available for processing.

To subscribe to this event we will have to configure our event listener config file as follows:

.. code-block:: yaml

    my_event_listener:
        class: %my_event_listener_class%
        tags:
            - { name: kernel.event_listener, event: order.oncreated, method: onOrderCreated }


The related EventListener class and method will be:

.. code-block:: php

    namespace Elcodi\CartBundle\Event\OrderOnCreatedEvent;

    public function onOrderCreated(OrderOnCreatedEvent $event)
    {
        $cart = $event->getCart();
        $order = $event->getOrder();
    }


Actions triggered by this event
###############################

- ``OrderEventListener::onOrderCreated``: persists and flushes the newly created Order and it associated collaborators to the pestistence layer. **Priority: 0**

Since ``OrderEventListener::onOrderCreated`` is responsible for physically storing changes, care should be taken when designing custom event listeners subscribing ``order.oncreated``: if a listener has to perform changes to the Order that need to be made persistent, it is important for this listener to have a **positive** (> 0) priority so that it gets called **before** ``OrderEventListener::onOrderCreated``. 

order_line.oncreated
~~~~~~~~~~~~~~~~~~~~

Event fired when a new OrderLine is created from a CartLine.

To subscribe to this event we will have to configure our event listener config file as follows:

.. code-block:: yaml

    my_event_listener:
        class: %my_event_listener_class%
        tags:
            - { name: kernel.event_listener, event: order_line.oncreated, method: onOrderLineCreated }


The related EventListener class and method will be:

.. code-block:: php

    namespace Elcodi\CartBundle\Event\OrderLineOnCreatedEvent;

    public function onOrderLineCreated(OrderLineOnCreatedEvent $event)
    {
        $order = $event->getOrder();
        $cartLine = $event->getCartLine();
        $orderLine = $event->getOrderLine();
    }


order_state.prechange
~~~~~~~~~~~~~~~~~~~~~

Event fired when right before a new OrderHistoryState is appended to an existing Order.

To subscribe to this event we will have to configure our event listener config file as follows:

.. code-block:: yaml

    my_event_listener:
        class: %my_event_listener_class%
        tags:
            - { name: kernel.event_listener, event: order_state.prechange, method: onOrderStatePreChange }


The related EventListener class and method will be:

.. code-block:: php

    namespace Elcodi\CartBundle\Event\OrderStatePreChangeEvent;

    public function onOrderStatePreChange(OrderStatePreChangeEvent $event)
    {
        $order = $event->getOrder();
        $lastOrderHistory = $event->getLastOrderHistory();
        $newState = $event->getNewState();
    }


order_state.onchange
~~~~~~~~~~~~~~~~~~~~

Event fired when after new OrderHistoryState is appended to an existing Order.

To subscribe to this event we will have to configure our event listener config file as follows:

.. code-block:: yaml

    my_event_listener:
        class: %my_event_listener_class%
        tags:
            - { name: kernel.event_listener, event: order_state.onchange, method: onOrderStateOnChange }


The related EventListener class and method will be:

.. code-block:: php

    namespace Elcodi\CartBundle\Event\OrderStateOnChangeEvent;

    public function onOrderStateOnChange(OrderStateOnChangeEvent $event)
    {
        $order = $event->getOrder();
        $lastOrderHistory = $event->getLastOrderHistory();
        $newOrderHistory = $event->getNewOrderHistory();
        $newState = $event->getNewState();
    }


Actions triggered by this event
###############################

- ``OrderStateEventListener::onOrderStateChangeFlush``: Persists and flushes the OrderHistory and its collaborating entities. **Priority: 0**

Since ``OrderStateEventListener::onOrderStateChangeFlush`` is responsible for physically storing changes, care should be taken when designing custom event listeners subscribing ``order_state.onchange``: if a listener has to perform changes to the OrderHistory that need to be made persistent, it is important for this listener to have a **positive** (> 0) priority so that it gets called **before** ``OrderStateEventListener::onOrderStateChangeFlush``. 


order_line_state.prechange
~~~~~~~~~~~~~~~~~~~~~~~~~~

Event fired when right before a new OrderLineHistoryState is appended to an existing OrderLine.

To subscribe to this event we will have to configure our event listener config file as follows:

.. code-block:: yaml

    my_event_listener:
        class: %my_event_listener_class%
        tags:
            - { name: kernel.event_listener, event: order_line_state.prechange, method: onOrderLineStatePreChange }


The related EventListener class and method will be:

.. code-block:: php

    namespace Elcodi\CartBundle\Event\OrderLineStatePreChangeEvent;

    public function onOrderLineStatePreChange(OrderLineStatePreChangeEvent $event)
    {
        $order = $event->getOrder();
        $orderLine = $event->getOrderLine();
        $lastOrderLineHistory = $event->getLastOrderLineHistory();
        $newState = $event->getNewState();
    }


order_line_state.onchange
~~~~~~~~~~~~~~~~~~~~~~~~~

Event fired when after new OrderLineHistoryState is appended to an existing OrderLine.

To subscribe to this event we will have to configure our event listener config file as follows:

.. code-block:: yaml

    my_event_listener:
        class: %my_event_listener_class%
        tags:
            - { name: kernel.event_listener, event: order_line_state.onchange, method: onOrderLineStateOnChange }


The related EventListener class and method will be:

.. code-block:: php

    namespace Elcodi\CartBundle\Event\OrderLineStateOnChangeEvent;

    public function onOrderLineStateOnChange(OrderLineStateOnChangeEvent $event)
    {
        $order = $event->getOrder();
        $orderLine = $event->getOrderLine();
        $lastOrderLineHistory = $event->getLastOrderLineHistory();
        $newOrderLineHistory = $event->getNewOrderLineHistory();
        $newState = $event->getNewState();
    }


Actions triggered by this event
###############################

- ``OrderLineStateEventListener::onOrderLineStateOnChange``: Triggers a ``order_state.prechange`` when all lines of the same orders align to the same state. This way it is possible to arrach custom logic that affect an Order when its OrderLines get modified. A common use for this listener is to automatically change an Order state to *accepted* when **all** of its OrderLines change their state to *accepted*
- ``OrderLineStateEventListener::onOrderLineStateOnChangeFlush``: Persists and flushes an OrderLineHistory and its collaborating entities. **Priority: 0**

Since ``OrderLineStateEventListener::onOrderLineStateOnChange`` is responsible for physically storing changes, care should be taken when designing custom event listeners subscribing ``order_line_state.onchange``
: if a listener has to perform changes to the OrderLineHistory that need to be made persistent, it is important for this listener to have a **positive** (> 0) priority so that it gets called **before** ``OrderLineStateEventListener::onOrderLineStateOnChange``. 

.. _order-states:

Order states
------------

A default set of states is defined by the bundle configuration. Along with the states definition, a workflow of valid transitions can be configured which tell to which state each of them can be brought. The ``OrderManager::checkOrderLineCanChangeToState()`` method validates state changes.

The following is the default statuses configuration:


.. code-block:: yaml

	order:
        initial_state:        new
        states:

            # Defaults:
            new:                 
                - accepted
                - pending.payment
                - payment.failed
            accepted:            
                - problem
                - ready.ship
                - cancelled
            problem:             
                - accepted
                - cancelled
            ready.ship:          
                - shipped
            shipped:             
                - returned
                - delivered
            returned:            
                - shipped
                - refunded
                - cancelled
            delivered:           
                - ready.invoice
                - returned
            ready.invoice:       
                - invoiced
            invoiced:            
                - paid
            refunded:            
                - cancelled
            cancelled:           
                - accepted
            pending.payment:     
                - accepted
                - cancelled


It is quite self-explanatory: keys of the ``yaml`` configuration below the ``states`` level represent the status **name**. Elements in the child array are the valid target states.