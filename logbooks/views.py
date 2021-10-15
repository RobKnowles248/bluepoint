from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from .models import Logbook


def logbook(request, user_id):
    """
    Display the user's logbook
    """
    if user_id == 'my':
        logbook = get_object_or_404(Logbook, user=request.user)
        my_logbook = True
    else:
        logbook = get_object_or_404(Logbook, user_id=user_id)
        my_logbook = False
    template = 'logbooks/logbook.html'
    context = {
        'logbook': logbook,
        'my_logbook': my_logbook,
    }

    return render(request, template, context)


def add_bluepoint(request):
    """
    Add a new bluepoint to your logbook
    """
    if request.user.is_authenticated:
        template = 'logbooks/add_bluepoint.html'
        context = {}

        return render(request, template, context)
    else:
        messages.info(request, 'Please log in to add a bluepoint')
        redirect(reverse('account_login'))
