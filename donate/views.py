from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from django.contrib import messages

import stripe

from .forms import DonationForm
from .models import Donation


def donate(request):
    """
    A view for rendering the donation page
    """
    if request.method == 'POST':
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'donation_amount': request.POST['donation_amount'],
        }
        donation_form = DonationForm(form_data)
        if donation_form.is_valid():
            donation = donation_form.save()
            return redirect(reverse('pay', args=[donation.donation_number]))
        else:
            messages.error(request, 'Please check your details')
    else:
        donation_form = DonationForm()
    template = 'donate/donate.html'
    context = {
        'donation_form': donation_form,
    }

    return render(request, template, context)


def pay(request, donation_number):
    """
    A view for rendering the payment page
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    donation = get_object_or_404(Donation, donation_number=donation_number)

    if request.method == 'POST':
        donation.paid = True
        donation.save()
        return redirect(reverse(
            'payment_success', args=[donation.donation_number]))

    else:
        donation_amount = donation.donation_amount
        stripe_amount = round(donation_amount * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_amount,
            currency=settings.STRIPE_CURRENCY,
        )

        print(intent)

        template = 'donate/pay.html'
        context = {
            'donation_number': donation_number,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, template, context)


def payment_success(request, donation_number):
    """
    Handle successful payments
    """
    donation = get_object_or_404(Donation, donation_number=donation_number)
    messages.success(request, 'Payment successful!')

    template = 'donate/payment_success.html'
    context = {
        'donation': donation,
    }
    return render(request, template, context)
