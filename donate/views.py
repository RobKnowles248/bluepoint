from django.shortcuts import render

from .forms import DonationForm


def donate(request):
    """
    A view for rendering the donation page
    """
    donation_form = DonationForm()
    template = 'donate/donate.html'
    context = {
        'donation_form': donation_form,
        'stripe_public_key': 'pk_test_51JLphqKpMBPEAF4Mc730BMeFYr4He6G6FWFQTC9D3T61biArtAStuEVpGtWXwlmpJKxAby2h3lCXMWDyPYB90SeE00Gcios0SJ',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
