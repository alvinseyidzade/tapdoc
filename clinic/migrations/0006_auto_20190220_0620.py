# Generated by Django 2.1.2 on 2019-02-20 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xidmetler', '0001_initial'),
        ('clinic', '0005_auto_20190220_0558'),
    ]

    operations = [
        migrations.CreateModel(
            name='Xidmetler_qiymet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='clinic',
            name='xidmetler',
            field=models.ManyToManyField(related_name='xidmetler', through='clinic.Xidmetler_qiymet', to='xidmetler.Xidmetler'),
        ),
        migrations.AddField(
            model_name='xidmetler_qiymet',
            name='clinic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.Clinic'),
        ),
        migrations.AddField(
            model_name='xidmetler_qiymet',
            name='xidmetler',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xidmetler.Xidmetler'),
        ),
    ]
