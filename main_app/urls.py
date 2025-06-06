from django.urls import path
# from . import views  
from .views import (
    HomeView, AboutView, ContactView, HelpView,
    EmployeeListView, EmployeeDetailView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView, 
    TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView,
    TimesheetListView, TimesheetDetailView, TimesheetCreateView, TimesheetUpdateView, TimesheetDeleteView,
    TimesheetItemListView, TimesheetItemDetailView, TimesheetItemCreateView, TimesheetItemUpdateView, TimesheetItemDeleteView

    ) 

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('help/', HelpView.as_view(), name='help'),

    path('employees/', EmployeeListView.as_view(), name='employee_list'),
    path('employees/create', EmployeeCreateView.as_view(), name='employee_create'),
    path('employees/<int:pk>', EmployeeDetailView.as_view(), name='employee_detail'),
    path('employees/<int:pk>/update', EmployeeUpdateView.as_view(), name='employee_update'),
    path('employees/<int:pk>/delete', EmployeeDeleteView.as_view(), name='employee_delete'),

    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('tasks/create', TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('tasks/<int:pk>/update', TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete', TaskDeleteView.as_view(), name='task_delete'),

    path('timesheets/', TimesheetListView.as_view(), name='timesheet_list'),
    path('timesheets/create', TimesheetCreateView.as_view(), name='timesheet_create'),
    path('timesheets/<int:pk>', TimesheetDetailView.as_view(), name='timesheet_detail'),
    path('timesheets/<int:pk>/update', TimesheetUpdateView.as_view(), name='timesheet_update'),
    path('timesheets/<int:pk>/delete', TimesheetDeleteView.as_view(), name='timesheet_delete'),

    path('timesheets/<int:timesheet_id>/timesheetitems/', TimesheetItemListView.as_view(), name='timesheet_item_list'),
    path('timesheets/<int:timesheet_id>/timesheetitems/create', TimesheetItemCreateView.as_view(), name='timesheet_item_create'),
    path('timesheets/<int:timesheet_id>/timesheetitems/<int:pk>', TimesheetItemDetailView.as_view(), name='timesheet_item_detail'),
    path('timesheets/<int:timesheet_id>/timesheetitems/<int:pk>/update', TimesheetItemUpdateView.as_view(), name='timesheet_item_update'),
    path('timesheets/<int:timesheet_id>/timesheetitems/<int:pk>/delete', TimesheetItemDeleteView.as_view(), name='timesheet_item_delete'),

  
]


