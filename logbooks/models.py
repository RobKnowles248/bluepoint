from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .functions import get_grades_tuple


class Logbook(models.Model):
    """
    A model for the logbook of a user of the site
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    max_bluepoint = models.CharField(max_length=3, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Bluepoint(models.Model):
    """
    A model for a log of a bluepoint by a user
    """
    route_name = models.CharField(max_length=254, null=False, blank=False)
    crag_name = models.CharField(max_length=254, null=False, blank=False)
    GRADES = get_grades_tuple()
    grade = models.CharField(
        max_length=3, choices=GRADES, null=False, blank=False)
    user = models.ForeignKey(
        'Logbook', null=False, blank=False, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_or_update_logbook(sender, instance, created, **kwargs):
    """
    Create or update the logbook
    """
    if created:
        Logbook.objects.create(user=instance)
    # Existing users: just save the profile
    instance.logbook.save()
