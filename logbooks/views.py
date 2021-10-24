from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User

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


def edit_bluepoint(request, bluepoint_id):
    """
    Edit a bluepoint
    """
    if request.user.is_authenticated:
        bluepoint = get_object_or_404(Bluepoint, id=bluepoint_id)
        user_logbook = get_object_or_404(Logbook, user=request.user)
        bluepoints = Bluepoint.objects.all().filter(user=user_logbook)
        if bluepoint in bluepoints:
            if request.method == 'POST':
                form_data = {
                    'route_name': request.POST['route_name'],
                    'crag_name': request.POST['crag_name'],
                    'grade': request.POST['grade'],
                    'comment': request.POST['comment'],
                    'user': user_logbook,
                }
                form = BluepointForm(
                    form_data, request.FILES, instance=bluepoint)
                if form.is_valid():
                    form.save()
                    messages.success(
                        request, 'Successfully updated bluepoint!')
                    return redirect(reverse('logbook', args=['my']))
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
    else:
        messages.error(
            request, 'You are not logged in!'
        )
        return redirect(reverse('account_login'))


def delete_bluepoint(request, bluepoint_id):
    """
    Edit a bluepoint
    """
    if request.user.is_authenticated:
        bluepoint = get_object_or_404(Bluepoint, id=bluepoint_id)
        user_logbook = get_object_or_404(Logbook, user=request.user)
        bluepoints = Bluepoint.objects.all().filter(user=user_logbook)
        if bluepoint in bluepoints:
            bluepoint.delete()
            messages.success(request, 'Bluepoint successfully deleted!')
            return redirect(reverse('logbook', args=['my']))
        else:
            messages.error(
                request, 'You do not have permission to delete that bluepoint!')
            return redirect(reverse('home'))
    else:
        messages.error(
            request, 'You are not logged in!'
        )
        return redirect(reverse('account_login'))


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
    # queries = Q(user__icontains=query)
    users = User.objects.filter(username__contains=query)

    template = 'logbooks/search.html'
    context = {
        'users': users,
        'query': query
    }

    return render(request, template, context)
