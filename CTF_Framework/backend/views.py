from django.shortcuts import render, HttpResponse
from .utils import login_required

def home(request):
    return render(request, 'home.html')

def leaderboard(request):
    return render(request, 'leaderboard.html')

def announcement(request):
    return render(request, 'announcement.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def teamProfile(request):
    return render(request, 'team.html')