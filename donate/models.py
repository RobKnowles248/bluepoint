import uuid
from django.db import models
from django.conf import settings


class Donation(models.Model):
    """
    A model for a donation by a user of the site
    """
    donation_number = models.CharField(
        max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    donation_amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_donation_number(self):
        """
        Generate a random, unique donation number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override original save method to set the donation number if it
        is not set already
        """
        if not self.donation_number:
            self.donation_number = self._generate_donation_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.donation_number
