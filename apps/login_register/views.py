# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import *


# Create your views here.
def index(request):
    login_form = UserLoginForm(request.POST or None)
    reg_form = UserRegistrationForm(request.POST or None)
    context = {
        'login_form': login_form,
        'reg_form': reg_form,
    }
    return render(request, 'login_register/index.html', context)


def to_login(request):
    login_form = UserLoginForm(request.POST or None)
    reg_form = UserRegistrationForm()
    context = {
        'login_form': login_form,
        'reg_form': reg_form,
    }
    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('reviews:index')
    return render(request, 'login_register/index.html', context)


def to_logout(request):
    logout(request)
    return redirect('login_register:index')


def to_register(request):
    login_form = UserLoginForm()
    reg_form = UserRegistrationForm(request.POST or None)
    context = {
        'login_form': login_form,
        'reg_form': reg_form,
    }
    if reg_form.is_valid():
        new_user = reg_form.save(commit=False)
        password = reg_form.cleaned_data.get('password')
        new_user.set_password(password)
        new_user.save()
        log_new_user = authenticate(username=new_user.username, password=password)
        login(request, log_new_user)
        return redirect('reviews:index')
    return render(request, 'login_register/index.html', context)

