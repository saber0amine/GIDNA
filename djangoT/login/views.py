from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .forms import creerUtilisateur
from dashboard.models import ProjectStats , Dashboard , TaskStats , ObjectiveStats



# Create your views here.

def flogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password=  request.POST.get('password')
        user=authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            ProjectStats.objects.get_or_create(user=user)  # Create or get the ProjectStats record
            Dashboard.objects.get_or_create(user=user)  # Create or get the ProjectStats record
            TaskStats.objects.get_or_create(user=user)  # Create or get the ProjectStats record
            ObjectiveStats.objects.get_or_create(user=user)  # Create or get the ProjectStats record

            return redirect('dashboard')
        else :
            messages.error(request,'Username or Password incorrect!')           
    return render(request , 'login/login.html')


def finscription(request):
    form=creerUtilisateur()
    if request.method == "POST":
        form=creerUtilisateur(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Bravo '+ user +' :votre compte a été crée avec succes')
            return redirect('acces')
    context={'form' :form}
    return render ( request, "login/inscription.html" , context)


def flogout(request):
    logout(request)
    return redirect('acces')