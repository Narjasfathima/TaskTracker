from django.urls import path
from Admin.views.authviews import *
from Admin.views.userviews import *
from Admin.views.adminviews import *
from Admin.views.taskviews import *


urlpatterns=[

    path('super_admin_home',SuperAdminHomeView.as_view(),name='super_admin_home'),

    # User Management
    path('user_reg',UserRegView.as_view(),name='user_reg'),
    path('user_list',UsersListView.as_view(),name='user_list'),
    path('edit_user/<int:id>',EditUserView.as_view(),name='edit_user'),
    path('delete_user/<int:id>',delete_userView,name='delete_user'),

    # Admin Management
    path('admin_reg',AdminRegView.as_view(),name='admin_reg'),
    path('admin_list',AdminListView.as_view(),name='admin_list'),
    path('edit_admin/<int:id>',EditAdminView.as_view(),name='edit_admin'),
    path('delete_admin/<int:id>',delete_adminView,name='delete_admin'),

    # Task Management
    path('add_task',TaskCreateView.as_view(),name='add_task'),
    path('task_list',TaskListView.as_view(),name='task_list'),
    path('edit_task/<int:id>',EditTaskView.as_view(),name='edit_task'),
    path('delete_task/<int:id>',delete_taskView,name='delete_task'),
    path('completed_task/',CompletedTaskListView.as_view(),name='completed_task'),
    path('view_task/<int:id>',TaskView.as_view(),name='view_task'),
  

]