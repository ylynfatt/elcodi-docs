Installation
============

The preferred way to install Elcodi bundles is by using Composer_.

Install CoreBundle as a project dependency
------------------------------------------

The quickest way to include Elcodi CoreBundle in your Symfony project is to just add the ``elcodi/core-bundle`` package to your Symfony project ``composer.json``.

.. code-block:: json

    // Your project composer.json
    "require": {
        "elcodi/core-bundle": "dev-master"
    }


Then just run

.. code-block:: bash

    $ composer.phar update


Refer to the `composer documentation`_ for more details.

.. note::

	``CoreBundle`` is a common requirement for almost all Elcodi bundles. A part from testing purposes, you will not usually need it alone

Install via composer create-project
-----------------------------------

For testing purposes, you can install a testeable version of Elcodi CoreBundle by using ``composer create-project``.

.. code-block:: bash

    $ composer create-project elcodi/core-bundle <TargetDirectory> --stability=dev

This will checkout the latest version of CoreBundle and install its dependencies.
 

Running tests
-------------

If you installed CoreBundle using composer ``create-project``, you can run the test suite by typing

.. code-block:: bash

   $ phpunit -c phpunit.xml

.. _Composer: http://getcomposer.org

.. _`composer documentation`: https://getcomposer.org/doc/00-intro.md