
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView, TemplateView

from django.urls import reverse_lazy
from django.shortcuts import render, redirect

from .models import Employee, Task, Timesheet, TimesheetItem


class HomeView(TemplateView): 
    template_name = 'main_app/home.html'

class AboutView(TemplateView):
    template_name = 'main_app/about.html'

class ContactView(TemplateView):
    template_name = 'main_app/contact.html'

class HelpView(TemplateView):
    template_name = 'main_app/help.html'

class PayView(TemplateView):
    template_name = 'main_app/pay.html'

# -----------------------EMPLOYEE----------------------------------

class EmployeeListView(ListView):
    model = Employee
    template_name = './employees/employee_list.html'
    context_object_name = 'employees'

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = './employees/employee_detail.html'
    context_object_name = 'employee'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employee = self.get_object()
        context['employee'] = self.object
        return context
    
class EmployeeCreateView(CreateView):
    model = Employee
    template_name = './employees/employee_form.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('employee_detail', kwargs={'pk': self.object.pk})

class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = './employees/employee_form.html'
    context_object_name = 'employee'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('employee_detail', kwargs={'pk': self.object.pk})

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = './employees/employee_confirm_delete.html'
    context_object_name = 'employee'
    success_url = reverse_lazy('employee_list')

# -----------------------TASK----------------------------------

class TaskListView(ListView):
    model = Task
    template_name = './tasks/task_list.html'
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = Task
    template_name = './tasks/task_detail.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = self.get_object()
        context['task'] = self.object
        return context

class TaskCreateView(CreateView):
    model = Task
    template_name = './tasks/task_form.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('task_detail', kwargs={'pk': self.object.pk})

class TaskUpdateView(UpdateView):
    model = Task
    template_name = './tasks/task_form.html'
    context_object_name = 'task'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('task_detail', kwargs={'pk': self.object.pk})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = './tasks/task_confirm_delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('task_list')

# -----------------------TIMESHEET----------------------------------

class TimesheetListView(ListView):
    model = Timesheet
    template_name = './timesheets/timesheet_list.html'
    context_object_name = 'timesheets'

class TimesheetDetailView(DetailView):
    model = Timesheet
    template_name = './timesheets/timesheet_detail.html'
    context_object_name = 'timesheet'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        timesheet = self.get_object()
        context['timesheet_items'] = TimesheetItem.objects.filter(timesheet=timesheet)
        return context
    
class TimesheetCreateView(CreateView): 
    model = Timesheet
    template_name = './timesheets/timesheet_form.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('timesheet_detail', kwargs={'pk': self.object.pk})
    
class TimesheetUpdateView(UpdateView):
    model = Timesheet
    template_name = './timesheets/timesheet_form.html'
    context_object_name = 'timesheet'
    fields = ['timesheet_date']

    def get_success_url(self):
        return reverse_lazy('timesheet_detail', kwargs={'pk': self.object.pk})

class TimesheetDeleteView(DeleteView): 
    model = Timesheet
    template_name = './timesheets/timesheet_confirm_delete.html'
    context_object_name = 'timesheet'
    success_url = reverse_lazy('timesheet_list')

def timesheet_list(request):
    timesheets = Timesheet.objects.all()
    for t in timesheets:
        t.formatted_pay = "${:,.2f}".format(float(t.calculate_pay()))
    return render(request, 'timesheets/timesheet_list.html', {'timesheets': timesheets})
# -----------------------TIMESHEET ITEM----------------------------------

class TimesheetItemListView(ListView):
    model = TimesheetItem
    template_name = './timesheet_items/timesheet_item_list.html'
    context_object_name = 'timesheet_items'

class TimesheetItemDetailView(DetailView):
    model = TimesheetItem
    template_name = './timesheet_items/timesheet_item_detail.html'
    context_object_name = 'timesheet_item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        timesheet_item = self.get_object()
        context['timesheet_item'] = self.object
        return context
    
class TimesheetItemCreateView(CreateView):
    model = TimesheetItem
    template_name = './timesheet_items/timesheet_item_form.html'
    fields = ['task', 'hours_worked', 'comment']
    context_object_name = 'timesheet_item'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        timesheet_id = self.kwargs.get('timesheet_id')
        # Get tasks already used in this timesheet
        used_tasks = TimesheetItem.objects.filter(timesheet_id=timesheet_id).values_list('task_id', flat=True)
        # Exclude those tasks from the queryset
        form.fields['task'].queryset = Task.objects.exclude(id__in=used_tasks)
        return form

    def form_valid(self, form):
        timesheet_id = self.kwargs.get('timesheet_id')
        form.instance.timesheet_id = timesheet_id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('timesheet_detail', kwargs={'pk': self.object.timesheet.pk})
    
class TimesheetItemUpdateView(UpdateView):
    model = TimesheetItem
    template_name = './timesheet_items/timesheet_item_form.html'
    context_object_name = 'timesheet_item'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('timesheet_detail', kwargs={'pk': self.object.timesheet.pk})
    
class TimesheetItemDeleteView(DeleteView):
    model = TimesheetItem
    template_name = './timesheet_items/timesheet_item_confirm_delete.html'
    context_object_name = 'timesheet_item'
    
    def get_success_url(self):
        return reverse_lazy('timesheet_detail', kwargs={'pk': self.object.timesheet.pk})
