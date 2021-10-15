from django import forms
from .models import Bluepoint


class BluepointForm(forms.ModelForm):
    """
    Form for creating/editing a bluepoint object
    """
    class Meta:
        model = Bluepoint
        fields = '__all__'
