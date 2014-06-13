Installation
============

The preferred way to install Elcodi bundles is by using Composer_.

Install CartBundle as a project dependency
------------------------------------------

The quickest way to include Elcodi CartBundle in your Symfony project is to just add the ``elcodi/cart-bundle`` package to your Symfony project ``composer.json``.

.. code-block:: json

    // Your project composer.json
    "require": {
        "elcodi/cart-bundle": "dev-master"
    }


Then just run

.. code-block:: bash

    $ composer.phar update


Refer to the `composer documentation`_ for more details.


Install via composer create-project
-----------------------------------

For testing purposes, you can install a testeable version of Elcodi CartBundle by using ``composer create-project``.

.. code-block:: bash

    $ composer create-project elcodi/cart-bundle <TargetDirectory> --stability=dev

This will checkout the latest version of CartBundle and install its dependencies.
 

Running tests
-------------

If you installed CartBundle using composer ``create-project``, you can run the test suite by typing

.. code-block:: bash

   $ phpunit -c phpunit.xml

.. _Composer: http://getcomposer.org

.. _`composer documentation`: https://getcomposer.org/doc/00-intro.md