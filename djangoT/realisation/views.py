from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from lists.models import Projet
from lists.models import Nature
from planification.models import Planification
from realisation.forms import RealisationForm
from .models import Realisation
from .filters import realisation_filtrer
from dashboard.models import Dashboard

@login_required(login_url='acces')
# Create your views here.


def freal(request):

    projets=Projet.objects.all().filter(user=request.user).order_by('-id') 
    natures=Nature.objects.all().filter(user=request.user).order_by('-id') 
    taches=Planification.objects.all().filter(user=request.user).order_by('-id') 
    livrables=Realisation.objects.all().filter(user=request.user).order_by('-id') 
    filterRealisation=realisation_filtrer(request.GET , queryset=livrables)
    livrables=filterRealisation.qs
    context = {'projets':projets , 'natures':natures , 'taches':taches , 'livrables':livrables , 'filterRealisation':filterRealisation}  
    return render(request , 'realisation/realisation.html' , context)


@login_required(login_url='acces')
def valider_realisation(request):
    if request.method == "POST":
        form = RealisationForm(request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            realisation = form.save(commit=False)
            realisation.user = request.user  # Set the user field here
            realisation.save()
            dashboard_data , created = Dashboard.objects.get_or_create(user=request.user)  
            dashboard_data.update_stats()
   
            return redirect('realisation')
        else:
            print("Form is not valid:")
            print(form.errors)
            return redirect('realisation')
    else:
        form = RealisationForm(user=request.user)
       
    return render(request, 'realisation/valider_realisation.html', {'form': form})






@login_required(login_url='acces')
def singular_realisation(request, pk):

    all_realisation = Realisation.objects.get(id=pk)

    context = {'realisation':all_realisation}

    return render(request, 'Realisation/view-record.html', context=context)

