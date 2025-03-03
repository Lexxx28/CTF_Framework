from django.urls import path
from . import auth
urlpatterns = [
    path('register/', auth.register, name='Register'),
    path('login/', auth.login, name='Login'),
]
