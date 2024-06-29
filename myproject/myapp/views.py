import logging
from django.shortcuts import render
from .forms import UserForm, RecipeForm
from .models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from datetime import timedelta
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)


def index(request):
    context = {'title': 'Главная'}
    return render(request, 'index.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            logger.info(f'Создан аккаунт {username} ({email=})')
            return redirect('signup_success')
    else:
        form = UserForm()
    context = {
        'title': 'Регистрация',
        'form': form,
    }
    return render(request, 'signup.html', context)


def signup_success(request):
    context = {'title': 'Успешная регистрация'}
    return render(request,
                  'signup_success.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
        else:
            messages.error(request,
                           'Неправильное имя пользователя или пароль')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
        'title': 'Авторизация',
    }
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('index')


@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            messages.success(request, 'Рецепт успешно создан')
            return redirect('index')
    else:
        form = RecipeForm()

    context = {
        'form': form,
        'title': 'Добавить рецепт'
    }
    return render(request, 'add.html', context)