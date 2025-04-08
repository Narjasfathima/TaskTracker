from django.urls import path
from Admin.views.authviews import *
from Admin.views.userviews import *


urlpatterns=[

    # Auth
    path('super_admin_home',SuperAdminHomeView.as_view(),name='super_admin_home'),
    path('user_reg',UserRegView.as_view(),name='user_reg'),
    path('user_list',UsersListView.as_view(),name='user_list'),
    path('edit_user/<int:id>',EditUserView.as_view(),name='edit_user'),
    path('delete_user/<int:id>',delete_userView,name='delete_user'),
  

]