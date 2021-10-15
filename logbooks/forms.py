from django import forms
from .models import Bluepoint, Logbook


class BluepointForm(forms.ModelForm):
    """
    Form for creating/editing a bluepoint object
    """
    class Meta:
        model = Bluepoint
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Get an array of climbing grades
        grades = []
        letters = ['a', 'b', 'c']
        for i in range(1, 10):
            if i < 6:
                grades.append(str(i))
                grades.append(str(i) + '+')
            else:
                for letter in letters:
                    grades.append(str(i) + letter)
                    grades.append(str(i) + letter + '+')
        self.fields['grade'].choices = grades
