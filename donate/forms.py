from django import forms
from .models import Donation


class DonationForm(forms.ModelForm):
    """
    Form for making a donation
    """
    class Meta:
        model = Donation
        fields = (
            'full_name', 'email', 'donation_amount',
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'donation_amount': 'Donation Amount',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
