Install as a project dependency
===============================

Using Elcodi as a `standalone Symfony application` at this time can be useful just for the sake of exploring the code or to test stuff if you are willing to :doc:`contribute </contributing/contributing>`.

In order to use it as a foundation for your own code you will need to install it as a project dependency. As usual, the quickest way is to just add the ``elcodi`` package to your Symfony project ``composer.json``.

.. code-block:: json

    // Your project composer.json
    "require": {
        "elcodi/elcodi": "dev-master"
    }


Then just run

.. code-block:: bash

    $ composer.phar install


Refer to the `composer documentation`_ for more details.


.. _`composer documentation`: https://getcomposer.org/doc/00-intro.md