from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image1 = forms.ImageField(label='Image',
                             required=False,)
    image2 = forms.ImageField(label='Image',
                             required=False,)
    image3 = forms.ImageField(label='Image',
                             required=False,)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names

