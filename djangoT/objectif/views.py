from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from lists.models import Projet
from lists.models import Nature
from objectif.models import Objectif
from objectif.forms import ObjectifForm  , UpdateObjectifForm
from dashboard.models import ObjectiveStats
from .filters import objectif_filtrer
# Create your views here.
@login_required(login_url='acces')
def fobj(request):
    projets=Projet.objects.all().filter(user=request.user).order_by('-id') 
    natures=Nature.objects.all().filter(user=request.user).order_by('-id') 
    objectifs=Objectif.objects.all()
    filterObjectif = objectif_filtrer(request.GET, queryset=Objectif.objects.all(), user=request.user)
    objectifs=filterObjectif.qs
    context={'projets':projets , 'natures':natures , 'objectifs':objectifs , 'filterObjectif':filterObjectif}
    
    return render(request , 'objectif/objectif.html',context)




from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Objectif
from .forms import ObjectifForm

@login_required(login_url='acces')
def create_objectif(request):
    if request.method == "POST":
        form = ObjectifForm(request.user, request.POST)
        if form.is_valid():
            objectif = form.save(commit=False)
            objectif.user = request.user  # Set the user to the logged-in user
            objectif.save()
            dashboard_objectives, created = ObjectiveStats.objects.get_or_create(user=request.user)
            dashboard_objectives.update_stats()
            # Rest of your code for successful form submission
            return redirect('objectif')
    else:
        form = ObjectifForm(request.user)  # Pass the user to the form here

    context = {'form': form}
    return render(request, 'objectif/create_objectif.html', context)


@login_required(login_url='acces')
def update_objectif(request, pk):

    objectif = Objectif.objects.get(id=pk)
    if objectif.user == request.user:
       form = UpdateObjectifForm(instance=objectif)

       if request.method == 'POST':

        form = UpdateObjectifForm(request.POST, instance=objectif)

        if form.is_valid():

            form.save()
            

            return redirect("objectif")
        
    context = {'form':form}

    return render(request, 'objectif/update-objectif.html', context=context)






@login_required(login_url='my-login')
def delete_objectif(request, pk):

    objectif = Objectif.objects.get(id=pk)

    objectif.delete()
    dashboard_objectives, created = ObjectiveStats.objects.get_or_create(user=request.user)
    dashboard_objectives.update_stats()

    return redirect('objectif')