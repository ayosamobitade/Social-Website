from django.urls import path
from .views import user_login
import django.contrib.auth impo




urlpatterns = [
    path('login/', user_login, name = 'login'),
    pat
    
]