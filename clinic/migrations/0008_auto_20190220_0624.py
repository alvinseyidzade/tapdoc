# Generated by Django 2.1.2 on 2019-02-20 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0007_auto_20190220_0623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='xidmetler',
            field=models.ManyToManyField(related_name='xidmett', through='clinic.Xidmetler_qiymet', to='xidmetler.Xidmetler'),
        ),
    ]
