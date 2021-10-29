from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Logbook, Bluepoint
from .forms import BluepointForm
from .utils import get_sort_grade, get_logbook_data


def logbook(request, username):
    """
    Display the user's logbook
    """
    logbook = Logbook.objects.get(user__username=username)
    my_logbook = (str(request.user) == username)
    bluepoints = Bluepoint.objects.all().filter(user=logbook)
    logbook_data = get_logbook_data(bluepoints)
    sorted_bluepoints = logbook_data['sorted_bluepoints']
    max_number_of_grade = logbook_data['max_number_of_grade']

    template = 'logbooks/logbook.html'
    context = {
        'logbook': logbook,
        'my_logbook': my_logbook,
        'sorted_bluepoints': sorted_bluepoints,
        'max_number_of_grade': max_number_of_grade
    }

    return render(request, template, context)


@login_required
def add_bluepoint(request):
    """
    Add a new bluepoint to your logbook
    """
    if request.method == "POST":
        logbook = get_object_or_404(Logbook, user=request.user)
        sort_grade = get_sort_grade(request.POST['grade'])
        form_data = {
            'route_name': request.POST['route_name'],
            'climber': request.POST['climber'],
            'grade': request.POST['grade'],
            'comment': request.POST['comment'],
            'user': logbook,
            'sort_grade': sort_grade,
        }
        form = BluepointForm(form_data)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Bluepoint successfully added to your logbook')
            return redirect(reverse('logbook', args=[request.user]))
        else:
            messages.error(request, 'Error submitting form')
    else:
        form = BluepointForm()
    template = 'logbooks/add_bluepoint.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required()
def edit_bluepoint(request, bluepoint_id):
    """
    Edit a bluepoint
    """
    bluepoint = get_object_or_404(Bluepoint, id=bluepoint_id)
    user_logbook = get_object_or_404(Logbook, user=request.user)
    bluepoints = Bluepoint.objects.all().filter(user=user_logbook)
    if bluepoint in bluepoints:
        if request.method == 'POST':
            sort_grade = get_sort_grade(request.POST['grade'])
            form_data = {
                'route_name': request.POST['route_name'],
                'climber': request.POST['climber'],
                'grade': request.POST['grade'],
                'comment': request.POST['comment'],
                'user': user_logbook,
                'sort_grade': sort_grade,
            }
            form = BluepointForm(
                form_data, request.FILES, instance=bluepoint)
            if form.is_valid():
                form.save()
                messages.success(
                    request, 'Successfully updated bluepoint!')
                return redirect(reverse('logbook', args=[request.user]))
            else:
                messages.error(
                    request, 
                    'Failed to update bluepoint. Please check the form!'
                )
        else:
            form = BluepointForm(instance=bluepoint)
            messages.info(
                request, 
                f'You are editing your bluepoint of {bluepoint.route_name}'
            )

        template = 'logbooks/edit_bluepoint.html'
        context = {
            'form': form,
            'bluepoint': bluepoint,
        }

        return render(request, template, context)
    else:
        messages.error(
            request, 'You do not have permission to edit that bluepoint!')
        return redirect(reverse('home'))


@login_required
def delete_bluepoint(request, bluepoint_id):
    """
    Delete a bluepoint
    """
    bluepoint = get_object_or_404(Bluepoint, id=bluepoint_id)
    if str(bluepoint.user) == str(request.user):
        bluepoint.delete()
        messages.success(request, 'Bluepoint successfully deleted!')
        return redirect(reverse('logbook', args=[request.user]))
    else:
        messages.error(
            request, 'You do not have permission to delete that bluepoint!')
        return redirect(reverse('home'))


def search(request):
    """
    A view to display logbook search results
    """
    query = None
    if request.GET:
        if 'query' in request.GET:
            query = request.GET['query']
    if not query:
        messages.error(request, "You didn't enter any search criteria!")
        return redirect(reverse('home'))
    users = User.objects.filter(username__contains=query)

    template = 'logbooks/search.html'
    context = {
        'users': users,
        'query': query
    }

    return render(request, template, context)
