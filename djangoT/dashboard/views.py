from django.shortcuts import render
from lists.models import Projet
from realisation.models import Realisation  # Import your Project model

# Create your views here.
from django.shortcuts import render
from dashboard.models import Dashboard , ProjectStats , TaskStats , ObjectiveStats

def fdash(request): 
    # Fetch data from the Dashboard model
    dashboard_data = Dashboard.objects.filter(user=request.user).first()
    dashboard_project = ProjectStats.objects.filter(user=request.user).first()
    number_projects = dashboard_project.total_projects
    dashboard_tasks = TaskStats.objects.filter(user=request.user).first()
    number_tasks = dashboard_tasks.total_tasks
    dashboard_objectives = ObjectiveStats.objects.filter(user=request.user).first()

    number_objectifs = dashboard_objectives.total_objectives
    task_realiser = dashboard_data.task_realiser
    task_non_realiser = dashboard_data.task_non_realiser
   

    context = {
        'task_realiser': task_realiser,
        'task_non_realiser': task_non_realiser,
        'number_projects': number_projects,
        'number_tasks': number_tasks,
        'number_objectifs': number_objectifs,
        
    }
    return render(request, 'dashboard/dashboard.html', context=context)

