from django.db import models
from datetime import date

GENDERS = (
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other')
)

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    gender = models.CharField(max_length=50, choices=GENDERS, default='Other')
    start_date = models.DateField(default=date.today)
    hourly_salary = models.DecimalField(max_digits=6, decimal_places=2, default=50.00)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=250)
    profile_pic = models.CharField(max_length=250)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.job_title}"
    
class Task(models.Model):
    task_name =  models.CharField(max_length=100)
    project = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    completed = models.BooleanField(default=False)

    def __str__(self): 
        return f"{self.task_name} - {self.project} ({self.id})"
    

    
class Timesheet(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    timesheet_date = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.employee.name} on {self.timesheet_date}"
    
    def total_hours_worked(self):
        return sum(item.hours_worked for item in self.items.all())
    
    def calculate_pay(self):
        total_hours = self.total_hours_worked()
        return total_hours * self.employee.hourly_salary
    
    class Meta:
        unique_together = ['employee', 'timesheet_date']

class TimesheetItem(models.Model): 
    timesheet = models.ForeignKey(Timesheet, on_delete=models.CASCADE , related_name='items') 
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    hours_worked = models.DecimalField(max_digits=5, decimal_places= 2, default=0.00)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.timesheet.employee.name} works on {self.task.task_name} ({self.task.project}) - {self.hours_worked} hours on {self.timesheet.timesheet_date}"
    
    class Meta:
        unique_together = ['timesheet', 'task']
    

