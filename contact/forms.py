from django import forms

from .models import Query


class QueryForm(forms.ModelForm):
    """
    displays a form for users to submit 
    a query
    """
    class Meta:
        """
        defines the model and the fields displayed
        """
        model = Query
        exclude = 'date_submitted'
