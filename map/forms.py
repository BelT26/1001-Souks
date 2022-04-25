from django import forms
from .models import Maker


class MakerForm(forms.ModelForm):

    class Meta:
        model = Maker
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False,)

    