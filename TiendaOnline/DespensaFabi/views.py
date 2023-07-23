from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, update_session_auth_hash
from .forms import RegistrationForm, ChangePasswordForm, UserEditForm


def Home(request):
    return render(request, "AppDespensaFabi/home.html")


def Producto(request):
    return render(request, "AppDespensaFabi/producto.html")


def Carrito (request):
    return render(request, "AppDespensaFabi/carrito.html")


def Perfilviews (request):
    usuario = request.user
    try:
        perfil = UserProfile.objects.get(user=usuario)
    except UserProfile.DoesNoExist:
        perfil = None

    return render(request, "AppDespensaFabi/perfil.html")


def registro(request):
    if request.user.is_authenticated:
        return redirect('Home')
    else:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                nacionalidad = form.cleaned_data['nacionalidad']
                nacimiento = form.cleaned_data['nacimiento']
                ciudad = form.cleaned_data['ciudad']
                postal = form.cleaned_data['postal']
                direccion = form.cleaned_data['direccion']

                perfil = UserProfile(user=user, nacionalidad=nacionalidad, nacimiento=nacimiento, ciudad=ciudad,
                                     postal=postal, direccion=direccion)
                perfil.save()

                return redirect('../login')
        else:
            form = RegistrationForm()

        if form.errors:
            for field, error in form.errors.items():
                messages.error(request, f"{field.capitalize()}: {error.as_text()}")

        return render(request, 'AppDespensaFabi/registro.html', {'form': form})


def login_views (request):
    if request.user.is_authenticated:
        return redirect('Home')
    else:
        if request.method == 'POST':
            username = request.POST['user']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'AppDespensaFabi/home.html')
            else:
                return render(request, 'AppDespensaFabi/login.html', {'error': 'Username o contraseña incorrectos.'})
        return render(request, 'AppDespensaFabi/login.html')


@login_required
def edit_perfil (request):
    usuario = request.user
    try:
        perfil = UserProfile.objects.get(user=usuario)
    except UserProfile.DoesNoExist:
        perfil = None

    if request.method == "POST":
        form = UserEditForm(request.POST, instance=usuario)
        if forn.is_valid():
            form.save()

            perfil.nacionalidad = form.cleaned_data['nacionalidad']
            perfil.nacimiento = form.cleaned_data['nacimiento']
            perfil.ciudad = form.cleaned_data['ciudad']
            perfil.postal = form.cleaned_data['postal']
            perfil.direccion = form.cleaned_data['direccion']
            perfil.save()

            return redirect('perfil')
