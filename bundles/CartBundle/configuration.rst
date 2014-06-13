Configuration
=============

Full default configuration
--------------------------

.. code-block: yaml

	# Default configuration for "ElcodiCartBundle"
	elcodi_purchase:
    cart:
        save_in_session:      true
        session_field_name:   cart_id
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

