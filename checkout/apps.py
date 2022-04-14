# from Boutique Ado project
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    alerts Django to new signals file
    """
    name = 'checkout'

    def ready(self):
        """
        imports signals file
        """
        import checkout.signals
