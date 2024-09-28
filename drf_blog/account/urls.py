from django.urls import path 
from rest_framework.authtoken.views import obtain_auth_token 
from .views import user_registration

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/',user_registration, name='register'),
    
]