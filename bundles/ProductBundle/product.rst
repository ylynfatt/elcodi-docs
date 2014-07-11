Product
=======

.. _productbundle-product-product-and-variant:

Product and Variant
-------------------

``Product`` and ``Variant`` share a common ``PurchasableInterface`` behavior. This is useful when dealing with both object as seen from the point of view of services working with them.

.. note ::

    In the following paragraph we will refer to ``PurchasableInterface`` as a ``Purchasable``. Keep in mind that the actual intrerface name is always ``PurchasableInterface``


a ``Purchasable`` is an object that:

* Has a SKU code
* Has ``stock`` attribute, reporting the purchasable availability.
* Implements ``ProductPriceInterface``, so that prices can be read and written

Seen from the ``Cart`` point of view, a ``Purchasable`` is an object that can be passed to the ``CartManager`` and is eligible to be added to the ``Cart`` for further processing. See the :ref:`CartManager::addPurchasable() <cartbundle-services-addpurchasable>` documentation for more details.

