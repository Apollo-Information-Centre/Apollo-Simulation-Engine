# Generated by Django 5.1.3 on 2024-11-15 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='simulation',
            name='description',
        ),
        migrations.RemoveField(
            model_name='simulation',
            name='name',
        ),
        migrations.AddField(
            model_name='simulation',
            name='doctor',
            field=models.CharField(default='Unknown Doctor', max_length=255),
        ),
        migrations.AddField(
            model_name='simulation',
            name='parameter1',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='simulation',
            name='parameter2',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='simulation',
            name='patient',
            field=models.CharField(default='Unknown Patient', max_length=255),
        ),
        migrations.AddField(
            model_name='simulation',
            name='result',
            field=models.FloatField(default=0.0),
        ),
    ]
