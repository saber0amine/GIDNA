from django.shortcuts import render, redirect
from django.http import HttpResponse
# from login.models import Login
from lists.models import Lists
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate
from django.contrib import messages
from lists.models import Projet , Nature , Emplacement
from lists.forms import ProjetForm ,  NatureForm, EmplacementForm , UpdateProjetForm , UpdateNatureForm , UpdateEmplacementForm
from dashboard.models import ProjectStats
from .filters import filtrer_par_projet , filtrer_par_nature ,  filtrer_par_emplacement


# login required for acces
@login_required(login_url='acces')
def flists(request):
    emplacements=Emplacement.objects.filter(user=request.user).order_by('-id')
    projets=Projet.objects.filter(user=request.user).order_by('-id')
    natures=Nature.objects.filter(user=request.user).order_by('-id')
    # users=Login.objects.filter(user=request.user).order_by('-id')
    lists=Lists.objects.filter(user=request.user).order_by('-id')
    filterProjet=filtrer_par_projet(request.GET , queryset=projets , request=request)
    projets=filterProjet.qs 
    filterNature=filtrer_par_nature(request.GET , queryset=natures , request=request)
    natures=filterNature.qs
    filterEmplacement=filtrer_par_emplacement(request.GET , queryset=emplacements , request=request)
    emplacements=filterEmplacement.qs
    context = {'lists':lists , 'projets':projets , 'natures':natures , 'emplacements':emplacements , 'filterProjet':filterProjet , 'filterNature':filterNature ,'filterEmplacement':filterEmplacement }
    return render(request , 'lists/lists.html'  , context)




@login_required(login_url='my-login')
def create_projet(request):
    if request.method == "POST":
        form = ProjetForm(request.POST)
        if form.is_valid():
            projet = form.save(commit=False)
            projet.user = request.user
            projet.save()

            # Create or update the ProjectStats record
            dashboard_project, created = ProjectStats.objects.get_or_create(user=request.user)
            dashboard_project.update_stats()

            return redirect('lists')
        else:
            print("Form is not valid")
            return redirect('lists')
    else:
        form = ProjetForm()

    return render(request, 'lists/create_projet.html', {'form': form})







@login_required(login_url='my-login')
def delete_projet(request, pk):

    projet = Projet.objects.get(id=pk)

    projet.delete()
    
            # Create or update the ProjectStats record
    dashboard_project, created = ProjectStats.objects.get_or_create(user=request.user)
    dashboard_project.update_stats()

    return redirect("lists")





@login_required(login_url='acces')
def create_nature(request):
  form = NatureForm()

  if request.method == "POST":
      form = NatureForm(request.POST or None)
      if form.is_valid():
          nature=form.save(commit=False)
          nature.user = request.user
          nature.save()
          return redirect('lists')
      else:
          print("form is not valid")
          return redirect('lists')

  return render(request , 'lists/create_nature.html'  , {'form': form})





@login_required(login_url='acces')
def create_emplacement(request):
  form = EmplacementForm()

  if request.method == "POST":
      form = EmplacementForm(request.POST or None)
      if form.is_valid():
          emplacement=form.save(commit=False)
          emplacement.user = request.user
          emplacement.save()
          return redirect('lists')
      else:
          print("form is not valid")
          return redirect('lists')

  return render(request , 'lists/create_emplacement.html'  , {'form': form})





@login_required(login_url='acces')
def update_projet(request, pk):

    projet = Projet.objects.get(id=pk)

    form = UpdateProjetForm(instance=projet)

    if request.method == 'POST':

        form = UpdateProjetForm(request.POST, instance=projet)

        if form.is_valid():

            form.save()

            return redirect("lists")
        
    context = {'form':form}

    return render(request, 'lists/update-projet.html', context=context)





@login_required(login_url='acces')
def update_projet(request, pk):

    projet = Projet.objects.get(id=pk)

    form = UpdateProjetForm(instance=projet)

    if request.method == 'POST':

        form = UpdateProjetForm(request.POST, instance=projet)

        if form.is_valid():

            form.save()

            return redirect("lists")
        
    context = {'form':form}

    return render(request, 'lists/update-projet.html', context=context)







@login_required(login_url='acces')
def update_nature(request, pk):

    nature = Nature.objects.get(id=pk)

    form = UpdateNatureForm(instance=nature)

    if request.method == 'POST':

        form = UpdateNatureForm(request.POST, instance=nature)

        if form.is_valid():

            form.save()

            return redirect("lists")
        
    context = {'form':form}

    return render(request, 'lists/update-nature.html', context=context)






@login_required(login_url='my-login')
def delete_nature(request, pk):

    nature = Nature.objects.get(id=pk)

    nature.delete()

    return redirect('lists')







@login_required(login_url='acces')
def update_emplacement(request, pk):

    emplacement = Emplacement.objects.get(id=pk)

    form = UpdateEmplacementForm(instance=emplacement)

    if request.method == 'POST':

        form = UpdateEmplacementForm(request.POST, instance=emplacement)

        if form.is_valid():

            form.save()

            return redirect("lists")
        
    context = {'form':form}

    return render(request, 'lists/update-emplacement.html', context=context)








@login_required(login_url='my-login')
def delete_emplacement(request, pk):

    emplacement = Emplacement.objects.get(id=pk)

    emplacement.delete()

    return redirect('lists')