from django.shortcuts import render, HttpResponse
from .utils import login_required

def home(request):
    return HttpResponse("this is home page")

def leaderboard(request):
    return HttpResponse("this is leader board page")

@login_required
def challenge(request):
    return HttpResponse("This is challenge page")

@login_required
def profile(request):
    return HttpResponse("This is profile page")

@login_required
def teamProfile(request):
    return HttpResponse("This is team page")