# Generated by Django 5.2.1 on 2025-06-05 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_timesheetitem_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timesheetitem',
            name='employee',
        ),
    ]
