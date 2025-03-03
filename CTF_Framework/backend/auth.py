from django.shortcuts import render, HttpResponse

def login(request):
    return HttpResponse("Login!")

def register(request):
    return HttpResponse("Register!")