from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

# Create your views here.


def singup(request):
    if request.method == 'GET':
        return render(request, "signup.html", {
            'form': UserCreationForm,
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('inicioUtiles')
            except IntegrityError:
                return render(request, "signup.html", {
                    'form': UserCreationForm,
                    'error': 'Usuario ya existe'
                })
        return render(request, "signup.html", {
            'form': UserCreationForm,
            'error': 'Contraseñas no coinciden'
        })

@login_required
def signout(request):
    logout(request)
    return redirect('intranet')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrectas'
            })
        else:
            login(request, user)
            return redirect('inicioUtiles')
