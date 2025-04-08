from django.urls import path
from Users.api.views.authviews import *
from Users.api.views.taskviews import *


urlpatterns=[

    # auth
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # task
    path('tasks/', TaskListView.as_view(), name='tasks'),
    path('tasks/<int:pk>/', TaskStatusUpdateView.as_view(), name='task update'),
    path('tasks/<int:pk>/report/', TaskReportView.as_view(), name='task report'),

  

]