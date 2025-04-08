from django.urls import path
from Users.api.views.authviews import *


urlpatterns=[

    # auth
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # task
    
  

]