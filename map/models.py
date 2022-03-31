from django.db import models
from products.models import Category


# Create your models here.
class City(models.Model):
    """A model to  represent the cities that are known for producing certain
    product categories"""

    class Meta:
        """returns the correct plural spelling in the admin panel"""
        verbose_name_plural = 'Cities'

    name = models.CharField(max_length=200, blank=False, null=False)
    category = models.ForeignKey(Category, null=True, blank=True,
                                 on_delete=models.SET_NULL)
    description = models.TextField(default='')
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

