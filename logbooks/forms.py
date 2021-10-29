from django import forms
from .models import Bluepoint


class BluepointForm(forms.ModelForm):
    """
    Form for creating/editing a bluepoint object
    """
    class Meta:
        model = Bluepoint
        exclude = ['date_added']

    def __init__(self, *args, **kwargs):
        """
        Add placeholders to Bluepoint form
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'route_name': 'The name of the route you belayed the climber on...',
            'climber': 'The climber who you belayed on that route...',
            'grade': 'The grade of the route climbed...',
            'comment': 'Any comments...',
        }

        for field in self.fields:
            if field in placeholders.keys():
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
