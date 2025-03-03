from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password, make_password
from .models import User
from .utils import check_fields
import json

def login(request):
    if request.method == "POST":
        parameters = json.loads(request.body)
        
        if check_fields(parameters, ["username", "password"]):
            return JsonResponse({"error": "Please input all parameters."}, status=400)
        
        username, password = parameters['username'].lower(), parameters['password']
        user = User.get_user_by_name(username)
        if not user:
            return JsonResponse({"error": "User not found"}, status=404)
        
        if not check_password(password, user.password):
            return JsonResponse({"error": "Invalid password"}, status=401)
        
        request.session["user_id"] = user.id
        request.session["username"] = user.name
        request.session.set_expiry(12 * 3600)
        
        print(f"==> {user} logged in!")
        return JsonResponse({"message": "Login successful!"})
        
    
    return HttpResponse("Login!")

def register(request):
    if request.method == "POST":
        parameters = json.loads(request.body)
        
        if check_fields(parameters, ["username", "email", "password"]):
            return JsonResponse({"error": "Please input all parameters."}, status=400)
        
        username, email, password = parameters['username'].lower(), parameters['email'].lower(), parameters['password']
        if User.objects.filter(name=username).exists():
            return JsonResponse({"error": "Username already exists!"}, status=400)
        
        if User.objects.filter(email=email).exists():
            return JsonResponse({"error": "Email already registered!"}, status=400)
        
        User.objects.create(
            name=username,
            email=email,
            password=make_password(password)
        )
        
        # TAMBAHIN FITUR OTP
        
        return HttpResponseRedirect("/login/")
    
    return HttpResponse("Register!")