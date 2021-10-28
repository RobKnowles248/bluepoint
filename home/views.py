from django.shortcuts import render, reverse
from django.conf import settings
from logbooks.models import Bluepoint


def index(request):
    """ A view to return the index page """
    # Get the 10 most recent bluepoints
    recent_bluepoints = Bluepoint.objects.all().order_by(
        'date_added__day', 'date_added__hour', 'date_added__minute'
    ).reverse()[:10]

    # Get the 10 top bluepoints
    top_bluepoints = Bluepoint.objects.all().order_by(
        'sort_grade'
    ).reverse()[:10]

    template = 'home/index.html'
    context = {
        'recent_bluepoints': recent_bluepoints,
        'top_bluepoints': top_bluepoints,
        'MEDIA_URL': settings.MEDIA_URL,
    }

    return render(request, template, context)
