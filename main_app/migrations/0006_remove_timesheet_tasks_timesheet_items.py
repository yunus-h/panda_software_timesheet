# Generated by Django 5.2.1 on 2025-06-05 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_timesheet_tasks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timesheet',
            name='tasks',
        ),
        migrations.AddField(
            model_name='timesheet',
            name='items',
            field=models.ManyToManyField(through='main_app.TimesheetItem', to='main_app.task'),
        ),
    ]
