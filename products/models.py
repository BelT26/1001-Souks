from django.db import models
from map.models import City, Maker


# Create your models here.
class Category(models.Model):
    """A model to represent the categories that the products will be
    divided into"""

    class Meta:
        """returns the correct plural spelling in the admin panel"""
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=200, blank=False, null=False)
    friendly_name = models.CharField(max_length=200, blank=False, null=False,
                                     default='')
    description = models.TextField(default='')
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    city = models.ForeignKey(City, null=True, blank=True,
                             on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.friendly_name}'

    def get_friendly_name(self):
        """
        returns the friendly name
        """
        return self.friendly_name


class Product(models.Model):
    """A model to represent each of the products sold"""
    name = models.CharField(max_length=200, blank=False, null=False)
    category = models.ForeignKey(Category, null=True, blank=True,
                                 on_delete=models.SET_NULL)
    producer = models.ForeignKey(Maker, null=True, blank=True,
                                 on_delete=models.CASCADE)
    city = models.ForeignKey(City, null=True, blank=True,
                             on_delete=models.SET_NULL)
    sku = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    multibuy_offer = models.BooleanField(default=False, null=True, blank=True)
    multibuy_num_items = models.IntegerField(null=True, blank=True)
    multibuy_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True)
    image1_url = models.URLField(max_length=1024, null=True, blank=True)
    size = models.CharField(max_length=200, null=True, blank=True)
    colour_selection = models.BooleanField(default=False, null=True,
                                           blank=True)
    colour1 = models.CharField(max_length=200, null=True, blank=True)
    colour2 = models.CharField(max_length=200, null=True, blank=True)
    colour3 = models.CharField(max_length=200, null=True, blank=True)
    product_type = models.CharField(max_length=200, blank=True, null=True)
    composition = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
