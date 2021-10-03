from django.contrib import admin
from .models import Donation


class DonationAdmin(admin.ModelAdmin):
    readonly_fields = (
        'donation_number', 'date', 'donation_amount')

    fields = (
        'donation_number', 'full_name', 'email', 'date', 'donation_amount')

    list_display = (
        'donation_number', 'date', 'full_name', 'donation_amount'
    )

    ordering = ('-date',)


admin.site.register(Donation)
