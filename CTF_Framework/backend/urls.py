from django.urls import path
from . import auth, views
urlpatterns = [
    path('register/', auth.register, name='Register'),
    path('login/', auth.login, name='Login'),
    
    path('', views.home, name='Home'),
    path('leaderboard/', views.leaderboard, name='Leader Board'),
    path('announcement/', views.announcement, name='Announcement'),
    path('profile/', views.profile, name='Profile'),
    path('team/', views.teamProfile, name='Team Profile'),
]
