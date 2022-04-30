from django import forms
from .widgets import CustomClearableFileInput
from .models import Maker


class MakerForm(forms.ModelForm):
    """
    form used to add and edit details of artisans
    """
    class Meta:
        """
        defines which model fields are displayed
        """
        model = Maker
        fields = '__all__'

    image1 = forms.ImageField(label='Image',
                              required=False, widget=CustomClearableFileInput)
