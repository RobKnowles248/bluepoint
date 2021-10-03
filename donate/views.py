from django.shortcuts import render

from .forms import DonationForm


def donate(request):
    """
    A view for rendering the donation page
    """
    donation_form = DonationForm()
    template = 'donate/donate.html'
    context = {
        'donation_form': donation_form
    }

    return render(request, template, context)
