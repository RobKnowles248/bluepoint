# Generated by Django 3.2.7 on 2021-10-15 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logbooks', '0004_bluepoint_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bluepoint',
            name='comment',
        ),
    ]
