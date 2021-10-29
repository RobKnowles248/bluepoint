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
        Autofocus on full name field
        """
        super().__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs['autofocus'] = True
