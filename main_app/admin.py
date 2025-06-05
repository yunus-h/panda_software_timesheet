from django.contrib import admin

from .models import Employee, Task, Timesheet, TimesheetItem

admin.site.register(Employee)
admin.site.register(Task)
admin.site.register(Timesheet)
admin.site.register(TimesheetItem)
