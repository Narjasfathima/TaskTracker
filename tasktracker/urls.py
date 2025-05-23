from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.authentication import JWTAuthentication

from Admin.views.authviews import SignInView


from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

users_schema_view = get_schema_view(
    openapi.Info(
        title="User API Documentation",
        default_version='v1',
        description="API documentation for User",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[JWTAuthentication],
    patterns=[path('User/', include('Users.urls'))],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',SignInView.as_view(),name='signin'),
    path('Admin/',include('Admin.urls')),
    path('User/',include('Users.urls')),

    # Swagger for Users app
    re_path(r'^swagger/user/(?P<format>\.json|\.yaml)$', users_schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/user/', users_schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
