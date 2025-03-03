from django.shortcuts import render, HttpResponse
from .utils import login_required

def home(request):
    return render(request, 'home.html')

def leaderboard(request):
    return render(request, 'leaderboard.html')

def announcement(request):
    return HttpResponse("this is announcement page")

@login_required
def challenge(request):
    return HttpResponse("This is challenge page")

@login_required
def profile(request):
    return HttpResponse("This is profile page")

@login_required
def teamProfile(request):
    return HttpResponse("This is team page")