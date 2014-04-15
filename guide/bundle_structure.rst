Bundle structure
================

Structure intro.

Base structure of a bundle
--------------------------

.. note::

	Look at :ref:`dependencyinjection` for an overview of the proposed `Extension class`_ at the base of Elcodi bundles.



* ``Factories``
* ``Wrappers``
* ``Resources``

.. code-block:: php

	namespace Elcodi\CoreBundle\Factory\Abstracts;

	use Elcodi\CoreBundle\Entity\Abstracts\AbstractEntity;	

	abstract class AbstractFactory
	{
		/**
	     * Creates an instance of an entity.
	     * All entity querying logic should be placed in a repository, and all
	     * creational logic in a factory class.
	     *
	     * This method must return always an empty instance for related entity,
	     * initialized as expected by documentation.
	     *
	     * If original entity is overwritten and new Implementation has the same
	     * construct behaviour, this method should not be overwritten.
	     *
	     * @return AbstractEntity Empty entity
	     */
	    abstract public function create();
	}


.. _`Extension class`: http://symfony.com/doc/current/cookbook/bundles/extension.html