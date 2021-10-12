from django.shortcuts import render


def logbook(request):
    """
    Display the user's logbook
    """
    template = 'logbooks/logbook.html'
    context = {}

    return render(request, template, context)
