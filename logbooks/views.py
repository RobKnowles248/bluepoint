from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from .models import Logbook, Bluepoint
from .forms import BluepointForm
from .functions import sort_bluepoints, get_max_number_of_grade, get_numbers_of_each_grade


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
    bluepoints = Bluepoint.objects.all().filter(user=logbook)
    sorted_bluepoints = sort_bluepoints(bluepoints)
    max_number_of_grade = get_max_number_of_grade(sorted_bluepoints)
    numbers_of_each_grade = get_numbers_of_each_grade(
        sorted_bluepoints, max_number_of_grade)
    template = 'logbooks/logbook.html'
    context = {
        'logbook': logbook,
        'my_logbook': my_logbook,
        'sorted_bluepoints': sorted_bluepoints,
        'max_number_of_grade': max_number_of_grade,
        'numbers_of_each_grade': numbers_of_each_grade,
    }

    return render(request, template, context)


def add_bluepoint(request):
    """
    Add a new bluepoint to your logbook
    """
    if request.user.is_authenticated:
        if request.method == "POST":
            logbook = get_object_or_404(Logbook, user=request.user)
            form_data = {
                'route_name': request.POST['route_name'],
                'crag_name': request.POST['crag_name'],
                'grade': request.POST['grade'],
                'comment': request.POST['comment'],
                'user': logbook,
            }
            print(form_data)
            form = BluepointForm(form_data)
            if form.is_valid():
                form.save()
                messages.success(request, 'Bluepoint successfully added to your logbook')
                return redirect(reverse('logbook', args=['my']))
            else:
                messages.error(request, 'Error submitting form')
        else:
            form = BluepointForm()
        template = 'logbooks/add_bluepoint.html'
        context = {
            'form': form,
        }

        return render(request, template, context)
    else:
        messages.info(request, 'Please log in to add a bluepoint')
        return redirect(reverse('account_login'))
