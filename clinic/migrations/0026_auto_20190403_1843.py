# Generated by Django 2.1.2 on 2019-04-04 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0025_auto_20190403_0501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clinic',
            name='cityy',
        ),
        migrations.RemoveField(
            model_name='clinic',
            name='location2',
        ),
    ]
