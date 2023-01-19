from django.shortcuts import render
from .models import Project

# Create your views here.


def home(request):
    # Grab the project database and push into the render
    projects = Project.objects.all() # grab all the objects of the database
    #print(projects)
    return render(request, 'portfolio/home.html', {'projects':projects})