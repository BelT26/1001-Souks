from django.db import models


# Create your models here.
class City(models.Model):
    """A model to  represent the cities that are known for producing certain
    product categories"""

    class Meta:
        """returns the correct plural spelling in the admin panel"""
        verbose_name_plural = 'Cities'

    name = models.CharField(max_length=200, blank=False, null=False)
    description_paragraph1 = models.TextField(default='')
    description_paragraph2 = models.TextField(null=True, blank=True)
    description_paragraph3 = models.TextField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Maker(models.Model):
    """A model to represent each of the featured producers"""
    name = models.CharField(max_length=200, blank=False, null=False)
    city = models.ForeignKey(City, null=True, blank=True,
                             on_delete=models.SET_NULL)
    description = models.TextField()
    image1 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
