from django.urls import path
from .views import AdminSignup, AdminLogin

urlpatterns = [
    path('auth/signup/', AdminSignup.as_view(), name='admin-signup'),
    path('auth/login/', AdminLogin.as_view(), name='admin-login'),
]
