Services
========

.. _cartbundle-services-cartmanager:

CartManager
-----------

The core service used to perform actions on a ``Cart`` and its related entities is the ``CartManager``.

.. code-block:: php

    $cartManager = $this
        ->container
        ->get('elcodi.cart_manager');


The CartManager provides a simple yet powerful api that gives access to the most common operations related to a checkout process. The following paragraphs describe its methods and parameters.


->addLine()
-----------

Given an instance of a CartInterface and an instance of CartLineInterface, this method adds a ``CartLine`` to a ``Cart``

.. code-block:: php

    use Elcodi\CartBundle\Entity\Cart;
    use Elcodi\CartBundle\Entity\CartLine;

    $cart = new Cart;
    $cartLine = new CartLine;
    $cartManager->addLine(
        $cart, 
        $cartLine
    );

This method will fire the `cart_line.onadd`, ``cart.preload`` and ``cart.onload`` events, in the described order.

->removeLine()
--------------

Given a CartInterface and a CartLineInterface objects, this method will remove a ``CartLine`` from a ``Cart``. 

explain?: dada la configuración de mapeo inicial de ambas entidades, en el momento en que un ``CartLine`` es eliminada de un ``Cart``, este es eliminado de la capa de persistencia. El objeto sigue existiendo como tal.

.. code-block:: php

    use Elcodi\CartBundle\Entity\Cart;
    use Elcodi\CartBundle\Entity\CartLine;

    $cart = new Cart;
    $cartLine = new CartLine;
    $cartManager->removeLine(
        $cart, 
        $cartLine
    );


This method will fire the ``cart_line.onremove``, ``cart.preload`` and ``cart.onload`` events in the described order.

->emptyLines()
--------------

Given a CartInterface object, all its CartLines will be removed.

.. code-block:: php

    use Elcodi\CartBundle\Entity\Cart;

    $cart = new Cart;
    $cartManager->emptyLines(
        $cart
    );


This method will fire the ``cart_line.onempty``, ``cart.preload`` and ``cart.onload`` events in the described order.

->editCartLine()
----------------

Given a CartInterface object, a ProductInterface object and a positive integer number **n**, the ``CartLine`` is modified by adding the Product and setting item quantity to **n**. It is mandatory that a CartLine has an associated ``Cart``.

.. code-block:: php

    use Elcodi\CartBundle\Entity\Cart;
    use Elcodi\ProductBundle\Entity\Product;

    $cart = new Cart;
    $product = new Product();
    $quantity = 10;
    $cartManager->editCartLine(
        $cart,
        $product,
        $quantity
    );

If the value of **n** is less than 1, the ``CartLine`` will be removed and a ``cart_line.onremove`` event will be fired. If its value is equal or greater than 1 a ``cart_line.onedit`` event will be emitted. On both cases the ``cart.preload`` and `cart.onload` events will be fired, in the shown order.


->increaseCartLineQuantity()
----------------------------

Given a CartLineInterface object and a positive integer **n**, the item quantity in the ``CartLine`` will be incremented by **n**. It is mandatory that a ``CartLine`` has an assigned ``Cart``.

.. code-block:: php

    use Elcodi\CartBundle\Entity\Cart;

    $cart = new Cart;
    $quantity = 10;
    $cartManager->increaseCartLineQuantity(
        $cart,
        $quantity
    );


If the resulting item quantity value is less than 1, the CartLine will be removed and a ``cart_line.onremove`` event will be fired. If its value is equal or greater than 1 a ``cart_line.onedit`` event will be emitted. On both cases the ``cart.preload`` and `cart.onload` events will be fired, in the shown order.

->decreaseCartLineQuantity()
----------------------------

Given a CartLineInterface object and a positive integer **n**, the item quantity in the CartLine will be decreased by **n**. It is mandatory that a CartLine has an assigned ``Cart``.

.. code-block:: php

    use Elcodi\CartBundle\Entity\Cart;

    $cart = new Cart;
    $quantity = 10;
    $cartManager->decreaseCartLineQuantity(
        $cart,
        $quantity
    );


If the resulting item quantity value is less than 1, the CartLine will be removed and a ``cart_line.onremove`` event will be fired. If its value is equal or greater than 1 a ``cart_line.onedit`` event will be emitted. On both cases the ``cart.preload`` and `cart.onload` events will be fired, in the shown order.

->setCartLineQuantity()
-----------------------

Given a CartLineInterface object and a positive integer **n**, the item quantity in the CartLine will be set to **n**.

.. code-block:: php

    use Elcodi\CartBundle\Entity\Cart;

    $cart = new Cart;
    $quantity = 10;
    $cartManager->setCartLineQuantity(
        $cart,
        $quantity
    );


If the value of **n** is less than 1, the CartLine will be removed and a ``cart_line.onremove`` event will be fired. If its value is equal or greater than 1 a ``cart_line.onedit`` event will be emitted. On both cases the ``cart.preload`` and ``cart.onload`` events will be fired, in the shown order.

.. _cartbundle-services-addpurchasable:

->addPurchasable()
------------------

``CartManager::addPurchasable(CartInterface $cart, PurchasableInterface $purchasable, $quantity)``

Given a ``CartInterface`` object, a ``PurchasableInterface`` object and a positive integer **n**, if the ``Purchasable`` has not yet been added to the ``Cart`` a new ``CartLine`` is created, holding a reference to the ``Purchasable`` object and an item quantity value of **n** will be set. If the ``Purchasable`` was already present in the ``Cart``, the item quantity value will be increased by **n**.

If the value of **n** is less than 1, no action will be performed on the ``Cart`` or ``CartLine``.

.. note ::

    Refer to the :ref:`ProductBundle documentation <productbundle-product-product-and-variant>` to clarify the meanings of ``Purchasable``, ``Product`` and ``Variant``

When a ``Purchasable`` is added to the ``Cart`` using ``addPurchasable()``, different actions occur internally.

If the ``Purchasable`` is a ``ProductInterface`` object,

* Current ``Cart::cartItems`` are iterated over and the ``Product`` being added is compared with current ``CartLine::product``
* If they match, ``CartLine::quantity`` is incresed correspondingly depending on ``$quantity``.
* if they do *NOT* match, a new ``CartLine`` is factored, ``CartLine::product`` is assigned the passed object and quantity is set correspondingly depending on ``$quantity``.

If the ``Purchasable`` is a ``VariantInterface`` object,

* Current ``Cart::cartItems`` are iterated over and the ``Variant`` being added is compared with current ``CartLine::variant``
* If they match, ``CartLine::quantity`` is incresed correspondingly depending on ``$quantity``.
* if they do *NOT* match, a new ``CartLine`` is factored, ``CartLine::variant`` is assigned the passed object, ``CartLine::product`` is set to ``$purchasable->getProduct()`` and quantity is set correspondingly depending on ``$quantity``.

Example with ``Product``:

.. code-block:: php

    use Elcodi\CartBundle\Entity\Cart;
    use Elcodi\ProductBundle\Entity\Product;

    $cart = new Cart;
    $product = new Product();
    $quantity = 10;
    $cartManager->addPurchasable(
        $cart,
        $product,
        $quantity
    );

Example with ``Variant``:

.. code-block:: php

    use Elcodi\CartBundle\Entity\Cart;
    use Elcodi\ProductBundle\Entity\Product;
    use Elcodi\ProductBundle\Entity\Variant;

    $cart = new Cart;
    $product = new Product();
    $variant = new Variant();
    $variant->setProduct($product);
    $quantity = 10;
    $cartManager->addPurchasable(
        $cart,
        $variant,
        $quantity
    );


If the ``Purchasable`` was already present in the ``Cart``, a ``cart_line.onedit`` event will be fired, referencing the CartLine associated with the Product. Conversely, a `cart_line.onadd` event will be emitted. On both cases, the ``cart.preload`` and ``cart.onload`` events will be fired in the described order.

->addProduct()
--------------

.. note ::

    This method is deprecated. See :ref:`CartManager::addPurchasable() <cartbundle-services-addpurchasable>`


Given a CartInterface object, a ProductInterface object and a positive integer **n**, if the Product has not yet been added to the ``Cart`` a new CartLine is created, holding a reference to the Product object and an item quantity value of **n** will be set. If the Product was already present in the ``Cart``, the item quantity value will be increased by **n**.

If the value of **n** is less than 1, no action will be performed on the ``Cart`` or CartLine.

.. code-block:: php

    use Elcodi\CartBundle\Entity\Cart;
    use Elcodi\ProductBundle\Entity\Product;

    $cart = new Cart;
    $product = new Product();
    $quantity = 10;
    $cartManager->addProduct(
        $cart,
        $product,
        $quantity
    );

If the Product was already present in the ``Cart``, a ``cart_line.onedit`` event will be fired, referencing the CartLine associated with the Product. Conversely, a `cart_line.onadd` event will be emitted. On both cases, the ``cart.preload`` and ``cart.onload`` events will be fired in the described order.