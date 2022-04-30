from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """
    displays a form for adding and updating products
    """

    class Meta:
        """
        defines the model and the fields displayed
        """
        model = Product
        fields = '__all__'

    image1 = forms.ImageField(label='Image',
                              required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
