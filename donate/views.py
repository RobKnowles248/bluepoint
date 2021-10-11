from django.shortcuts import render
from django.conf import settings

from .forms import DonationForm

import stripe


def donate(request):
    """
    A view for rendering the donation page
    """
    donation_form = DonationForm()
    template = 'donate/donate.html'
    context = {
        'donation_form': donation_form,
    }

    return render(request, template, context)


def pay(request):
    """
    A view for rendering the payment page
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    donation_amount = 12.99
    stripe_amount = round(donation_amount * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_amount,
        currency=settings.STRIPE_CURRENCY,
    )

    print(intent)

    template = 'donate/pay.html'
    context = {
        'stripe_public_key': stripe_public_key,
        'client_secret': stripe_secret_key,
    }

    return render(request, template, context)
