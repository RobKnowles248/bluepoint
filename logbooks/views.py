from django.shortcuts import render, get_object_or_404

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
