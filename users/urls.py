# Django equivalent of your Spring Boot URL mappings
from django.urls import path
from . import views

urlpatterns = [
    # Hello world endpoints (replacing HelloController)
    path('hello/', views.hello, name='hello'),
    path('about/', views.about, name='about'),
    
    # Authentication endpoints (replacing AuthController)
    path('auth/register/', views.register, name='register'),
    path('auth/login/', views.login, name='login'),
    path('auth/change-password/', views.change_password, name='change-password'),
]
