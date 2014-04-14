Install via composer init-project
=================================

The quickest way to install a testeable version of the Elcodi platform is using `Composer`_.

.. code-block:: bash

    $ composer create-project elcodi/elcodi --stability=dev

This will checkout the latest version of Elcodi and install all its dependencies.

 .. note::
	Installing ``elcodi/elcodi`` via ``composer init-project`` will checkout the *whole* project, basically you will get all the bundles. Look at the section :ref:`using-individual-bundles` to see how to work only with the components that you need.


Running tests
-------------

The standalone project comes with a simple environment that can be used to launch tests. As always you can run the test suite by typing

.. code-block:: bash

   $ phpunit -c phpunit.xml

.. _Composer: http://getcomposer.org
