from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from lists.models import Projet
from lists.models import Nature
from objectif.models import Objectif
from .models import Planification 
from planification.forms import PlanificationForm , UpdateTacheForm
from dashboard.models import Dashboard , TaskStats
from .filters import planification_filtrer

# Create your views here.
@login_required(login_url='acces')
def fplan(request):
    date_tache=Planification.objects.all().filter(user=request.user).order_by('-id') 
    projets=Projet.objects.all().filter(user=request.user).order_by('-id') 
    natures=Nature.objects.all().filter(user=request.user).order_by('-id') 
    obj=Objectif.objects.all().filter(user=request.user).order_by('-id') 
    taches=Planification.objects.all().filter(user=request.user).order_by('-id') 
    filterPlanification=planification_filtrer(request.GET , queryset=taches)
    taches=filterPlanification.qs
    context = {'projets':projets , 'natures':natures, 'obj':obj , 'taches':taches , 'filterPlanification':filterPlanification}
    return render(request , 'planification/planification.html' , context)



@login_required(login_url='acces')
def create_tache(request):
    
  if request.method == "POST":
      form = PlanificationForm(request.user , request.POST )
      if form.is_valid():
          planification = form.save(commit=False)
          planification.user = request.user  # Set the user to the logged-in user 
          planification.save()
          dashboard_data , created = Dashboard.objects.get_or_create(user=request.user)  
          dashboard_data.update_stats()
          dashboard_tasks, created = TaskStats.objects.get_or_create(user=request.user)
          dashboard_tasks.update_stats()
   
         
            # Rest of your code for successful form submission
          return redirect('planification')
  else:
        form = PlanificationForm(request.user)  # Pass the user to the form here
        
  return render(request , 'planification/create_tache.html'  , {'form': form})


@login_required(login_url='acces')
def update_tache(request, pk):

    tache = Planification.objects.get(id=pk)

    form = UpdateTacheForm(instance=tache)

    if request.method == 'POST':

        form = UpdateTacheForm(request.POST, instance=tache)

        if form.is_valid():

            form.save()
       

            return redirect("planification")
        
    context = {'form':form}

    return render(request, 'planification/update-tache.html', context=context)






@login_required(login_url='my-login')
def delete_tache(request, pk):

    tache = Planification.objects.get(id=pk)
    tache.delete()
    dashboard_data , created = Dashboard.objects.get_or_create(user=request.user)  
    dashboard_data.update_stats()
    dashboard_tasks, created = TaskStats.objects.get_or_create(user=request.user)
    dashboard_tasks.update_stats()
   

    return redirect('planification')