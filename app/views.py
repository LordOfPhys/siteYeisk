#- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.utils import timezone
from app.models import Order

@csrf_exempt
def index(request):
    context_dict = {}
    if request.method == 'POST':
        keys = list(request.POST.keys())
        date = str(timezone.now()).split(" ")[0]
        time = str(timezone.now()).split(" ")[1].split(".")[0]
        order = ""
        i = 0
        while i < len(keys) - 2:
            order += request.POST[keys[i]] + " " + request.POST[keys[i + 1]] + "\n"
            i += 2
        Order.objects.create(phone = request.POST['phone'], adress = request.POST['adress'], time = date + " " + time, order = order)
        return render(request, 'game/spasibo.html', context_dict)
    return render(request, 'game/main.html', context_dict)

@csrf_exempt
def room(request):
    context_dict = {}
    return render(request, 'game/room.html', context_dict)

@csrf_exempt
def log(request):
    if request.method == 'POST':
        a = request.POST['login']
        b = request.POST['password']
        user = authenticate(username=a, password=b)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('../index')
            else:
                context_dict = {'boldmessage': "Данный аккаунт неактивен"}
                return render(request, 'game/login.html', context_dict)
        else:
            context_dict = {'boldmessage': "Неверный логин или пароль"}
            return render(request, 'game/login.html', context_dict)
    context_dict = {'boldmessage': ""}
    return render(request, 'game/login.html', context_dict)

@csrf_exempt
def logout_view(request):
    auth.logout(request)
    return render(request,'game/spasibo.html')
