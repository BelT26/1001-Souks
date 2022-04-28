from django.db import models


# Create your models here.
class Query(models.Model):
    """
    A model to represent a query that is generated
    throught the contact form
    """
    PERSONALISATION = 'PR'
    BESPOKE = 'BS'
    DELIVERY = 'DE'
    EXCHANGE = 'ER'
    OTHER = 'OT'
    COLLABORATE = 'CO'
    QUERY_CHOICES = [
        (PERSONALISATION, 'Personalisation Request'),
        (BESPOKE, 'Bespoke / Sourcing Enquiry'),
        (DELIVERY, 'Delivery'),
        (EXCHANGE, 'Exchange / Refund'),
        (COLLABORATE, 'Work With Us'),
        (OTHER, 'Other')
    ]

    class Meta:
        """returns the correct plural spelling in the admin panel"""
        verbose_name_plural = 'Queries'

    name = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(max_length=200, blank=False, null=False)
    query_type = models.CharField(max_length=200, choices=QUERY_CHOICES, 
                                  default=OTHER)
    details = models.TextField(default='')
    date_submitted = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return f'{self.name}'
