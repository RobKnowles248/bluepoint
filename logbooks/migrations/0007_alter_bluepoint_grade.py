# Generated by Django 3.2.7 on 2021-10-18 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logbooks', '0006_bluepoint_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bluepoint',
            name='grade',
            field=models.CharField(choices=[('10c+', '10c+'), ('10c', '10c'), ('10b+', '10b+'), ('10b', '10b'), ('10a+', '10a+'), ('10a', '10a'), ('9c+', '9c+'), ('9c', '9c'), ('9b+', '9b+'), ('9b', '9b'), ('9a+', '9a+'), ('9a', '9a'), ('8c+', '8c+'), ('8c', '8c'), ('8b+', '8b+'), ('8b', '8b'), ('8a+', '8a+'), ('8a', '8a'), ('7c+', '7c+'), ('7c', '7c'), ('7b+', '7b+'), ('7b', '7b'), ('7a+', '7a+'), ('7a', '7a'), ('6c+', '6c+'), ('6c', '6c'), ('6b+', '6b+'), ('6b', '6b'), ('6a+', '6a+'), ('6a', '6a'), ('5+', '5+'), ('5', '5'), ('4+', '4+'), ('4', '4'), ('3+', '3+'), ('3', '3'), ('2+', '2+'), ('2', '2'), ('1+', '1+'), ('1', '1')], max_length=4),
        ),
    ]
